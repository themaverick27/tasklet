from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from board.serializers import BoardSerializers
from board.models import Board
from list.models import List
from list.serializers import ListSerializers
from django.core.exceptions import PermissionDenied

# Create your views here.
class BoardViewSet(ModelViewSet):
    serializer_class = BoardSerializers
    queryset = Board.objects.all()

    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

# Get lists for a board
class BoardListAPIView(ListCreateAPIView):
    serializer_class = ListSerializers

    def get_queryset(self):
        board_id = self.kwargs['board_id']
        board = Board.objects.filter(id=board_id, owner=self.request.user).first()
        if not board:
            raise PermissionDenied("You do not have permission to access this board's lists")
        return List.objects.filter(board=board)

    def perform_create(self, serializer):
        board_id = self.kwargs['board_id']
        board = Board.objects.filter(id=board_id, owner=self.request.user).first()
        if not board:
            raise PermissionDenied("You do not have permission to add lists to this board")
        serializer.save(board=board)