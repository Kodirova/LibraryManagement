from django.db import models

# Create your models here.
from django.db.models import Q
from django.urls import reverse


class Student(models.Model):
    full_name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone = models.IntegerField()

    def __str__(self):
        return self.full_name


    def get_absolute_url(self):
        return reverse('student_list', kwargs={'pk': self.pk})


class Book(models.Model):
   # ISBN =  models.IntegerField()
    name = models.CharField(max_length=256)
    full_name_of_author = models.CharField(max_length=256)
    status = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('book_list', kwargs={'pk': self.pk})




class PurchasedBook(models.Model):
    student = models.ForeignKey(to = 'Student', on_delete=models.CASCADE)
    book = models.ForeignKey(to='Book', on_delete=models.CASCADE)

    purchased_date = models.DateField(auto_now=True)
    delivered_date = models.DateField(auto_now_add=False, blank=True, null=True)
    # objects = PurchasedBookManager()

    def get_absolute_url(self):
        return reverse('order-list', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.student}'




# class OrderBooks(models.Model):
#     id = models.IntegerField(primary_key=True)
#     book_id = models.ManyToManyField(Book)
#     order_id = models.ManyToManyField(Order)
#     quantity = models.IntegerField(default=1)
