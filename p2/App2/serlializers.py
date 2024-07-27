from django.db.models import fields
from rest_framework import serializers
from .models import student

class Std_Serializer(serializers.ModelSerializer):
	class Meta:
		model = student
		fields = ('name','contactno','email','address')