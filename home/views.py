from rest_framework.views import APIView
from django.http.response import Http404
from home.models import Menu, Advantage
from home.serializer import MenuSerializer, AdvantageSerializer
from rest_framework.response import Response

class MenuAPIView(APIView):
	def get_object(self, pk):
		try:
			return Menu.objects.filter(pk=pk)
		except Menu.DoesNotExist:
			raise Http404
	
	def get(self, request, pk=None):
		if pk is not None:
			data = self.get_object(pk)
		else:
			data = Menu.objects.all()
		serializer = MenuSerializer(data, many=True)
		return Response(serializer.data)
	
	def post(self, request, format=None):
		data = request.data
		serializer = MenuSerializer(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		response = Response()
		response.data = {
			'message': 'Menu Created Successfully',
			'data': serializer.data
		}
		return response

	def put(self, request, pk=None, format=None):
		menu = Menu.objects.get(pk=pk)
		serializer = MenuSerializer(instance=menu, data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		response = Response()
		response.data = {
			'message': 'Menu Updated Successfully',
			'data': serializer.data
		}
		return response
	
	def delete(self, request, pk, format=None):
		menu_to_delete = Menu.objects.get(pk=pk)
		menu_to_delete.delete()
		return Response({
				'message': 'Menu Deleted Successfully'
		})


class AdvantageAPIView(APIView):
	def get_object(self, pk):
		try:
			return Advantage.objects.filter(pk=pk)
		except Advantage.DoesNotExist:
			raise Http404
	
	def get(self, request, pk=None):
		if pk is not None:
			data = self.get_object(pk)
		else:
			data = Advantage.objects.all()
		serializer = AdvantageSerializer(data, many=True)
		return Response(serializer.data)
	
	def post(self, request, format=None):
		data = request.data
		serializer = AdvantageSerializer(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		response = Response()
		response.data = {
			'message': 'Advantage Created Successfully',
			'data': serializer.data
		}
		return response

	def put(self, request, pk=None, format=None):
		advantage = Advantage.objects.get(pk=pk)
		serializer = AdvantageSerializer(instance=advantage, data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		response = Response()
		response.data = {
			'message': 'Advantage Updated Successfully',
			'data': serializer.data
		}
		return response
	
	def delete(self, request, pk, format=None):
		advantage_to_delete = Advantage.objects.get(pk=pk)
		advantage_to_delete.delete()
		return Response({
				'message': 'Advantage Deleted Successfully'
		})
