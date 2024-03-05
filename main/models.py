from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, ValidationError
from .validators import ImageFileValidator
import qr_qode
from io import BytesIO
from django.core.files import File


class User(AbstractUser):
    full_name = models.CharField(max_length=55, db_index=True, verbose_name='toliq ismi')
    address = models.CharField(max_length=75, null=True, blank=True, verbose_name='manzili')
    phone_number = models.CharField(max_length=13, unique=True, verbose_name='telefon raqami', validators=[
        RegexValidator(
            regex='^[/+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid number',
        )])

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'User'


class Deliver(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='deliver_photos/')
    gender = models.CharField(choices=(
        (1, 'Male'),
        (2, 'Female'),
    ))
    age = models.IntegerField(default=18)








class Delivery(models.Model):
    type = models.CharField(choices=(
        (1, 'On_foot'),
        (2, 'Cycle'),
        (3, 'Scuter'),
        (4, 'Motorbike'),
        (5, 'Car'),
    ))
    delivery_time = models.IntegerField(default=1)
    deliver = models.ForeignKey(to='Deliver', on_delete=models.CASCADE)








class Customer(models.Model):
    food = models.ForeignKey(to='Food', on_delete=models.CASCADE, verbose_name='Taomi')
    full_name = models.CharField(max_length=255, verbose_name='toliq ism')
    age = models.IntegerField(default=18, verbose_name='yosh')
    gender = models.IntegerField(default=1, verbose_name='jinsi',  choices=(
        (1, 'Male'),
        (2, 'Female'),
    ))
    address = models.CharField(max_length=255, verbose_name='joylashuv')
    photo = models.ImageField(upload_to='photos/', verbose_name='rasmi', validators=[ImageFileValidator()])
    phone_number = models.CharField(max_length=13, verbose_name='telefon raqamia')
    extra_phone_number = models.CharField(max_length=13, null=True, blank=True, verbose_name='ekstra_telefon_raqam')
    bio = models.TextField(verbose_name="ma'lumotlari")
    time_ordered = models.DateTimeField
    payment_status = models.IntegerField(default=1, verbose_name='tolov statusi', choices=(
        (1, 'unpaid'),
        (2, 'part_paid'),
        (3, 'paid'),
    ))
    payment_type = models.CharField(choices=(
        (1, 'Card'),
        (2, 'Cash'),
        (3, 'Unpaid'),
    ))

class Chef(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    gender = models.CharField(choices=(
        (1, 'Male'),
        (2, 'Female'),
    ))
    qr_qode = models.ImageField(upload_to='qr_qode/', blank=True, null=True)




    def save(self, *args, **kwargs):
        qr = qr_qode.QRcode(
            version=1,
            error_correction=qr_qode.constans.ERROR_CORRECT_L,
            box_size=5,
            border=3,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.payment_type.order}")
        qr.make(fit=True)
        img = qr_make_image(fill_colors="black", back_color="white")


        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)
        super().save(*args, **kwargs)

        class Meta:
            verbose_name = 'Comment'
            verbose_name_plural = 'Comments'


class Place(models.Model):
    number = models.IntegerField()
    type = models.CharField(choices=(
        (1, 'Simple'),
        (2, 'Royal'),
        (3, 'Comfort'),
    ))



class Food(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(choices=(
        (1, 'Drink'),
        (2, 'Food')
    ))
    cost = models.IntegerField()
    expration_date = models.IntegerField(default=1)


class Cassa(models.Model):
    cashier = models.CharField(max_length=50)
    payment_type = models.CharField(choices=(
        (1, 'Card'),
        (2, 'Naqd'),

    ))
    payment = models.CharField(choices=(
        (1, 'Paid'),
        (2, 'Unpaid'),
    ))


class Employee(models.Model):
    user = models.OneToOneField(to='User', on_delete=models.CASCADE, verbose_name='foydalanuvchi')
    status = models.IntegerField(default=5, verbose_name='statusi',choices=(
        (1, 'manager'),
        (2, 'asissant'),
        (3, 'deliver'),
        (4, 'cooker'),
        (5, 'cashier'),

    ))
    salary = models.PositiveIntegerField(verbose_name='ish haqi')
    work_time = models.CharField(max_length=255, verbose_name='ish vaqti')
    bio = models.CharField(max_length=255, verbose_name='biosi')
    age = models.IntegerField(verbose_name='yosh')
    departament = models.ForeignKey(to='Departament', on_delete=models.CASCADE, verbose_name='departamenti')


    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'