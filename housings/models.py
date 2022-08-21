from django.utils.translation import gettext_lazy as _
from locations.models import County, City, PostalCode
from django.db import models


class Property(models.Model):
    property_number = models.DecimalField(
        _('Property Identification Number'), unique=True, blank=True, null=True,
        max_digits=15, decimal_places=0, help_text=_('Identifier of each property'),
    )
    county = models.ForeignKey(
        County, _('County'), blank=True, null=True, on_delete=models.CASCADE,
        help_text=_('County this property belongs to'),
    )
    city = models.ForeignKey(
        City, _('City/Municipality'), blank=True, null=True, on_delete=models.CASCADE,
        help_text=_('City/Municipality this property belongs to'),
    )
    cadastral_unit_number = models.DecimalField(
        _('Cadastral Unit Number'), max_digits=10, decimal_places=0,
        blank=True, null=True, help_text=_('Cadastral Unit Number of the property'),
    )
    property_unit_number = models.DecimalField(
        _('Property Unit Number'), max_digits=10, decimal_places=0,
        blank=True, null=True, help_text=_('Property Unit Number of the property'),
    )
    lease_number = models.DecimalField(
        _('Lease Number'), max_digits=10, decimal_places=0,
        blank=True, null=True, help_text=_('Lease Number of the property'),
    )
    unit_number = models.DecimalField(
        _('Unit Number'), max_digits=10, decimal_places=0,
        blank=True, null=True, help_text=_('Unit Number of the property'),
    )
    subfarm_name = models.CharField(
        _('Subfarm Name'), max_length=100, blank=True, null=True,
        help_text=_('Name of the subfarm'),
    )
    number_of_plots = models.DecimalField(
        _('Number of plots'), max_digits=10, decimal_places=0,
        blank=True, null=True, help_text=_('Number of available plots in this property'),
    )
    property_area = models.DecimalField(
        _('Property Area'), max_digits=15, decimal_places=4,
        blank=True, null=True, help_text=_('Property Area'),
    )
    source_number = models.DecimalField(
        _('Source Number'), max_digits=15, decimal_places=0,
        blank=True, null=True, help_text=_('Source Number'),
    )
    source_name = models.CharField(
        _('Source Name'), max_length=50, blank=True, null=True,
        help_text=_('Name of the Source'),
    )
    industry_group_code = models.CharField(
        _('Industry Code'), max_length=50, blank=True, null=True,
        help_text=_('Industry Code Number'),
    )
    industry_group_name = models.CharField(
        _('Industry Code Name'), max_length=50, blank=True, null=True,
        help_text=_('Indestry Code Name'),
    )
    written_contract_exists = models.BooleanField(
        _('Written Contract Exists'), blank=True, null=True,
        help_text=_('Availability of written contract'),
    )
    turnover_date = models.DecimalField(
        _('Turnover Date'), max_digits=10, decimal_places=0,
        blank=True, null=True, help_text=_('Date of property turnover'),
    )
    purchase_price = models.DecimalField(
        _('Purchase Price'), max_digits=20, decimal_places=2,
        blank=True, null=True, help_text=_('Purchase Price'),
    )
    turnover_type_code = models.CharField(
        _('Turnover Type Code'), max_length=50, blank=True, null=True,
        help_text=_('Turnover Type Code for property'),
    )
    turnover_type_code = models.CharField(
        _('Turnover Type Name'), max_length=200, blank=True, null=True,
        help_text=_('Turnover Type Name for property'),
    )
    number_of_coownership = models.DecimalField(
        _('Number of co-ownership'), max_digits=10, decimal_places=0,
        blank=True, null=True, help_text=_('Number of co-ownership for property'),
    )
    maximum_allowed_coownership = models.DecimalField(
        _('Maximum allowed co-ownership'), max_digits=10, decimal_places=0,
        blank=True, null=True, help_text=_('Maximum co-ownership allowed for property'),
    )
    establish_date = models.DecimalField(
        _('Date of Establishment'), max_digits=10, decimal_places=0,
        blank=True, null=True, help_text=_('Date of Establishment'),
    )
    establish_year = models.DecimalField(
        _('Year of Establishment'), max_digits=10, decimal_places=0,
        blank=True, null=True, help_text=_('Year of Establishment'),
    )
    property_type_code = models.DecimalField(
        _('Property Type Code'), max_digits=10, decimal_places=0,
        blank=True, null=True, help_text=_('Property Type Code'),
    )
    property_type_name = models.CharField(
        _('Property Type'), max_length=30, blank=True, null=True,
        help_text=_('Name of Property Type'),
    )
    building_on_property = models.CharField(
        _('Building on Property'), max_length=50, blank=True, null=True,
        help_text=_('Buildings on Property'),
    )
    building_name_on_property = models.CharField(
        _('Building Name on Property'), max_length=200, blank=True, null=True,
        help_text=_('Name of Buildings on Property'),
    )
    number_of_buildings = models.DecimalField(
        _('Number of Buildings'), max_digits=10, decimal_places=0,
        blank=True, null=True, help_text=_('Number of Buildings on Property'),
    )
    number_of_addresses = models.DecimalField(
        _('Number of Addresses'), max_digits=10, decimal_places=0,
        blank=True, null=True, help_text=_('Number of Addresses on Property'),
    )
    coordinate_system_number = models.DecimalField(
        _('Coordinate System Number'), max_digits=10, decimal_places=0,
        blank=True, null=True, help_text=_('Coordinate System Number'),
    )
    coordinate_system_name = models.CharField(
        _('Coordinate System Name'), max_length=25, blank=True, null=True,
        help_text=_('Coordinate System Name'),
    )
    latitude = models.DecimalField(
        _('UTM X coordinate'), max_digits=30, decimal_places=10,
        blank=True, null=True, help_text=_('Latitude'),
    )
    longitude = models.DecimalField(
        _('UTM Y coordinate'), max_digits=30, decimal_places=10,
        blank=True, null=True, help_text=_('Longitude'),
    )
    
    def __str__(self):
        return self.subfarm_name
