from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class Role(models.TextChoices):
    ADMIN = 'ADMIN', 'Administrator'
    CUSTOMER = 'CUSTOMER', 'Customer'

class Pregunta(models.Model):
    pregunta_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.pregunta_text

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, )
    rol = models.CharField(max_length=50, choices=Role.choices, default=Role.CUSTOMER)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email']

    def __str__(self):
        return f'{self.username} {self.password} {self.email}'

# class UsuarioManager(BaseUserManager):
#     def create_user(self, email, name, password=None):
#         if not email:
#             raise ValueError('El usuario debe tener un correo electrónico')
#         user = self.model(
#             email=self.normalize_email(email),
#             name=name
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, name, password):
#         user = self.create_user(
#             email,
#             password=password,
#             name=name
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
#
#     def get_by_natural_key(self, username):
#         return self.get(nickname=username)

# class Usuario(AbstractBaseUser):
#
#     nickname = models.CharField(max_length=100, unique=True)
#     e_mail = models.CharField(max_length=100, unique=True)
#     rol = models.CharField(max_length=50, default='usuario')
#
#     objects = UsuarioManager()
#
#     USERNAME_FIELD = 'e_mail'
#
#
#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)
#         self.save()
#
#     def check_password(self, raw_password):
#         return check_password(raw_password, self.password)
#
#     def __str__(self):
#         return f'{self.e_mail} {self.password} {self.nickname} {self.rol}'

