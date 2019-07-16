from django.db import models

# Create your models here.


class Tracks(models.Model):
    tail_number = models.CharField(verbose_name='tail_number', max_length=256)
    track_model = models.CharField(verbose_name='track_model', max_length=256)
    max_load_capacity = models.IntegerField(verbose_name='load_capacity')
    current_weight = models.IntegerField(verbose_name='current_weight')

    def __str__(self):
        return self.tail_number


class TracksChoice(models.Model):
    trk_model = models.CharField(verbose_name='track_choice_model', max_length=256)

    def __str__(self):
        return self.trk_model
