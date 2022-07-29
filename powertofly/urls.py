from django.urls import path, include

urlpatterns = [
    path('data/', include('users.urls')),
]
