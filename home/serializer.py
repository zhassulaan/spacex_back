from rest_framework import serializers
from home.models import Menu, Advantage

class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = Menu
		fields = ('id', 'route', 'text')

class AdvantageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Advantage
		fields = ('id', 'name', 'number', 'description')
