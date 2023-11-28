from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app.models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserViewDetalist(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer