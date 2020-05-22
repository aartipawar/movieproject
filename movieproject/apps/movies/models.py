from django.db import models
from django.utils.translation import ugettext_lazy as _

class Movie(models.Model):
    movie = models.CharField(max_length=250)
    description = models.TextField(_("Descrption"), blank = True, null = True)
    year = models.IntegerField(verbose_name =_('Release Year'))
    rating = models.FloatField(_("Movie Rating"), blank = True, null = True)
    cast = models.TextField(_("Cast"), blank = True, null = True)

    class Meta:
       managed = True
       ordering = ['-id']