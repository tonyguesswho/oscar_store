from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class AbstractTimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, first_name, last_name, password):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        if password is None:
            raise TypeError('superuser must have a password')
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin, AbstractTimeStampedModel):
	email = models.EmailField(db_index = True, unique = True)

	first_name = models.CharField(max_length=255)

	last_name = models.CharField(max_length=255)

	is_active = models.BooleanField(default=True)

	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()


	def __str__(self):
		return self.email 

	def get_full_name(self):
		return self.firstname

	def get_short_name(self):
		return self.firstname

