from django.contrib import admin

from content.models import Movie, Genre, Language, ProductionCompany


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """"""


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """"""


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    """"""


@admin.register(ProductionCompany)
class ProductionCompanyAdmin(admin.ModelAdmin):
    """"""
