from django.db import models
from cassandra.cqlengine.models import Model as CassandraModel
from cassandra.cqlengine import columns as CassandraColumns
# Create your models here.


class CassandraAdventuresModel(CassandraModel):
    adventure_id = CassandraColumns.UUID(primary_key=True)
    adventure_desc = CassandraColumns.Text()
    last_modified = CassandraColumns.DateTime()


# class Dupa(models.Model):
#     id = models.IntegerField(primary_key=True)
#
#
# def ensure_schema(self):
#     """
#     Ensures the table exists and has the correct schema.
#     """
#     # If the table's there, that's fine - we've never changed its schema
#     # in the codebase.
#     if self.Migration._meta.db_table in self.connection.introspection.table_names(self.connection.cursor()):
#         return
#     # Make the table
#     with self.connection.schema_editor() as editor:
#         editor.create_model(self.Migration)