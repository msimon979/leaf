import copy

import numpy as np
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from matrix.helpers import transpose_matrix


class MatrixViewTests(APITestCase):
    """
    Test the view
    """
    def test_example_from_assignment(self):
        """
        Given: A request

        When: There is a valid payload

        Then: Returns list as a response
        """
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        url = reverse("matrix")
        data = {"matrix": matrix}

        response = self.client.post(url, data=data, format="json")
        assert response.status_code == status.HTTP_200_OK

        data = response.json()

        assert data["results"] == np.transpose(matrix).tolist()

    def test_missing_key_from_payload(self):
        """
        Given: A request

        When: It is missing the matrix key

        Then: An error is returned
        """
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        url = reverse("matrix")
        data = {"not_matrix": matrix}

        response = self.client.post(url, data=data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        assert response.json() == {"error": "Matrix key is required in the payload"}

    def test_matrix_is_not_a_list(self):
        """
        Given: A request

        When: The payload has the matrix as a str

        Then: An error is returned
        """
        matrix = "[[1,2,3],[4,5,6],[7,8,9]]"

        url = reverse("matrix")
        data = {"matrix": matrix}

        response = self.client.post(url, data=data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        assert response.json() == {"error": "Matrix is not a list"}


@pytest.mark.parametrize(
    "matrix",
    [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[-2, -8, 9, 42, 5], [-2, 11, 20, 4, 5]],
        [[1], [1]],
        [
            [100, 3123, 22, -1, -20, 60, 1, 90],
            [2, 1, 22, -18, -20, 60, 1, 3],
            [100, 2, 12, -1, -20, 60, 1, 7],
        ],
    ],
)
def test_transpose_matrix(matrix):
    """
    Running unit test on function. Using numpy to verify the result
    returned by my function matches theirs
    """
    np_matrix = np.transpose(matrix).tolist()
    assert transpose_matrix(matrix) == np_matrix
