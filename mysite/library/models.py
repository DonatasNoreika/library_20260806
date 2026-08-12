from django.db import models
import uuid

# Create your models here.
class Genre(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

    # class Meta:
    #     verbose_name = "Žanras"
    #     verbose_name_plural = "Žanrai"


class Author(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    description = models.TextField(default="")

    def display_books(self):
        return ", ".join(book.title for book in self.books.all())

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField()
    summary = models.TextField()
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField(to="Genre")
    author = models.ForeignKey(to="Author",
                               on_delete=models.SET_NULL,
                               null=True, blank=True,
                               related_name="books")

    def display_genre(self):
        return ", ".join(genre.name for genre in self.genre.all())

    # display_genre.short_description = "Žanrai"

    def __str__(self):
        return self.title

class BookInstance(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    book = models.ForeignKey(to="Book", on_delete=models.CASCADE)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('d', 'Administered'),
        ('t', 'Taken'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(choices=LOAN_STATUS, default='d')

    def __str__(self):
        return str(self.uuid)