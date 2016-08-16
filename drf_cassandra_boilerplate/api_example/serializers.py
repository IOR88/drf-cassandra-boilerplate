from rest_framework.serializers import Serializer
from rest_framework.fields import URLField, CharField, DateTimeField


class CassandraAdventureSerializer(Serializer):
    adventure_id = URLField(format='hex_verbose')
    adventure_desc = CharField()
    last_modified = DateTimeField()