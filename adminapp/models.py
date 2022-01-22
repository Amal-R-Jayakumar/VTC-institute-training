from django.db import models
# from courses.models import Course

class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Corporation(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Municipality(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Panchayath(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class VTCListExcel(models.Model):
    excel_file = models.FileField(upload_to='excel/files')



