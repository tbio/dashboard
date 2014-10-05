# Third Party Modules
from rest_framework import serializers

# App Modules
from measurements.models import Measurement
from accounts.models import User


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
