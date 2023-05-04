### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Murat-Kertiev/api_final_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source venv/Scripst/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Как посмотреть примеры запросов к api

После запуска локального сервера можно посмотреть примеры запросов по адресу:

```
http://127.0.0.1:8000/redoc/
```