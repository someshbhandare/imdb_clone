import ast
import csv

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response

from content.models import Movie, ProductionCompany, Genre, Language
from content.serializers import MovieSerializer, CSVUploadSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  # Allow the client to override the page size
    max_page_size = 100


class MovieViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['release_date', 'original_language']
    ordering_fields = ['release_date', 'rating']
    pagination_class = CustomPagination

    @action(methods=["POST"], detail=False)
    def bulk_create(self, request: Request, *args, **kwargs):
        serializer = CSVUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        errors = []

        file = serializer.validated_data.get("file")
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for i, row in enumerate(reader):
            try:
                budget: int = int(float(row.get("budget")))
                homepage: str = row.get("homepage")
                original_language: str = row.get("original_language")
                original_title: str = row.get("original_title")
                overview: str = row.get("overview")
                release_date: str = row.get("release_date")
                revenue: int = int(float(row.get("revenue")))
                runtime: int = int(float(row.get("runtime")))
                release_status: str = row.get("status")
                title: str = row.get("title")
                rating: float = float(row.get("vote_average", ""))
                vote_count: int = int(float(row.get("vote_count")))
                production_company_id: int = int(row.get("production_company_id"))
                genre_id: int = int(row.get("genre_id"))
                languages: list[str] = ast.literal_eval(row.get("languages", []))

                production_company, _ = ProductionCompany.objects.get_or_create(id=production_company_id)
                genre, _ = Genre.objects.get_or_create(id=genre_id)
                language_objs = []
                for language in languages:
                    language_obj, _ = Language.objects.get_or_create(name=language)
                    language_objs.append(language_obj)

                movie = Movie.objects.create(
                    title=title,
                    overview=overview,
                    original_title=original_title,
                    original_language=original_language,
                    runtime_in_min=runtime,
                    status=release_status,
                    release_date=release_date,
                    production_company=production_company,
                    genre=genre,
                    vote_count=vote_count,
                    rating=rating,
                    budget=budget,
                    revenue=revenue,
                    homepage=homepage
                )
                movie.languages.add(*language_objs)
            except Exception as e:
                errors.append(f"Error processing row {i}: {str(e)}")

        return Response(data={"message": "Data Uploaded Successfully!", "errors": errors}, status=status.HTTP_200_OK)
