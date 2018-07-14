from django.db import models
from django.utils import timezone


class HomePage(models.Model):
	carousel_image1 = models.ImageField(max_length=100)
	carousel_image2 = models.ImageField(max_length=100)
	carousel_image3 = models.ImageField(max_length=100)
	welcome_header = models.CharField(max_length=50)
	welcome_text = models.TextField(max_length=1500)
	supply_header = models.CharField(max_length=50)
	supply_text = models.TextField(max_length=1500)
	our_service_header = models.CharField(max_length=50)
	our_service_text = models.TextField(max_length=1500)


	def __str__(self):
		self.welcome_header


#THIS IS THE CONTACT MODEL TO RECEIVE CONTACTS
'''class Contact(models.Model):
    name = models.CharField("full name", max_length=120)
    company = models.CharField("company name", max_length=120)
    email = models.EmailField("email address", max_length=120)
    message = models.TextField()
    email_date = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True

    def __str__(self):
        return self.name
'''

# Create your models here.
