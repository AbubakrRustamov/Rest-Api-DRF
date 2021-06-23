from django.db import models

# Create your models here.


Grade = [

    ('excellent', 1),
    ('average', 0),
    ('bad', -1),
]
StudentGrade = [

    ('excellent', 100),
    ('average', 70),
    ('bad', 50),
]
#dataflair

class DRFPost(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    uploaded = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices=Grade, default='average',  max_length=50)

    class Meta:
        ordering = ['uploaded']

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='picture/', blank=True)

    class Meta:
        ordering = ['add_date']
        def __str__(self):
            return self.title

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    rating = models.CharField(choices=StudentGrade, default='average', max_length=50)
    image = models.ImageField(upload_to='picture/', blank=True)
    add_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['add_date']
        def __str__(self):
            return self.name