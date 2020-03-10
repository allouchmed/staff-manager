from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """
    The main system user model.
    """

    city = models.ForeignKey('users.City', verbose_name=_('City'), related_name='people',
                             on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey('users.Department', verbose_name=_('Department'), related_name='employees',
                                   on_delete=models.SET_NULL, blank=True, null=True)
    organization = models.ForeignKey('users.Organization', verbose_name=_('Organization'),
                                     related_name='employees', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ('id',)

    def __str__(self):
        return self.email


class Country(models.Model):
    """
    Country model.
    """

    name = models.CharField(verbose_name=_('Country'), max_length=500)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        ordering = ('name',)

    def __str__(self):
        return self.name


class City(models.Model):
    """
    Country's city model.
    """

    country = models.ForeignKey('users.Country', verbose_name=_('Country'), related_name='cities',
                                on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_('City'), max_length=500)

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        unique_together = (('country', 'name'),)
        ordering = ('name',)

    def __str__(self):
        return self.name


class Organization(models.Model):
    """
    An organization model for uniting departments.
    """

    name = models.CharField(verbose_name=_('Organization'), max_length=500)

    class Meta:
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')
        ordering = ('name',)

    def __str__(self):
        return self.name


class Department(models.Model):
    """
    A department model of some organization.
    """

    organization = models.ForeignKey('users.Organization', verbose_name=_('Organization'), related_name='departments',
                                     on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_('Department'), max_length=500)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
        unique_together = (('organization', 'name'),)
        ordering = ('name',)

    def __str__(self):
        return self.name
