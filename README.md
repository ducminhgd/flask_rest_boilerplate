# RESTFul API Boilerplate

## Database

Create database

```shell
flask run db init --multidb
flask run db migrate
flask run db upgrade
```

## Sample nginx

```
upstream flask {
    server 127.0.0.1:5000;
    keepalive 1;
}

server {
    listen 80;
    listen [::]:80;
    server_name local-flask.teko.vn;

    allow all;
    access_log /var/log/nginx/local-flask.teko.vn.access.log;
    error_log /var/log/nginx/local-flask.teko.vn.error.log;

    location / {
        proxy_pass  http://flask;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
    }
}
```