from django.utils.translation import gettext_lazy as _
from locations.models import County, City, PostalCode
from django.db import models


class Property(models.Model):
    property_number = models.IntegerField(
        _('Property Identification Number'), unique=True, blank=True, null=True,
        help_text=_('Identifier of each property'),
    )
    county = models.ForeignKey(
        County, _('County'), blank=True, null=True, on_delete=models.CASCADE,
        help_text=_('County this property belongs to'),
    )
    city = models.ForeignKey(
        City, _('City/Municipality'), blank=True, null=True, on_delete=models.CASCADE,
        help_text=_('City/Municipality this property belongs to'),
    )
    gnr = models.IntegerField(
        _('Cadastral Unit Number'), blank=True, null=True,
        help_text=_('Cadastral Unit Number of the property'),
    )
    bnr = models.IntegerField(
        _('Property Unit Number'), blank=True, null=True,
        help_text=_('Property Unit Number of the property'),
    )
    fnr = models.IntegerField(
        _('Lease Number'), blank=True, null=True,
        help_text=_('Lease Number of the property'),
    )
    snr = models.IntegerField(
        _('Unit Number'), blank=True, null=True,
        help_text=_('Unit Number of the property'),
    )
    bruksnavn = models.CharField(
        _('Subfarm Name'), max_length=100, blank=True, null=True,
        help_text=_('Name of the subfarm'),
    )
    antall_teiger = models.IntegerField(
        _('Number of plots'), blank=True, null=True,
        help_text=_('Number of available plots in this property'),
    )
    area = models.DecimalField(
        _('Property Area'), max_digits=15, decimal_places=4,
        blank=True, null=True, help_text=_('Property Area'),
    )
    arealkilde_nr = models.IntegerField(
        _('Source Number'), blank=True, null=True,
        help_text=_('Source Number'),
    )
    arealkilde_navn = models.CharField(
        _('Source Name'), max_length=50, blank=True, null=True,
        help_text=_('Name of the Source'),
    )
    natrings_kode = models.CharField(
        _('Industry Code'), max_length=50, blank=True, null=True,
        help_text=_('Industry Code Number'),
    )
    natrings_kode_navn = models.CharField(
        _('Industry Code Name'), max_length=50, blank=True, null=True,
        help_text=_('Indestry Code Name'),
    )
    tinglyst = models.BooleanField(
        _('Written Contract Exists'), blank=True, null=True,
        help_text=_('Availability of written contract'),
    )
    omsetnings_dato = models.IntegerField(
        _('Turnover Date'), blank=True, null=True,
        help_text=_('Date of property turnover'),
    )
    kjopesum = models.DecimalField(
        _('Purchase Price'), max_digits=20, decimal_places=2,
        blank=True, null=True, help_text=_('Purchase Price'),
    )
    omsetningstype_kode = models.CharField(
        _('Turnover Type Code'), max_length=50, blank=True, null=True,
        help_text=_('Turnover Type Code for property'),
    )
    omsetningstype_navn = models.CharField(
        _('Turnover Type Name'), max_length=200, blank=True, null=True,
        help_text=_('Turnover Type Name for property'),
    )
    sameie_teller = models.IntegerField(
        _('Number of co-ownership'), blank=True, null=True,
        help_text=_('Number of co-ownership for property'),
    )
    sameie_nevner = models.IntegerField(
        _('Maximum allowed co-ownership'), blank=True, null=True,
        help_text=_('Maximum co-ownership allowed for property'),
    )
    etablert_dato = models.IntegerField(
        _('Date of Establishment'), blank=True, null=True,
        help_text=_('Date of Establishment'),
    )
    etablert_aar = models.IntegerField(
        _('Year of Establishment'), blank=True, null=True,
        help_text=_('Year of Establishment'),
    )
    eiendomstype_kode = models.IntegerField(
        _('Property Type Code'), blank=True, null=True,
        help_text=_('Property Type Code'),
    )
    eiendomstype_navn = models.CharField(
        _('Property Type'), max_length=30, blank=True, null=True,
        help_text=_('Name of Property Type'),
    )
    bygning_paa_eiendom = models.CharField(
        _('Building on Property'), max_length=50, blank=True, null=True,
        help_text=_('Buildings on Property'),
    )
    bygning_paa_eiendom_navn = models.CharField(
        _('Building on Property Name'), max_length=200, blank=True, null=True,
        help_text=_('Name of Buildings on Property'),
    )
    antall_bygninger = models.IntegerField(
        _('Number of Buildings'), blank=True, null=True,
        help_text=_('Number of Buildings on Property'),
    )
    antall_addresser = models.IntegerField(
        _('Number of Addresses'), blank=True, null=True,
        help_text=_('Number of Addresses on Property'),
    )
    lkoord_sys_nr = models.IntegerField(
        _('Coordinate System Number'), blank=True, null=True,
        help_text=_('Coordinate System Number'),
    )
    lkoord_sys_navn = models.CharField(
        _('Coordinate System Name'), max_length=25, blank=True, null=True,
        help_text=_('Coordinate System Name'),
    )
    lkooelokx = models.DecimalField(
        _('UTM X coordinate'), max_digits=30, decimal_places=10,
        blank=True, null=True, help_text=_('Latitude'),
    )
    lkooeloky = models.DecimalField(
        _('UTM Y coordinate'), max_digits=30, decimal_places=10,
        blank=True, null=True, help_text=_('Longitude'),
    )
    
    def __str__(self):
        return self.bruksnavn
