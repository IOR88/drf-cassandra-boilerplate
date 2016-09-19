from django_cassandra_engine.serializers import DjangoCassandraModelSerializer


from .models import CassandraAdventuresModel_1


class CassandraAdventuresSerializer(DjangoCassandraModelSerializer):

    class Meta:
        model = CassandraAdventuresModel_1
        fields = '__all__'
