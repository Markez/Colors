from rest_framework import generics, mixins
from .serializers import CompanySerializer, RangiSerializer
from rangi.models import Rangi, Company
from rest_framework.permissions import AllowAny


# this shows all the companies that are created
# this for adding a new company
class CompanyApiView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CompanySerializer
    permission_classes =(AllowAny,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        return Company.objects.all()


# this view shows all the rangis that are there in the database
# This for creating a new Rangi
class RangiApiView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = RangiSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        return Rangi.objects.all()


# opens one object at a time
# The endpoints now
class CompanyRudApiView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CompanySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Company.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


# this view opens one object at a time
# The endpoints now
class RangiRudApiView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = RangiSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Rangi.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
