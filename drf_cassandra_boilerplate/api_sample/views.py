from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import CassandraAdventuresModel_1
from .serializers import CassandraAdventuresSerializer
# from .filters import CassandraAdventuresFilterSet


class CassandraAdventuresViewSet(ModelViewSet):
    queryset = CassandraAdventuresModel_1.objects.all()
    serializer_class = CassandraAdventuresSerializer
    # filter_class = CassandraAdventuresFilterSet
