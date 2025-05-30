from django.db import models


class Product(models.Model):
    CATEGORY_CHOICE = [
        ('VEG', "Овощи"),
        ('FRT', "Фрукты"),
        ('JUS', "Соки"),
        ('DFT', "Сухофрукты"),
        ('unknown', "Not stated"),
    ]
    prod_name = models.CharField(max_length=50)
    prod_old_price = models.FloatField(default=0)
    prod_new_price = models.FloatField(default=0)
    category = models.CharField(
        choices=CATEGORY_CHOICE,
        default='unknown',
        max_length=50
    )
    prod_image = models.ImageField(upload_to='avatars/')
    AVAILABILITY_CHOICE = [
        ('в наличии', "в наличии"),
        ('нет в наличии', "нет в наличии"),
    ]
    availability=models.CharField(
        choices=AVAILABILITY_CHOICE,
    )

    def __str__(self):
        return f"{self.prod_name.title()}"

    def discount(self):
        if self.prod_old_price == 0 or self.prod_new_price >= self.prod_old_price:
            return None
        discount1 = self.prod_old_price - self.prod_new_price
        discount2 = (discount1 / self.prod_old_price) * 100
        return round(discount2, 2)
# # Create your models here.
