from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer, CreateBookSerializer


class BookFilter(filters.FilterSet):
    author = filters.CharFilter(field_name="author", lookup_expr="icontains")
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    is_available = filters.BooleanFilter(field_name="is_available")

    class Meta:
        model = Book
        fields = ["author", "title", "is_available", "published_date"]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("id")
    serializer_class = BookSerializer
    filterset_class = BookFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    search_fields = ["title", "author"]
    ordering_fields = ["id", "title", "author", "published_date"]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method != "GET":
            return BookSerializer
        return CreateBookSerializer

    def create(self, request, *args, **kwargs):
        # if the request data is a list, set `many=True`
        is_many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
