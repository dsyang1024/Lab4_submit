from django.db import models
from datetime import datetime


EVENT_TYPES = [
    ('seed','Seeding'),
    ('fertilize','Fertilizing'),
    ('irrigate','Irrigating'),
    ('harvest','Harvesting'),
    ('till','Tilling'),
    ('spray','Spraying'),
    ('other','Other')
]



# Create your models here.
class event(models.Model):
    # event_date = models.DateTimeField(default=datetime.now, blank=True)
    event_operator = models.CharField(max_length=50)
    event_operation = models.CharField(choices=EVENT_TYPES, max_length=10)
    event_location = models.CharField(max_length=10)

    def __str__(self):
        return self.event_id
    


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
    seed = models.ForeignKey(seed, on_delete=models.CASCADE)
    fertilizer = models.ForeignKey(fertilizer, on_delete=models.CASCADE)
    powerunit = models.ForeignKey(powerunit, on_delete=models.CASCADE)
    log_date = models.DateTimeField(default=datetime.now, blank=True)
    note = models.TextField()

    def __str__(self):
        return self.log_id