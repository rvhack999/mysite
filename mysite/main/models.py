from django.db import models


class User(models.Model):
    """ Модель клиента """
    name = models.CharField(max_length=20, help_text='Имя клиента')
    email = models.EmailField(help_text='email', null=True, blank=True)
    phone = models.CharField(max_length=20, help_text='Телефон клиента')
    discount = models.FloatField(help_text='Скидка', blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Worker(models.Model):
    """ Модель Мастеров и сотрудников """
    name = models.CharField(max_length=50, help_text='Имя и фамилия сотрудника')
    phone = models.CharField(max_length=20, help_text='Телефон сотрудника')
    """ Нужно сделать список со специализациями мастера """
    salary = models.FloatField(help_text='Процентная ставка')

    class Meta:
        verbose_name = 'Сторудник'
        verbose_name_plural = 'Сторудники'

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=50, help_text='Заголовок')
    category_mod = models.CharField(max_length=100, help_text='Модель оборудования', null=True, blank=True)
    mod = models.TextField(help_text='Введите характер неисправности')
    client_id = models.ForeignKey(User, on_delete=models.CASCADE)
    master_id = models.ForeignKey(Worker, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_created=True)
    date_out = models.DateField(blank=True, null=True)
    price = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, help_text='Наименование товара')
    price = models.FloatField(help_text='Стоимость')
    about = models.TextField(help_text='Описание товара')


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
