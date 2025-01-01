from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Base(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ProductionCompany(Base):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"ProductionCompany {self.id}. {self.name}"


class Genre(Base):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"Genre {self.id}. {self.name}"


class Language(Base):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"Language {self.id}. {self.name}"


class Movie(Base):
    title = models.CharField(max_length=255, db_index=True)
    overview = models.TextField(null=True, blank=True)
    original_title = models.CharField(max_length=255, null=True, blank=True)
    original_language = models.CharField(max_length=50, db_index=True)
    runtime_in_min = models.IntegerField(help_text="total runtime in minutes")
    status = models.CharField(db_index=True)
    release_date = models.DateField()

    production_company = models.ForeignKey(to=ProductionCompany, null=True, on_delete=models.SET_NULL, related_name="movies")
    genre = models.ForeignKey(to=Genre, null=True, on_delete=models.SET_NULL, related_name="movies")
    languages = models.ManyToManyField(to=Language, related_name="movies")

    vote_count = models.IntegerField()
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    budget = models.IntegerField()
    revenue = models.IntegerField()
    homepage = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id}. {self.title} - {self.rating}"