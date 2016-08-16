from django.db import models
from cassandra.cqlengine.models import Model as CassandraModel
from cassandra.cqlengine import columns as CassandraColumns
# Create your models here.


class CassandraAdventuresModel(CassandraModel):
    adventure_id = CassandraColumns.UUID(primary_key=True)
    adventure_desc = CassandraColumns.Text()
    last_modified = CassandraColumns.DateTime()
