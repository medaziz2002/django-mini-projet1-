from django.db import models

class Competance(models.Model) :
   competance_languistique = models.CharField(max_length=80)
   competance_technique = models.CharField(max_length=80)

class Formation(models.Model) :
    intitule=models.CharField(max_length=80)
    date=models.DateField()
    lieu=models.CharField(max_length=80)

class Stage(models.Model) :
    intitule=models.CharField(max_length=80)
    date=models.DateField()
    lieu=models.CharField(max_length=80)