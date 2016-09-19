from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import CassandraAdventuresModel\
    , CassandraAdventuresModel_M
from .serializers import CassandraAdventuresSerializer\
    , CassandraAdventuresSerializer_M
# from .filters import CassandraAdventuresFilterSet


class CassandraAdventuresViewSet(ModelViewSet):
    queryset = CassandraAdventuresModel.objects.all()
    serializer_class = CassandraAdventuresSerializer
    # filter_class = CassandraAdventuresFilterSet


class CassandraAdventuresViewSet_M(ModelViewSet):
    queryset = CassandraAdventuresModel_M.objects.all()
    serializer_class = CassandraAdventuresSerializer_M
    # filter_class = CassandraAdventuresFilterSet