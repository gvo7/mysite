from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254)
    business_phone = models.CharField(max_length=20)
    standby_phone = models.CharField(max_length=20)
    teamleader = models.CharField(max_length=50)
    sdo = models.CharField(max_length=50)

    def __str__(self):
        return self.name


#class Configuration_owner(models.Model):
#    name = models.CharField(max_length=50)
#    email = models.EmailField(max_length=254)
#    teamleader = models.CharField(max_length=50)
#    sdo = models.CharField(max_length=50)
#
#    def __str__(self):
#        return self.name
class Configuration_owner(models.Model):
    name = models.ForeignKey(Team, to_field='name', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class Management(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Service_status(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)
    contact = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField(max_length=254)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    shipping_contact = models.CharField(max_length=100)
    shipping_contact_phone = models.CharField(max_length=20)
    shipping_contact_email = models.EmailField(max_length=254)
    shipping_address = models.CharField(max_length=200)
    shipping_city = models.CharField(max_length=100)
    shipping_zip_code = models.CharField(max_length=20)
    shipping_country = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Integrator(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email_support = models.EmailField(max_length=254)
    account_manager = models.CharField(max_length=100)
    email_account_manager = models.EmailField(max_length=254)
    service_manager = models.CharField(max_length=100)
    email_service_manager = models.EmailField(max_length=254)
    contract_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email_support = models.EmailField(max_length=254)
    account_manager = models.CharField(max_length=100)
    email_account_manager = models.EmailField(max_length=254)
    service_manager = models.CharField(max_length=100)
    email_service_manager = models.EmailField(max_length=254)
    contract_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    vendor = models.ForeignKey(Vendor)
    product_name = models.CharField(max_length=50, unique=True)
    type =  models.ForeignKey(Type)
    eos_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    eol_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    logging_template = models.CharField(max_length=500)
    monitoring_template = models.CharField(max_length=500)

    def __str__(self):
        return str(self.vendor) + ' - ' + self.product_name + ' - ' + self.logging_template + ' - ' + self.monitoring_template 


class Device(models.Model):
    assettag = models.CharField(max_length=20, unique=True)
    hostname = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor)
    product = models.ForeignKey(Product)
    serial_number = models.CharField(max_length=50, unique=True)
    #configuration_owner = models.ForeignKey(Configuration_owner)
    operational_support_team = models.ForeignKey(Team, related_name='operational_support')
    standby_support_team = models.ForeignKey(Team, related_name='standby_support')
    integrator = models.ForeignKey(Integrator)
    management_ipv4 = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    management_ipv6 = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, blank=True, null=True)
    management_interface = models.ForeignKey(Management)
    os_version = models.CharField(max_length=20)
    support_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    location = models.ForeignKey(Location)
    service_status = models.ForeignKey(Service_status)
    last_backup = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)


    def __str__(self):
        return self.assettag + ' - ' + str(self.vendor) + ' - ' + str(self.product) + ' - ' + self.serial_number + ' - ' + str(self.configuration_owner) + ' - ' + str(self.integrator) + ' - ' + self.management_ipv4 + ' - ' + self.os_version