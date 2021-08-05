from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ShoppingList(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,  null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
