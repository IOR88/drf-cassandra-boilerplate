from django_cassandra_engine.serializers import DjangoCassandraModelSerializer


from .models import CassandraAdventuresModel


class CassandraAdventuresSerializer(DjangoCassandraModelSerializer):

    class Meta:
        model = CassandraAdventuresModel
        fields = '__all__'
