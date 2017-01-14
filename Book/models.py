from django.db import models
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return '%s , %s , %s' %(self.name, self.address , self.city )

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    def __str__(self):
        return '%s , %s , %s' %(self.first_name, self.last_name , self.email )

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    photo = models.ImageField(upload_to='bookImages')
    def __str__(self):
        return '%s , %s' % (self.title, self.publisher)

# Create your models here.
