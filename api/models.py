from django.db import models
from pandas.core.algorithms import mode

class Atom(models.Model):

    Series = (
        ('',''),
        ('Alkali metals', 'Alkali metals'),
        ('Alkaline earth metals','Alkaline earth metals'),
        ('Lanthanoids','Lanthanoids'),
        ('Actinoids','Actinoids'),
        ('Transition metals', 'Transition metals'),
        ('Post-transition metals', 'Post-transition metals'),
        ('Metalloids', 'Metalloids'),
        ('Reactive nonmetals', 'Reactive nonmetals'),
        ('Noble gases', 'Noble gases'),
        ('Unknown', 'Unknown')
    )

    Name = models.CharField(max_length=200)
    simbolo = models.CharField(max_length=2, default='Z')
    Serie = models.CharField(max_length=200, choices=Series)
    Atomic_number = models.IntegerField(default=0)
    Atomic_mass = models.FloatField()
    Energy_level = models.IntegerField()
    Electronegativity = models.FloatField()
    Electron_affinity = models.FloatField()
    melting_point = models.FloatField()
    vaporization_point = models.FloatField()
    Potencial_de_ionização = models.FloatField()
    Dureza = models.FloatField()
    Módulo = models.FloatField()
    Densidade = models.FloatField()
    Condutividade_termica = models.FloatField()
    Condutividade_eletrica = models.FloatField()
    Calor = models.FloatField()
    Descobrimento = models.IntegerField()

    def __str__(self):
        return self.Name

class Particle(models.Model):

    classes = (
        ('',''),
        ('Quark','Quark'),
        ('Anti-quark', 'Anti-quark'),
        ('Lépton', 'Lépton'),
        ('Anti-lépton', 'Anti-lépton'),
        ('Bóson', 'Bóson'),
    )

    Name = models.CharField(max_length=200)
    simbol = models.CharField(max_length=3)
    mass = models.FloatField()
    charge = models.FloatField()
    spin = models.FloatField()
    classification = models.CharField(max_length=200, choices=classes)

    def __str__(self):
        return self.Name
