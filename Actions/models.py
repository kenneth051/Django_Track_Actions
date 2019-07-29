from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import jwt
from datetime import datetime, timedelta
from TrackActions import settings
from Actions import constants

class UserManager(BaseUserManager):

    def create_user(self, email, username, password, **extra_fields):
        """Create and return a `User` with an email, username and password."""
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.username=username
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        """
        Create and return a `User` with superuser powers.
        Superuser powers means that this use is an admin that can do anything
        they want.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(email, username, password, **extra_fields)
        return user

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, blank=False)
    email=models.EmailField(max_length=255, unique=True,  blank=False)
    gender =models.CharField(max_length=255, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the console.
        """
        return self.email

    def token(self):
        credentials={
            "id":self.id,
            "username":self.username,
            "is_staff":self.is_staff,
            "is_active":self.is_active,
            "is_superuser":self.is_superuser,
            "email":self.email,
            "exp":datetime.now()+timedelta(days=1)
        }
        return jwt.encode(credentials,settings.SECRET_KEY).decode("utf-8")

class Todo(models.Model):
    user = models.OneToOneField("User", null=True, blank=True, on_delete=models.CASCADE)
    action = models.TextField(default="", editable=False)
    created_at = models.DateTimeField(default=datetime.now, editable=False)

class History(models.Model):
    table_name = models.CharField(max_length=255, blank=False, editable=False)
    user = models.ForeignKey("User", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    item_id = models.CharField(max_length=255, null=False, blank=False, editable=False)
    action = models.CharField(
        max_length=7, null=False, blank=False, choices=constants.ACTIONS, editable=False
    )
    body = models.TextField(default="", editable=False)

    class Meta:
        verbose_name_plural = "History model"

    def __str__(self):
        return self.action