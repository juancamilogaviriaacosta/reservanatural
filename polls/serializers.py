from django.core import serializers

class Serializador():

    def to_json(QuerySet):
        data = serializers.serialize("json", QuerySet)
        return data