from django.db import models


class ListOfManufacturers(models.Model):
    name = models.CharField(verbose_name='Производитель', max_length=64,
                            unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    is_active = models.BooleanField(verbose_name='активно', default=True)

    def __str__(self):
        return self.name


class TypeProducts(models.Model):
    type_product = models.CharField(verbose_name='Тип продукта')
    description = models.TextField(verbose_name='Описание', blank=True)
    is_active = models.BooleanField(verbose_name='активно', default=True)


class Product(models.Model):
    manufacturer = models.ForeignKey(ListOfManufacturers, on_delete=models.CASCADE)
    type_product = models.ForeignKey(TypeProducts, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование компонента', max_length=128)
    image = models.ImageField(upload_to='accommodation_img', blank=True)
    short_desc = models.TextField(verbose_name='Краткое описание продукта',
                                  max_length=60, blank=True)
    description = models.TextField(verbose_name='Описание продукта', blank=True)
    availability = models.PositiveIntegerField(verbose_name='Количество на складе')
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2, default=0)
    is_active = models.BooleanField(verbose_name='активно', default=True)

    class Meta:
        unique_together = ('manufacturer', 'type_product', 'name')

    @staticmethod
    def get_items():
        return Product.objects.filter(is_active=True).order_by('manufacturer', 'type_product', 'name')

    def __str__(self):
        return f'{self.type_product.name} {self.name} {self.manufacturer.name}'
