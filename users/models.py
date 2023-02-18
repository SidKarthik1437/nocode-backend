from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import jsonfield
from django.utils import timezone


class userAccountManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("User must have an username")

        user = self.model(username=username, ** extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.create_user(
            username, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, blank=False, unique=True)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    name = models.CharField(max_length=255, blank=False)
    phone = models.CharField(max_length=10)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = userAccountManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['name', 'phone', 'email']

    def getName(self):
        return self.name

    # def getID(self):
    #     return self.id
    #     # return self.name.strip().lower().replace(" ", "_")

    def __str__(self):
        return self.username

    # def get_projects(self):
    #     return self.projects.split(",") if self.projects else None


class Project(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # users = models.ManyToManyField(User, related_name="projects")
    description = models.TextField(blank=True)
    date_created = timezone.now()

    def __str__(self):
        return self.name

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


# class Script(models.Model):
#     name = models.CharField(max_length=255, blank=False, unique=True)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     owner = owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     nodes = jsonfield.JSONField()
#     edges = jsonfield.JSONField()
#     data = jsonfield.JSONField()
#     date_created = timezone.now()

#     def __str__(self):
#         return self.name

#     def getNodes(self):
#         return self.nodes

#     def getEdges(self):
#         return self.edges

#     def getData(self):
#         return self.edges
