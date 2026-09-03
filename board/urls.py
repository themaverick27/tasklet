from .views import BoardListAPIView, BoardViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'boards', BoardViewSet)

urlpatterns = [
    path('boards/<int:board_id>/lists/', BoardListAPIView.as_view()),
    path('', include(router.urls)),
]