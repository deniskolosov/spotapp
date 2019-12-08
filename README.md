Run in docker (assuming docker/docker-compose is installed):
```
git clone https://github.com/deniskolosov/spotapp.git
cd spotapp
docker-compose up
```
go to http://127.0.0.1:8000 

Run tests:
```
docker-compose run web ./manage.py test
```
