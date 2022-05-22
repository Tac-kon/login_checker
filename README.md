# Login_Checker

## 環境構築
下記のディレクトリを構成する。
```
root/
 ├ deployments/
 │ └ docker-compose
 │   ├ .env
 │   ├ docker-compose.yml
 │   ├ Dockerfile
 │   └ requirements.txt
 │
 ├ loginchecker # ★ここにアプリを追加
 │ ├ __init__.py
 │ ├ admin.py
 │ ├ apps.py
 │ ├ models.py
 │ ├ tests.py
 │ └ views.py
 │
 ├ project
 │ ├ __init__.py
 │ ├ asgi.py
 │ ├ urls.py
 │ └ wsgi.py
 │
 ├ .gitignore
 ├ manage.py
 └ README.md
```

1. プロジェクトファイルの作成
```
cd deployments/docker-compose
docker-compose run python3 django-admin startproject project .
```

2. アプリの作成
```
cd deployments/docker-compose 
docker-compose run python3 python manage.py startapp loginchecker
```

3. アプリ起動
```
cd deployments/docker-compose 
docker-compose up  
```

4. DBのマイグレーション
```
docker-compose exec python3 bash

# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
```

5. アプリ終了
```
cd deployments/docker-compose 
docker-compose down
```

## 参考
 - https://shimi-dai.com/django-env-on-docker/

 - https://qiita.com/LittleGreenMen/items/660c27669214da1c9613