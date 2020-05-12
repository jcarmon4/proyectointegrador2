from rest_framework import viewsets
from .models import Measure
from .serializers import MeasureSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class MeasureViewSet(viewsets.ModelViewSet):
    queryset = Measure.objects.all().order_by('-created')
    serializer_class = MeasureSerializer