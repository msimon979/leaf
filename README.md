# leaf

## Docker setup
If docker is installed on your machine you can build the container with `make init`

While the container is up run `make tests` to run the tests

## Local setup
In a virtual env run `pip install -r requirements.txt`

Bring up Django `python manage.py runserver 0.0.0.0:8000`

Run tests with `pytest matrix/tests.py`

## Example payloads
```
curl --location --request POST 'http://0.0.0.0:8000/matrix/' \
--header 'Content-Type: application/json' \
--data-raw '{
     "matrix": [[1,2,3],[4,5,6],[7,8,9]]
}'

# response
{"results": [[1, 4, 7], [2, 5, 8], [3, 6, 9]]}


curl --location --request POST 'http://0.0.0.0:8000/matrix/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "matrix": [[-2, -8, 9, 42, 5], [-2, 11, 20, 4, 5]]
}'

# response
{"results": [[-2, -2], [-8, 11], [9, 20], [42, 4], [5, 5]]}
```

## Notes
The api requires certain imports to run but no imports were used for the actual logic piece in helpers.transpose_matrix.

Numpy is imported in the test file to verify helpers.transpose_matrix is returning the correct data.

Even though nothing is saved to a database still using POST since it is passing a payload.
