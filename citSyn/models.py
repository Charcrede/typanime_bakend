from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from backend import settings

class Citation(models.Model):
    perso_name = models.CharField(max_length=255)  # Nom du personnage
    anime_name = models.CharField(max_length=255)  # Nom de l'anime
    url = models.CharField(max_length=500)  # URL de l'image associée
    text = models.TextField()  # Texte de la citation

    def __str__(self):
        return f"{self.perso_name} from {self.anime_name}"


class Synopsis(models.Model):
    url = models.CharField(max_length=500)  # URL de l'image associée
    anime = models.CharField(max_length=255)  # Titre de l'anime
    texte = models.TextField()  # Texte du synopsis
    validate = models.BooleanField(default=False)  # Statut de validation

    def __str__(self):
        return self.anime




class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_admin = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin


class Challenge(models.Model):
    text = models.TextField()  # URL de l'image associée
    anime = models.CharField(max_length=255)  # Titre de l'anime
    texte = models.TextField()  # Texte du synopsis
    validate = models.BooleanField(default=False)  # Statut de validation

    def __str__(self):
        return self.anime

class Vitesse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.SET_NULL, null=True, blank=True)
    synopsis = models.ForeignKey(Synopsis, on_delete=models.SET_NULL, null=True, blank=True)
    citation = models.ForeignKey(Citation, on_delete=models.SET_NULL, null=True, blank=True)
    speed = models.IntegerField()

    def __str__(self):
        return f"Vitesse: {self.speed} by {self.user.pseudo}"