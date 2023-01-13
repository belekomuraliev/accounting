from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


from .models import Position, Employees, User
from .serializer import PositionSerializer, EmployeeSerializer, UserSerializer


class UserListCreate(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class PositionListCreateAPIView(ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['department', 'title']
    ordering_fields = ['department', 'title']


class PositionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['fullname', 'salary']
    ordering_fields = ['fullname', 'salary']


class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]



