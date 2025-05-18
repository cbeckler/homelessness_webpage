from django.db import models

# Create your models here.
class HomelessCities(models.Model):
    city = models.CharField(max_length=200)
    population = models.IntegerField()
    homeless = models.IntegerField()
    proportion = models.FloatField()

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.city, self.population, self.homeless, self.proportion)