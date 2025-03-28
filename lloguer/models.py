from django.db import models
from django.contrib.auth.models import User


class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.marca} {self.model} ({self.matricula})"
    
# crear modelo Reserva que referencie a Automobil i User
# para evitar que se reserve el mismo automobil en un mismo dia se hace una clave unica con la combinación automobil y data_inici
#esto se puede hacer con un unique_together

class Reserva(models.Model):
    automobil = models.ForeignKey(Automobil, on_delete=models.CASCADE)
    usuari = models.ForeignKey(User, on_delete=models.CASCADE)
    data_inici = models.DateField()
    data_final = models.DateField()
    
    class Meta:
        unique_together = ('automobil', 'data_inici')
        
    def __str__(self):
        return f"Reserva de {self.automobil} per {self.usuari} del {self.data_inici} al {self.data_final}"