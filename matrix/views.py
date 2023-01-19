from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from matrix.helpers import transpose_matrix


class MatrixView(APIView):
    http_method_names = ["post", "head", "options"]

    def post(self, request):
        matrix = request.data.get("matrix", None)

        if matrix is None:
            return JsonResponse(
                {"error": "Matrix key is required in the payload"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if isinstance(matrix, list) is False:
            return JsonResponse(
                {"error": "Matrix is not a list"}, status=status.HTTP_400_BAD_REQUEST
            )

        result = transpose_matrix(matrix)
        return JsonResponse({"results": result}, status=status.HTTP_200_OK)
