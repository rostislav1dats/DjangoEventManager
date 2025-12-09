from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    """
    Custom base model manager for user`s model where email is unique identifier insted of username 
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save user with email and password 
        """
        if not email:
            raise ValueError("Email обязателен")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save superuser with email and password
        """
        if password is None:
            raise TypeError('Superusers must have a password')
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self.create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user`s model for events manager.
    Use email instead username for authentification
    """
    username = None
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('First name', max_length=150, blank=True)
    last_name = models.CharField('last name', max_length=150, blank=True)

    # user permissions
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Metadata
    date_joined = models.DateTimeField('data joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    email_notifications = models.BooleanField('email notifications', default=True, help_text='Receive email notifications about events')

    # Set email as field for autentification
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # email already needed as USERNAME_FIELD

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['-date_joined']

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'.strip()
        return full_name or self.email
    
    
    # @property
    # def events_count(self):
    #     """
    #     Return count of created user`s events
    #     """
    #     return self.events.count()
    