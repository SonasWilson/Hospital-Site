from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)
    

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctors')    

    def __str__(self):
        return self.name + '(' + self.specialization + ')'
    
class Booking(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    doc_name = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)
