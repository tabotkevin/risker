from rest_framework import serializers
 
from risks.models import Risk, Field, Text, Date, Number, Enum

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('value',)

class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ('value',)

class EnumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enum
        fields = ('value',)

class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = ('value',)

class TypeSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        if isinstance(value, Text):
            serializer = TextSerializer(value)
        elif isinstance(value, Date):
            serializer = DateSerializer(value)
        elif isinstance(value, Number):
            serializer = NumberSerializer(value)
        elif isinstance(value, Enum):
            serializer = EnumSerializer(value)
        else:
            raise Exception('Unexpected type object')

        return serializer.data
 
class RiskSerializer(serializers.HyperlinkedModelSerializer):
 
    class Meta:
        model = Risk
        fields = ('url', 'id', 'created', 'name','description')
        extra_kwargs = {
            'url': {
                'view_name': 'risks:risk-detail',
            }
        }


class FieldSerializer(serializers.HyperlinkedModelSerializer):

    # value = TypeSerializer()
    type = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()

    def get_type(self, obj):
        return obj.type.name

    def get_value(self, obj):
        return obj.value.value

    class Meta:
        model = Field
        fields = ('url', 'id', 'created', 'name', 'value', 'type', 'risk_id')
        read_only_fields = ('type',)
        extra_kwargs = {
            'url': {
                'view_name': 'fields:field-detail',
            }
        }


