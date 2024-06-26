from django.shortcuts import render
from rest_framework import generics, viewsets, pagination
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from .models import *
from .serializers import *


class AllSourcePagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'


# Класс, где происходит фильтрация по языку программирования, полученному в запросе с фронта. Результат из GitHub
class GitHubLanguageViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        language = self.request.query_params.get('language').split(',')
        user_id = GithubRawRepos.objects.filter(language__in=language).values('owner_id')
        queryset = GithubRawUsers.objects.filter(user_id__in=user_id)
        return queryset

    serializer_class = LanguageSerializer


class AllSourceCityViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        city = self.request.query_params.getlist('city')
        language = self.request.query_params.getlist("language")
        job = self.request.query_params.get("job")
        user_id = self.request.query_params.getlist("id")
        queryset = AllSourceUsersEnriched.objects.all()
        # Формируем условия для фильтрации
        conditions = Q()  # Пустой Q-объект
        if city:
            conditions &= Q(city__in=city)
        if job:
            conditions &= Q(jobtitle__icontains=job)
        if language:
            conditions &= Q(programming_languages__contains=language)
        if user_id:
            conditions &= Q(user_id__in=user_id)

        # Применяем условия к queryset
        if conditions:
            queryset = queryset.filter(conditions)

        return queryset
    pagination_class = AllSourcePagination
    serializer_class = AllSourceSerializer


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
