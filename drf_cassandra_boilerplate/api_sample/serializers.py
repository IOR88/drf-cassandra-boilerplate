from django_cassandra_engine.serializers import DjangoCassandraModelSerializer


from .models import CassandraAdventuresModel\
    , CassandraAdventuresModel_M


class CassandraAdventuresSerializer(DjangoCassandraModelSerializer):

    class Meta:
        model = CassandraAdventuresModel
        fields = '__all__'


class CassandraAdventuresSerializer_M(DjangoCassandraModelSerializer):

    class Meta:
        model = CassandraAdventuresModel_M
        fields = '__all__'