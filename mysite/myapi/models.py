from django.db import models

class Library(models.Model):
    book_name = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    no_of_pages = models.DecimalField(max_digits=3, decimal_places=0, default=0)

    def __str__(self):
        return self.book_name