### Generate token usong drf
$ ./manage.py createsuperuser

$ ./manage.py drf_create_token  <user>

### copy the generated token to the authorization header

└──╼ $http http://127.0.0.1:8000/api/hello/ "Authorization: Token 1577d1e126e24f5713a2f5f53572c05e6eba4981"
{
    "message": "Response one"
}


