from rest_framework.serializers import Serializer
from rest_framework.fields import UUIDField, CharField, DateTimeField


class CassandraAdventureSerializer(Serializer):
    adventure_id = UUIDField(format='hex_verbose')
    adventure_desc = CharField()
    last_modified = DateTimeField()
