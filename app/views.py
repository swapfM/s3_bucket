from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import UserModel
from rest_framework import status
from django.http import Http404, HttpResponseNotFound
from .forms import UserForm


# Create your views here.


class DataList(APIView):

    def get_object(self, pk):
        try:
            return UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        data = UserModel.objects.all()
        serializer = UserSerializer(data, many=True)

        list = []

        for i in range(len(serializer.data)):
            list.append(serializer.data[i]['Pic'])

        context = {
            'videos': list,
        }

        return render(request, 'index.html', context)

    def post(self, request, format=None):

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):

        data = self.get_object(pk)
        data.Pic.delete(save=False)
        data.delete()
        return Response(status=222)


