from django.db import models

class Contacto(models.Model):
    nombre=models.CharField(max_length=100,null=False,blank=False,verbose_name='Nombre')
    apellido=models.CharField(max_length=100,null=False,blank=False,verbose_name='Apellido')
    email= models.EmailField(max_length=100,null=False,blank=False,verbose_name='Email')
    telefono=models.CharField(max_length=15,null=False,blank=False,unique=True,verbose_name='Telefono')
    fotografia=models.ImageField(upload_to='fotos',default='fotos/default.jpg',null=True,blank=True,verbose_name='Fotografia')
    

