from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Company(models.Model):
    COMPANY_SIZES = (
        ('10-100', 'Small'),
        ('101-500', 'Medium'),
        ('501-1000', 'Large'),
        ('1000+', 'ExtraLarge'),
    )
    company_name = models.CharField(max_length=50)
    company_logo = models.ImageField(
        null=True, blank=True, upload_to="images/", max_length=50)
    company_size = models.CharField(max_length=10, choices=COMPANY_SIZES)
    company_created_by = models.CharField(max_length=50, blank=True)
    company_created_at = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.company_name


# class Album(models.Model):
#     artist = models.ForeignKey(Company, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     release_date = models.DateField()
#     num_stars = models.IntegerField()
