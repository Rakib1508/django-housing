from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from django.db import models
import random


class Account(AbstractUser):
    email = models.EmailField(
        _("email address"),
        error_messages = {
            'required': _('Must provide a valid email address.'),
            'invalid': _('Must provide a valid email address.'),
        },
    )
    first_name = models.CharField(
        _('first name'), max_length=150,
        error_messages = {
            'required': _('Must provide a first name.'),
            'max_length': _('First name can be at most 150 characters.'),
        },
    )
    last_name = models.CharField(
        _('last name'), max_length=150,
        error_messages = {
            'required': _('Must provide a last name.'),
            'max_length': _('Last name can be at most 150 characters.'),
        }
    )
    preferred_name = models.CharField(
        _('preferred name'), max_length=150, blank=True,
        help_text=_(
            'Name to be used for calling you by. '
            'If empty, first name will be used by default.'
        ),
    )
    phone_number = PhoneNumberField(
        _('phone number'), unique=True, blank=True, null=True,
        help_text=_('Required if two factor authentication is enabled.'),
        error_messages={
            'unique': _('A user with that phone number already exists.'),
        },
    )
    is_verified = models.BooleanField(
        _('phone number verification status'),
        default=False,
        help_text=_('Designates whether a user can enable two factor authentication.'),
    )
    two_factor_authentication = models.BooleanField(
        _('OTP-based authentication'),
        default=False,
        help_text=_('Designates whether a user uses two factor authentication.'),
    )
    allow_log_in = models.BooleanField(_('two factor authentication status'), default=False)
    verification_code = models.CharField(
        _('one time verification code'),
        blank=True, null=True, max_length=6,
    )
    verification_code_expiry = models.DateTimeField(
        _('verification code expiry time'), blank=True, null=True,
    )
    verification_attempts = models.IntegerField(_('verification attempted'), default=0)
    
    def __str__(self):
        return self.username
    
    @property
    def set_preferred_name(self):
        # preferred name will be set to first name if blank
        if self.preferred_name is None:
            self.preferred_name = self.first_name
    
    def save(self, **kwargs):
        if self.is_verified and not self.phone_number:
            raise ValidationError('Cannot verify user without a phone number.')
        
        if self.two_factor_authentication and not self.is_verified:
            raise ValidationError('Cannnot enable two factor authentication without a verified phone number')
        
        super().save(**kwargs)
    
    def generate_random_verification_code(self):
        code_number = random.randint(0, 999999)
        self.verification_code = str(code_number).zfill(6)
        self.verification_code_expiry = datetime.now() + timedelta(minutes=1)
        self.save()
    
    def verification_attempts_exceeded(self):
        self.verification_code = None
        self.verification_attempts = 0
        self.verification_code_expiry = None
        self.save()
    
    def check_verification_code(self, **kwargs):
        if kwargs.get('user_code', None) == self.verification_code:
            self.verification_attempts = 0
            self.verification_code = None
            self.verification_code_expiry = None
            if datetime.now() <= self.verification_code_expiry:
                self.is_verified = True
                print('Verification successful')
            self.save()
        else:
            if self.verification_attempts <= 5:
                print('Verification failed. OTP mismatch')
                self.verification_attempts = self.verification_attempts + 1
                self.save()
            else:
                self.verification_attempts_exceeded()
                raise ValidationError(
                    'Too many wrong attempts for verification! '
                    'Please verify phone number again!'
                )
    
    def verify_two_factor_authentication(self, **kwargs):
        if kwargs.get('user_code', None) == self.verification_code:
            self.verification_attempts = 0
            self.verification_code = None
            self.verification_code_expiry = None
            if datetime.now() <= self.verification_code_expiry:
                self.allow_log_in = True
                print('Verification successful')
            self.save()
        else:
            if self.verification_attempts <= 5:
                print('Verification failed. OTP mismatch')
                self.verification_attempts = self.verification_attempts + 1
                self.save()
            else:
                self.verification_attempts_exceeded()
                raise ValidationError(
                    'Too many wrong attempts for verification! '
                    'Please verify phone number again!'
                )
    
    def on_log_out(self):
        # add what values to update when user logs out
        pass
