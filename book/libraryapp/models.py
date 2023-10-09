from django.db import models
class SampleModel(models.Model):
field1 = models.CharField(max_length = 50)
field2 = models.IntegerField()
class Meta:
db_table = “sample_model”
