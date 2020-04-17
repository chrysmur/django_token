### Generate token usong drf
$ ./manage.py createsuperuser

$ ./manage.py drf_create_token  <user> 
- for testing purposes

### Request token from the api
$ http http://127.0.0.1:8000/api/token username=sost password=sost
{
    "token": "1577d1e126e24f5713a2f5f53572c05e6eb45w81"
}



### copy the generated token to the authorization header

└──╼ $http http://127.0.0.1:8000/api/hello/ "Authorization: Token 1577d1e126e24f5713a2f5f53572c05e6eb45w81"
{
    "message": "Response one"
}


