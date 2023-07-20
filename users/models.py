from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True, editable=False)
    username = models.CharField(_("Username"), max_length=255, unique= True)
    first_name = models.CharField(_("First Name"), max_length=250)
    last_name = models.CharField(_("last Name"), max_length=250)
    email = models.EmailField(_("Email Address"), max_length=254, unique= True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now())

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_short_name(self):
        return self.username

