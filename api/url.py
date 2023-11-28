from django.urls import path
from .views import CustomUserView,CustomUserViewDetalist

urlpatterns = [
    path('', CustomUserView.as_view()),
    path('<int:pk>', CustomUserViewDetalist.as_view()),
]