from django.urls import path
from .views import UserView

urlpatterns = [
    # End-point to fetch the user data
    path('users', UserView.as_view({'get': 'list'}), name='user-data')
]