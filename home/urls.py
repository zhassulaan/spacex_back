from django.urls import path
from rest_framework import routers
from .views import AdvantageAPIView, MenuAPIView

router = routers.SimpleRouter()

urlpatterns = [
    path('menu/', MenuAPIView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', MenuAPIView.as_view(), name='menu-detail'),
    path('advantages/', AdvantageAPIView.as_view(), name='advantages-list'),
    path('advantages/<int:pk>/', AdvantageAPIView.as_view(), name='advantage-detail'),
]

urlpatterns += router.urls