from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Configuration_owner(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    teamleader = models.CharField(max_length=50)
    sdo = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Management(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Service_status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)
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
    name = models.CharField(max_length=50)
    email_support = models.EmailField(max_length=254)
    account_manager = models.CharField(max_length=100)
    email_account_manager = models.EmailField(max_length=254)
    service_manager = models.CharField(max_length=100)
    email_service_manager = models.EmailField(max_length=254)
    contract_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=50)
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
    product_name = models.CharField(max_length=50)
    type =  models.ForeignKey(Type)
    eos_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    eol_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    logging_template = models.CharField(max_length=500)
    monitoring_template = models.CharField(max_length=500)

    def __str__(self):
        return str(self.vendor) + ' - ' + self.product_name + ' - ' + self.logging_template + ' - ' + self.monitoring_template 


class Device(models.Model):
    assettag = models.CharField(max_length=20)
    hostname = models.CharField(max_length=50)
    vendor = models.ForeignKey(Vendor)
    product = models.ForeignKey(Product)
    serial_number = models.CharField(max_length=50)
    configuration_owner = models.ForeignKey(Configuration_owner)
    integrator = models.ForeignKey(Integrator)
    management_ipv4 = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    management_ipv6 = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, blank=True, null=True)
    management_interface = models.ForeignKey(Management)
    os_version = models.CharField(max_length=20)
    support_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    last_backup = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)


    def __str__(self):
        return self.assettag + ' - ' + str(self.vendor) + ' - ' + str(self.product) + ' - ' + self.serial_number + ' - ' + str(self.configuration_owner) + ' - ' + str(self.integrator) + ' - ' + self.management_ipv4 + ' - ' + self.os_version