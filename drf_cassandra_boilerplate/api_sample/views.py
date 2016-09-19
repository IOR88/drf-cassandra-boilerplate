from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import CassandraAdventuresModel\
    , CassandraAdventuresModel_M, CassandraFamilyMember
from .serializers import CassandraAdventuresSerializer\
    , CassandraAdventuresSerializer_M, CassandraFamilyMemberSerializer
# from .filters import CassandraAdventuresFilterSet


class CassandraFamilyMemberViewSet(ModelViewSet):
    queryset = CassandraFamilyMember.objects.all()
    serializer_class = CassandraFamilyMemberSerializer


class CassandraAdventuresViewSet(ModelViewSet):
    queryset = CassandraAdventuresModel.objects.all()
    serializer_class = CassandraAdventuresSerializer
    # filter_class = CassandraAdventuresFilterSet


class CassandraAdventuresViewSet_M(ModelViewSet):
    queryset = CassandraAdventuresModel_M.objects.all()
    serializer_class = CassandraAdventuresSerializer_M
    # filter_class = CassandraAdventuresFilterSet

