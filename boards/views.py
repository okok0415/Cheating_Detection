from django.shortcuts import render
from rest_framework import generics

from . import models
from .serializers import BoardSerializer


class ListBoard(generics.ListCreateAPIView):
    queryset = models.Board.objects.all()
    serializer_class = BoardSerializer


class DetailBoard(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Board.objects.all()
    serializer_class = BoardSerializer
