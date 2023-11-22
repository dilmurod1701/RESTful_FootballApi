from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from django.core.mail import send_mail
from django.contrib.auth import login

# Local application packages
from .serializers import ReminderSerializer, GameSerializer, SignupSerializer, LoginSerializer
from .models import Game, Email
from Football.settings import EMAIL_HOST_USER


# Create your views here.


class GameScheduleView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


Email = str


class Email_Sender(APIView):
    queryset = Email
    serializer_class = ReminderSerializer

    def post(self, request):
        global Email
        serializer = ReminderSerializer(data=request.data)
        response = ReminderSerializer(data=request.data.get('email'))
        Email = response.initial_data
        to_mail = [Email]
        send_mail('New game',
                  'Don\'t forget to watch game! I will send you the link when match started!',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=to_mail,
                  fail_silently=False
                  )
        print(f'Message sent to {Email}')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class Search(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['home_team', 'away_team']


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=self.request.data,
                                     context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response('Muvafaqiiyatli otdingiz')


class Signup(CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]


def migration(request):
    import os
    os.system('python3 manage.py makemigrations')
    os.system('python3 manage.py migrate --no-input')
    return HttpResponse('migration done')
