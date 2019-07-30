from django.db import models
from rest_framework.reverse import reverse as api_reverse

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=120)

    def __str__(self):
        return self.company_name

        # add the request as an argument inorder to get the actual url

    def get_api_url(self, request=None):
        return api_reverse('api:company-list', kwargs={"pk": self.pk}, request=request)


class Rangi(models.Model):
    color_type = models.CharField(max_length=150)
    rangi = models.CharField(max_length=100)
    brand = models.ForeignKey(Company,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.color_type

    def get_api_url(self, request=None):
        return api_reverse('api:rangi-list', kwargs={"pk": self.pk}, request=request)


