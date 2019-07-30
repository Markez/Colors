from rest_framework import serializers
from rangi.models import Rangi, Company


class CompanySerializer(serializers.ModelSerializer):


    class Meta:
        model = Company
        fields = [
            'company_name',
            'location',
        ]

    def get_url(self, obj):
        # request
        # this will find the complete url build is from the model.py and views.py

        request = self.context.get("request")
        return obj.get_api_url(request=request)


class RangiSerializer(serializers.ModelSerializer):


    class Meta:
        model = Rangi
        fields = [

            'color_type',
            'rangi',
            'brand',

        ]

    def get_url(self, obj):
        # request
        # this will find the complete url build is from the model.py and views.py

        request = self.context.get("request")
        return obj.get_api_url(request=request)
