from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.core.validators import MinValueValidator, MaxValueValidator


def check(user_di):
    if user_di.get('username') is None:
        raise TypeError('Должен быть задан логин')
    if user_di.get('email') is None:
        raise TypeError('Должен быть задан email')
    if user_di.get('password') is None:
        raise TypeError('Должен быть задан пароль')



class UserManager(BaseUserManager):
    def get_object_by_public_id(self, id):
        try:
            instance = self.get(id=id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404
        


    def create_user(self, user_di):
        check(user_di)
        user_di['email'] = self.normalize_email(user_di['email'])
        user = self.model(**user_di)
        user.set_password(user_di['password'])
        user.save(using=self._db)
    
    def create_superuser(self, user_di):
        user = self.create_user(user_di)
        user.set_password(user_di['password'])
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    email = models.CharField(verbose_name="email", max_length=40, unique=True)
    username = models.CharField(validators=[username_validator], verbose_name="логин", max_length=40, unique=True)
    last_name = models.CharField(verbose_name="фамилия", max_length=40, default="")
    first_name = models.CharField(verbose_name="имя", max_length=40, default="")
    registration_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.username} {self.first_name}"
    
    def get_short_name(self):
        return self.username

    
    @property
    def name(self):
        return f'{self.username}'


class DateTime(models.Model):
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Project(DateTime):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Создатель', related_name='projects', related_query_name="project")
    title = models.CharField(max_length=200, verbose_name='название проекта', unique=True)
    description = models.TextField(verbose_name='описание проекта', default='')
    count_cols = models.SmallIntegerField(verbose_name='сколько раз звонить до дозвона по умолчанию для проекта', default=1)
    file = models.FilePathField(blank=True, null=True, default='')
    is_over = models.BooleanField(verbose_name='дозвоны совершены', default=False)
    is_started = models.BooleanField(verbose_name='начат', default=False)
    date_over = models.DateTimeField(null=True)
    date_start = models.DateTimeField(null=True)


class Call(DateTime):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='calls', related_query_name='call')
    phone = models.PositiveIntegerField(default=10, validators=[MinValueValidator(79000000000), MaxValueValidator(79999999999)])
    count_cols = models.SmallIntegerField(default=1, verbose_name='сколько раз звонить, либо дозвон либо всего звонков')
    is_call = models.BooleanField(verbose_name='звонил', default=False)
    is_dial = models.BooleanField(verbose_name='дозвонился', default=False)
    num_call_now = models.SmallIntegerField(default=0, verbose_name='уже позвонили раз')

    def __str__(self):
        return str(self.phone)
 

class AudioFileModel(DateTime):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='audio', related_query_name='audio')
    file = models.FileField(blank=False, null=False)

