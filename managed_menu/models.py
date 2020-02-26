from django.db import models

class Menu(models.Model):
    name = models.CharField(unique=True, max_length=100)
    active = models.BooleanField(default=True, db_index=True, verbose_name="Активность")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menus'

class MenuItem(models.Model):
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=500)
    parent_title = models.CharField(max_length=100, null=True, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("title","menu"),)
        verbose_name = 'menu item'
        verbose_name_plural = 'menu items'
