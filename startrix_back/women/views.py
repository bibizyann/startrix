from django.shortcuts import render
from rest_framework import generics, viewsets, pagination
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


# Класс, где происходит фильтрация по языку программирования, полученному в запросе с фронта
class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        language = self.request.query_params.get('language').split(',')
        user_id = GithubRawRepos.objects.filter(language__in=language).values('owner_id')
        queryset = GithubRawUsers.objects.filter(user_id__in=user_id)
        return queryset
    serializer_class = LanguageSerializer


# class CountryFilter(generics.ListCreateAPIView):
#     queryset = GithubRawUsers.objects.filter(location='Moscow').values()
#     serializer_class = CountrySerializer


# class CountryFilter(APIView):
#     def get(self, request):
#         lst = GithubRawUsers.objects.filter(location='Moscow').values()
#         return Response({'data': CountrySerializer(lst, many=True).data})
#
#     def post(self, request):
#         return Response({'name': 'Boris Jonson'})

# class CountryFilter(generics.ListAPIView):
#     queryset = GithubRawUsers.objects.filter(location='Russia')
#     serializer_class = CountrySerializer