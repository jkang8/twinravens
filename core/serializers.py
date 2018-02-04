from rest_framework.serializers import ModelSerializer

from core.models import Stop, Trip, User, Gps


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class GuestSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StopSerializer(ModelSerializer):
    class Meta:
        model = Stop
        fields = '__all__'


class GpsSerializer(ModelSerializer):
    class Meta:
        model = Gps
        fields = '__all__'
