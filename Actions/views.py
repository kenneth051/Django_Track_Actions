from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from Actions.serializers import UserSerializer, LoginSerializer, TodoSerializer, HistorySerializer
from Actions.models import User, Todo, History


class UserView(ModelViewSet):
    permission_classes = (AllowAny, )
    serializer_class= UserSerializer
    queryset = User.objects.all()

class LoginView(APIView):
    permission_classes = (AllowAny, )
    serializer_class= LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TodoView(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class= TodoSerializer
    queryset = Todo.objects.all()

class HistoryView(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class= HistorySerializer
    queryset = History.objects.all()
    http_method_names = ["get"]
