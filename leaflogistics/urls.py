from django.urls import path

from matrix.views import MatrixView

urlpatterns = [
    path("matrix/", MatrixView.as_view(), name="matrix"),
]
