from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Game, Email


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['home_team', 'away_team', 'date', 'hour', 'venue']


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(label="Username")
    password = serializers.CharField(label="Password")

    def validate(self, value):
        username = value.get('username')
        password = value.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = 'Xato: Natogri foydalanuvchi nomini kiritingiz'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = '"username" va "password" talab qilinadi.'
            raise serializers.ValidationError(msg, code='authorization')
        value['user'] = user
        return value


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password')
