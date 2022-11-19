from django.db import models

# Create your models here.
class info(models.Model):
  cedula = models.CharField(unique=True, max_length=10)
  name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField( max_length=100)
  date_of_birth = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  phone_number = models.CharField(unique=True, max_length=10)
  vaccination_status = models.CharField(max_length=100)

  #vaccination_type = models.CharField(max_length=100)
  
  vaccination_date = models.CharField(max_length=100)
  vaccination_total_dosis = models.CharField(max_length=1)

  #created_at =models.DateField(auto_now_add=True)

  def __str__(self):
      return self.name