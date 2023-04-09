from django.db import models

# Create your models here.
class Brew(models.Model):
    grind_size = models.IntegerField(max_length=255)
    brew_time = models.DurationField()
    yield_ratio = models.DecimalField(max_digits=5, decimal_places=2)
    beans_fk = models.ForeignKey('Bean', on_delete=models.CASCADE)

    class Meta:
        db_table = 'espresso.brew'

class Bean(models.Model):
    name = models.CharField(max_length=255)
    roast = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    notes = models.TextField()
    purchase_location = models.CharField(max_length=255)
    purchase_date = models.DateField()
    roast_date = models.DateField()
    freeze_date = models.DateField()
    first_unfreeze_date = models.DateField()
    second_unfreeze_date = models.DateField()

    class Meta:
        db_table = 'espresso.bean'


    