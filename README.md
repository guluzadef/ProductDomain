
<div align="center">
  <h1>Build project</h1>
</div>

- **Clone**: `git clone https://github.com/guluzadef/ProductDomain`
- **After Clone**: `cd ProductDomain`

- **Build docker**: `docker-compose up --build -d`

- **Restore Database**: `docker exec -i my_mongodb /usr/bin/mongorestore --username admin --password adminpass --authenticationDatabase admin --nsInclude="mydatabase.*" --archive < mongodb.dump`


- **API url for all count** : `localhost:8000/product` **Response** `All sub category product counts`
- **API url for all product** : `localhost:8000/all` **Response** `Show all product`

- **API url with parameters** : **exm**: `localhost:8000/product?min_price=1&max_price=35`


