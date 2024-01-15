from django.db import models

# Create your models here.



class Doctor(models.Model):
    Name = models.CharField(max_length = 50)
    mobile= models.CharField(max_length=15)
    speciality = models.CharField(max_length= 50)


class Patient(models.Model):
    name = models.CharField(max_length = 50)
    gender = models.CharField(max_length= 20)
    mobile = models.IntegerField(null =True)
    address = models.TextField()


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete = models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self) -> str:
        return self.Doctor.Name + " __" + self.Patient.name
