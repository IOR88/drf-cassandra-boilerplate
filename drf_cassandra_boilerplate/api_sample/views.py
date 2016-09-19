from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import CassandraAdventuresModel
from .serializers import CassandraAdventuresSerializer
# from .filters import CassandraAdventuresFilterSet


class CassandraAdventuresViewSet(ModelViewSet):
    queryset = CassandraAdventuresModel.objects.all()
    serializer_class = CassandraAdventuresSerializer
    # filter_class = CassandraAdventuresFilterSet
