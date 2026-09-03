from .views import ListTaskAPIView, ListViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'lists', ListViewSet)

urlpatterns = [
    path('lists/<int:list_id>/lists/', ListTaskAPIView.as_view()),
    path('', include(router.urls))
]
