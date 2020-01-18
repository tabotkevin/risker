from risks.models import Risk, Field, Text, Number, Enum, Date
from risks.helpers import get_field_value
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from risks.serializers import RiskSerializer, FieldSerializer
 
 
class RiskList(generics.ListCreateAPIView):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
 
    def perform_create(self, serializer):
        serializer.save()
 
 
class RiskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RiskSerializer
 
    def get_queryset(self):
        return Risk.objects.all().filter()


class FieldList(generics.ListCreateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
 
    def perform_create(self, serializer):
        risk_id = self.request.data.get('risk_id')
        val = self.request.data.get('value')
        type = self.request.data.get('type')
        value = get_field_value(type, val)
        serializer.save(risk_id=risk_id, value=value)

 
 
class FieldDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FieldSerializer
 
    def get_queryset(self):
        return Field.objects.all().filter()


    def perform_update(self, serializer):
        val = self.request.data.get('value')
        type = self.request.data.get('type')
        value = get_field_value(type, val)
        serializer.save(value=value)


class FieldRiskList(generics.ListCreateAPIView):
    serializer_class = FieldSerializer
 
    def perform_create(self, serializer):
        serializer.save()

    
    def get_queryset(self):
        id = self.kwargs.get('pk')
        if id is not None:
            risk = Risk.objects.filter(id=int(id)).first()
            if risk is not None:
                self.queryset = risk.field_set.all()
        return self.queryset