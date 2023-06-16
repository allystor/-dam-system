from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class TipoBacia(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Engenheiro(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    crea = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    rua = models.CharField(max_length=50)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=8)


class Bacia(models.Model):
    tipoBacia = models.ForeignKey(TipoBacia, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    profundidade = models.FloatField(null=False, blank=True)
    capacidade = models.FloatField(null=False, blank=True)
    largura = models.FloatField(null=False, blank=True)
    comprimento = models.FloatField(null=False, blank=True)
    engenheiro = models.ForeignKey(Engenheiro, on_delete=models.CASCADE)


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Usuários devem ter um endereço de e-mail válido.')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserAutentication(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(verbose_name='E-mail', unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def str(self):
        return self.email

    @property
    def is_anonymous(self):
        return not self.is_authenticated

    @property
    def is_authenticated(self):
        return self.is_active

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admi