from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models import  UniqueConstraint
# Create your models here.

def tri_ne_bolee(value):
    if value>110 or value <0:
        raise ValidationError(
            _(f"{value} NOT CORRET"),
            params={"value":value},
        )

class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12, null=True, blank=True, unique=True)
    city = models.CharField(max_length=50, editable=False, default='')
    gender_choise=[
        ("1", 'Мужской'),
        ("0", 'Женский'),
        ("None", "Не указан")]
    gender=models.CharField(max_length=50,choices=gender_choise,default="None")
    age = models.IntegerField(validators=[tri_ne_bolee], default=18)
    avatar=models.ImageField(upload_to='avatars/',blank=True, null=True)

    def __str__(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price=models.FloatField(default=0)
    discount=models.BooleanField(default=False)
    price_discount=models.FloatField(default=0)
    type_choises=[
        ("1","Алкоголь"),
        ("0","Еда"),
        ("2", "Not Stated"),
    ]
    type =models.CharField(choices=type_choises, max_length=20,default=0)
    def __str__(self):
        return f"{self.name.title()} "

class Cart(models.Model):
    user_id=models.ForeignKey("User",on_delete=models.CASCADE)
    product_id = models.ForeignKey("Product",on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user_id} - {self.product_id}  "

    class Meta:
        constraints=[
        UniqueConstraint(fields =['user_id', 'product_id'],name='user_product')
        ]




