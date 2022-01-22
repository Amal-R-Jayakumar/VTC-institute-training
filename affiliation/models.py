from django.db import models
from adminapp.models import District
# Create your models here.

class Affiliation_request(models.Model):
    owner_name = models.CharField(max_length=40)
    email= models.EmailField()
    contact_number = models.CharField(max_length=40)
    location = models.CharField(max_length=60)
    localbodytype = models.CharField(blank=True, max_length=60)
    localbodyname = models.CharField(blank=True, max_length=60)
    district = models.CharField(blank=True, max_length=60)
    pincode = models.CharField(blank=True, max_length=60)
    #district = models.ForeignKey(District, on_delete=models.CASCADE)
    # corporation = models.ForeignKey(Corporation, on_delete=models.CASCADE,null=True)
    # municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,null=True)
    # panchayath = models.ForeignKey(Panchayath, on_delete=models.CASCADE,null=True)
    token = models.CharField(max_length=40,default=False)

    def __str__(self):
        return self.email

class Affiliation_inspection(models.Model):
    name = models.CharField(max_length=50)
    institution_name = models.CharField(max_length=80)
    institution_address= models.CharField(max_length=200)
    contact_number = models.CharField(max_length=40)
    email= models.EmailField()
    localbody_type = models.CharField(max_length=50)
    localbody_name = models.CharField(max_length=50)
    typeof_institution = models.CharField(max_length=50)
    pincode = models.CharField(blank=True, max_length=60)
    nearest_travel = models.CharField(max_length=200)
    distance = models.CharField(max_length=200)
    constituency = models.CharField(max_length=80)
    police_station = models.CharField(max_length=80)
    other_affiliations = models.CharField(max_length=80)
    detailsof_institutions = models.CharField(max_length=80)
    phonenumberof_secretary =  models.CharField(max_length=40)
    distancefrom_localbody = models.CharField(max_length=80)
    area = models.CharField(max_length=80)
    furniture = models.CharField(max_length=80)
    no_oftrainers = models.CharField(max_length=50)
    no_ofcomputers = models.CharField(max_length=50)
    projector = models.CharField(max_length=50)
    white_board = models.CharField(max_length=50)
    toilet = models.CharField(max_length=50)
    internet = models.CharField(max_length=50)
    webcam = models.CharField(max_length=50)
    printer = models.CharField(max_length=50)
    scanner = models.CharField(max_length=50)
    token = models.CharField(max_length=40,default=False)