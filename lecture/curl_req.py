POST request:
curl -X 'POST' 'http://127.0.0.1:8080/items/' 
-H 'accept: application/json' 
-H 'Content-Type: application/json' 
-d '{"name": "BestSale", "description": "The best of the best", "price": 9.99, "tax": 0.99}'

curl -X 'POST' 'http://127.0.0.1:8080/items/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "BestSale", "description": "The  est of the best", "price": 9.99, "tax": 0.99}'

curl -X 'POST' 'http://127.0.0.1:8080/tasks' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{name":"name_12","description":"desc test 12","status":true}'

PUT request:

curl -X 'PUT' 'http://127.0.0.1:8080/items/42' 
-H 'accept: application/json' 
-H 'Content-Type: application/json' 
-d '{"name": "NewName", "description": "New description of the object", price": 77.7, "tax": 10.01}'

curl -X 'PUT' 'http://127.0.0.1:8080/items/42' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "NewName", "description": "New description of the object", "price": 77.7, "tax": 10.01}'

curl -X 'PUT' 'http://127.0.0.1:8080/task/12' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"id":fg,"name":"name_12","description":"desc fgh test 12","status":false}'

DELETE request:

curl -X 'DELETE' 'http://127.0.0.1:8080/items/13' 
-H 'accept: application/json'

curl -X 'DELETE' 'http://127.0.0.1:8080/items/13' -H 'accept: application/json'

curl -X 'DELETE' 'http://127.0.0.1:8080/task/1' -H 'accept: application/json'