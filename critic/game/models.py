from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=80)
    director = models.CharField(max_length=100)
    year = models.CharField(max_length=5)
    description = models.TextField()

    def __str__(self):
        return self.title


class Review(models.Model):
    review = models.TextField()
    reviewer = models.CharField(max_length=50)
    movie_name = models.ForeignKey(Movie)

    def __str__(self):
        return self.reviewer


class Similar(models.Model):
    movie = models.ForeignKey(Movie)
    sim1 = models.CharField(max_length=80)
    sim2 = models.CharField(max_length=80)
    sim3 = models.CharField(max_length=80)
    sim4 = models.CharField(max_length=80)
    sim5 = models.CharField(max_length=80)