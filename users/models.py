from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid


class userAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    id = models.UUIDField(primary_key=True default=uuid.uuid4, editable=False)
    
    phone = models.CharField(max_length=10)
    projects = models.ForeignKey("Project", on_delete=models.CASCADE, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = userAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    def getName(self):
        return self.name

    def getID(self):
        return self.id
        # return self.name.strip().lower().replace(" ", "_")

    def __str__(self):
        return self.email

    # def add_project(self, element):
    #     self.projects += "," + element if self.projects else element
    #     return self.save()

    # def get_projects(self):
    #     return self.projects.split(",") if self.projects else None

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # users = models.ManyToManyField(User, related_name="projects")
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    def add_user(self, element):
        self.users.add(element)

    def get_users(self):
        return self.users.all()

    def get_owner(self):
        return self.owner

    def get_description(self):
        return self.description

    def get_date_created(self):
        return self.date_created