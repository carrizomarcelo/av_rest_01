from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin



class UserManager(BaseUserManager):
    def _create_user(self, username, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
            )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, False, False, **extra_fields)
    
    def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Usuario', max_length = 255, unique = True)
    email = models.EmailField('Correo Electrónico', max_length = 255, unique = True)
    name = models.CharField('Nombre/s', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellido/s', max_length = 255, blank = True, null = True)
    image = models.ImageField('Imagen', upload_to='perfil/', max_length = 255, null = True, blank = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = True)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name']

    def natural_key(self):
        return self.username

    def __str__(self):
        """Visualizacion por defecto de un modelo.
        
        Retorna un formato de visualizacion por defecto de una instancia de un modelo, en este
        caso del modelo Usuario, este formato será visible cuando se desee vizualizar tanto en 
        navegador, consola, o en cualquier lugar donde sea llamado
        
        "Usuario {0}, con Nombre Completo: {1} {2}".format(self.username, self.last_name, self.name)

        """
        return f'{self.name} {self.last_name}'