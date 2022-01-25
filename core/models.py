from django.db import models

# Create your models here.


class Categoria(models.Model):
    name  = models.CharField(max_length=200, verbose_name="Nombre de la Categoria", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        # Ordena de mas nuevo a mas antiguo
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Nivel(models.Model):
    name  = models.CharField(max_length=200, verbose_name="Nombre", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Nivel de Escalacion"
        verbose_name_plural = "Niveles de Escalación"
        # Ordena de mas nuevo a mas antiguo
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Empresa(models.Model):
    name  = models.CharField(max_length=200, verbose_name="Nombre", blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="get_categoria",
                                verbose_name="Categoria")
    imagen = models.ImageField(verbose_name='Adjunta una imagen', upload_to= 'empresa', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        # Ordena de mas nuevo a mas antiguo
        ordering = ["-created"]

    def __str__(self):
        return self.name


class TablaEscalacion(models.Model):
    name  = models.CharField(max_length=200, verbose_name="Nombre", blank=True, null=True)
    last_name = models.CharField(max_length=200, verbose_name="Apellido", blank=True, null=True)
    mail = models.EmailField(max_length=200, verbose_name="Correo", blank=True, null=True)
    phone = models.CharField(max_length=200, verbose_name="Teléfono", blank=True, null=True)

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="get_empresa",
                                verbose_name="Empresa")
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, related_name="get_nivel",
                                verbose_name="Nivel de Escalación o Cargo")

    excel = models.FileField(max_length=200, verbose_name="Adjunta Archivo Excel", upload_to= 'documents', blank=True, null=True)

    order = models.IntegerField(verbose_name="Orden", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Tabla de Escalación"
        verbose_name_plural = "Tablas de Escalaciones"
        # Ordena de mas nuevo a mas antiguo
        ordering = ["order"]

    def __str__(self):
        return self.name