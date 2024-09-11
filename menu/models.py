from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Menus'
        verbose_name = 'Menu'


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    order = models.IntegerField(default=0)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Menu Items'
        verbose_name = 'Menu Item'

    def __str__(self):
        return self.name