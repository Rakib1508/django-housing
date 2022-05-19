from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models import UniqueConstraint
from datetime import datetime, timedelta
from core.utils import GenderChoices
from django.db import models
from hashlib import blake2b
import random


class Account(AbstractUser):
    email = models.EmailField(
        _("email address"), unique=True,
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
    gender = models.CharField(
        _('gender'), max_length=1, blank=True, null=True,
        choices=GenderChoices.choices,
    )
    phone_number = PhoneNumberField(
        _('phone number'), unique=True, blank=True, null=True,
        help_text=_('Required if two factor authentication is enabled.'),
        error_messages={
            'unique': _('A user with that phone number already exists.'),
        },
    )
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
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
    # verification_code = models.CharField(
    #     _('one time verification code'), blank=True, null=True, max_length=6,
    #     help_text=_('temporary password with an expiration in 1 minutes'),
    # )
    # verification_code_expiry = models.DateTimeField(
    #     _('verification code expiry time'), blank=True, null=True,
    #     help_text=_('verification code expires after 1 minutes of creation'),
    # )
    # failed_verification_attempts = models.IntegerField(
    #     _('consecutive failed verification attempted'), default=0, blank=True,
    #     help_text=_('consecutive number of failed attempts for verification'),
    # )
    # failed_login_attempts = models.IntegerField(
    #     _('consecutive failed login attempts'), default=0, blank=True,
    #     help_text=_('consecutive number of failed attempts for logging in'),
    # )
    # disallow_login = models.DateTimeField(
    #     _('account frozen temporarily'), blank=True, null=True, default=None,
    #     help_text=_('account suspended for some time due to repeated failed login'),
    # )
    profile_picture = models.URLField(
        _('profile picture or avatar'), blank=True,
        help_text=_('profile picture will be used at most places alongside name'),
    )
    
    class Meta:
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
            models.Index(fields=['first_name']),
            models.Index(fields=['last_name']),
            models.Index(fields=['preferred_name']),
            models.Index(fields=['gender']),
            models.Index(fields=['phone_number']),
            models.Index(fields=['first_name', 'last_name']),
            models.Index(fields=['first_name', 'gender']),
            models.Index(fields=['last_name', 'gender']),
            models.Index(fields=['preferred_name', 'gender']),
            models.Index(fields=['first_name', 'last_name', 'gender']),
        ]
    
    def __str__(self):
        return self.username
    
    @property
    def set_preferred_name(self):
        # preferred name will be set to first name if blank
        if self.preferred_name is None:
            self.preferred_name = self.first_name
    
    @property
    def set_profile_picture(self):
        # default profile picture will be set according to gender
        if self.profile_picture is None:
            if self.gender == self.GenderChoices.FEMALE:
                # if female, then use the default female avatar
                self.profile_picture = 'accounts/default-profile-picture-female.png'
            else:
                # if male or not specified, then use the default male avatar
                self.profile_picture = 'accounts/default-profile-picture-male.png'
    
    def save(self, **kwargs):
        if self.is_verified and not self.phone_number:
            raise ValidationError('Cannot verify user without a phone number.')
        
        if self.two_factor_authentication and not self.is_verified:
            raise ValidationError('Cannnot enable two factor authentication without a verified phone number')
        
        super().save(**kwargs)
    
    # def generate_random_verification_code(self):
    #     code_number = random.randint(0, 999999)
    #     self.verification_code = str(code_number).zfill(6)
    #     self.verification_code_expiry = datetime.utcnow() + timedelta(minutes=1)
    #     self.save()
    #     return self.verification_code
    
    # def failed_verification_attempts_exceeded(self):
    #     self.verification_code = None
    #     self.failed_verification_attempts = 0
    #     self.verification_code_expiry = None
    #     self.save()
        
    #     message = 'Too many wrong attempts for verification! Please check your phone number verify phone number again!'
    #     return message
    
    # def freeze_user_account(self, action):
    #     self.disallow_login = datetime.utcnow() + timedelta(minutes=30)
    #     self.save()
    #     message = f'Too many wrong attempts for {action}! Please try again after 30 minutes'
    #     return message
    
    # def check_verification_code(self, **kwargs):
    #     response = {}
    #     if kwargs.get('user_code', None) == self.verification_code:
    #         self.failed_verification_attempts = 0
    #         self.verification_code = None
    #         self.verification_code_expiry = None
    #         if datetime.now() <= self.verification_code_expiry:
    #             self.is_verified = True
    #             print('Verification successful')
    #             response['success'] = True
    #             response['message'] = 'Verification successful'
    #         else:
    #             response['success'] = False
    #             response['message'] = 'Code expired. Try again'
    #         self.save()
    #     else:
    #         if self.failed_verification_attempts < 5:
    #             print('Verification failed. OTP mismatch')
    #             self.failed_verification_attempts = self.failed_verification_attempts + 1
    #             self.save()
    #             response['success'] = False
    #             response['message'] = 'Code does not match. Try again'
    #         else:
    #             response['success'] = False
    #             response['message'] = self.failed_verification_attempts_exceeded()
        
    #     return response
    
    # def verify_two_factor_authentication(self, **kwargs):
    #     response = {}
    #     if kwargs.get('user_code', None) == self.verification_code:
    #         self.failed_login_attempts = 0
    #         self.verification_code = None
    #         self.verification_code_expiry = None
    #         if datetime.now() <= self.verification_code_expiry:
    #             print('Verification successful')
    #             response['success'] = True
    #             response['message'] = 'Verification successful'
    #         else:
    #             response['success'] = False
    #             response['message'] = 'Code expired. Please try a new OTP'
    #         self.save()
    #     else:
    #         if self.failed_login_attempts < 5:
    #             print('Verification failed. OTP mismatch')
    #             self.failed_login_attempts = self.failed_login_attempts + 1
    #             self.save()
    #             response['success'] = False
    #             response['message'] = 'Code does not match. Try again'
    #         else:
    #             response['success'] = False
    #             response['message'] = self.freeze_user_account()
        
    #     return response
    
    # def on_login_failure(self):
    #     response = {'success': False, 'message': 'Login failed! Try again'}
    #     self.failed_login_attempts = self.failed_login_attempts + 1
    #     if self.failed_login_attempts > 5:
    #         response['message'] = self.freeze_user_account()
    #     self.save()
    
    # def on_login_success(self):
    #     self.failed_login_attempts = 0
    #     self.save()
    #     response = {'success': True, 'message': 'Login successful!'}
    #     return response
    
    # def on_log_out(self):
    #     self.last_login = datetime.utcnow()
    #     self.save()
    #     response = {'success': True, 'message': 'Logout successful!'}
    #     return response


class Developer(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    developer_nickname = models.CharField(max_length=100, blank=True)
    access_key = models.CharField(max_length=16, unique=True)
    developer_secret_key = models.CharField(max_length=32, unique=True)
    
    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['access_key', 'developer_secret_key'],
                name='unique_developer_access_credentials'
            ),
        ]
        indexes = [
            models.Index(fields=['access_key']),
            models.Index(fields=['developer_secret_key']),
        ]
    
    def __str__(self):
        return self.developer_nickname
    
    @property
    def set_developer_nickname(self):
        if not self.developer_nickname:
            self.developer_nickname = self.user.preferred_name
    
    def generate_random_developer_keys(self):
        current_time = datetime.utcnow()
        string = self.user.username + str(current_time)
        identifier = bytes(string, 'utf=8')
        self.access_key = blake2b(key=identifier, digest_size=8).hexdigest()
        self.developer_secret_key = blake2b(key=identifier, digest_size=16).hexdigest()
