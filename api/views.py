# Third Party Modules
from rest_framework import viewsets

# App Modules
from measurements.models import Measurement
from accounts.models import User
from .serializers import MeasurementSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
