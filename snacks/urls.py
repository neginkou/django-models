from django.urls import path
from .views import SnackListView, AboutPageView, SnackDetailView

urlpatterns = [
    path('', SnackListView.as_view(), name='home'),
    path('<int:pk>/', SnackDetailView.as_view(), ),
    path('about/', AboutPageView.as_view(), name='about'),
    path('snacks/', SnackListView.as_view(), name='snack_list'),
]