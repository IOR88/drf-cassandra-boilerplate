from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import CassandraAdventureSerializer
from .models import CassandraAdventuresModel
# Create your views here.


class ListModelMixin(object):
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CassandraAdventuresAPI(ListModelMixin, GenericAPIView):
    serializer_class = CassandraAdventureSerializer
    queryset = CassandraAdventuresModel.objects.allow_filtering()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
