from django.db import models
from datetime import datetime


EVENT_TYPES = [
    ('spray', 'Spread/Spray'),
    ('tillage', 'Tillage'),
    ('plant', 'Plant'),
    ('harvest', 'Harvest'),
    ('soil_sampling', 'Soil Sampled')
]



# Create your models here.
class event(models.Model):
    # event_date = models.DateTimeField(default=datetime.now, blank=True)
    event_types = models.CharField(choices=EVENT_TYPES, max_length=50)

    def __str__(self):
        return self.event_id



class operator(models.Model):
    operator_name = models.CharField(max_length=50)

    def __str__(self):
        return self.operator_name



class location(models.Model):
    location_name = models.CharField(max_length=50)

    def __str__(self):
        return self.location_name



class seed(models.Model):
    seed_planted = models.CharField(max_length=50)
    seed_rate = models.IntegerField()

    def __str__(self):
        return self.seed_planted
    


class fertilizer(models.Model):
    fertilizer_type = models.CharField(max_length=50)
    fertilizer_rate = models.IntegerField()

    def __str__(self):
        return self.fertilizer_type



class powerunit(models.Model):
    powerunit_type = models.CharField(max_length=50)

    def __str__(self):
        return self.powerunit_type



class log(models.Model):
    log_id = models.ForeignKey(event, on_delete=models.CASCADE)
    log_date = models.DateTimeField(default=datetime.now, blank=True)
    seed = models.ForeignKey(seed, on_delete=models.CASCADE)
    fertilizer = models.ForeignKey(fertilizer, on_delete=models.CASCADE)
    powerunit = models.ForeignKey(powerunit, on_delete=models.CASCADE)
    note = models.TextField()

    def __str__(self):
        return self.log_id