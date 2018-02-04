from rest_framework import generics, renderers, status, viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Location, Stop, Trip, User
from core.serializers import GuestSerializer
from .serializers import LocationSerializer, StopSerializer, TripSerializer, \
    UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class StopViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Stop.objects.all().order_by('when')
    serializer_class = StopSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Location.objects.all().order_by('name')
    serializer_class = LocationSerializer


class TripViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


@api_view(['GET'])
def trip_itinerary(request, trip_pk):
    """
        Retrieve, update or delete a code snippet.
        """
    try:
        trip = Trip.objects.get(pk=trip_pk)
        guest_list = trip.guests.all()
        stops_list = trip.stops.all().order_by('when')

        trip_itinerary_data = {
            'trip': TripSerializer(trip).data,
        }
        trip_itinerary_data['trip']['guests'] = GuestSerializer(guest_list, many=True).data
        trip_itinerary_data['trip']['stops'] = StopSerializer(stops_list, many=True).data
    except Trip.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(trip_itinerary_data)

    return Response(status.HTTP_400_BAD_REQUEST)


class TripDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class Gps