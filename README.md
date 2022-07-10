### Проект api_yamdb

```
Проект YaMDb собирает отзывы пользователей на произведения.
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
```

### Разработчики:



```
https://github.com/Lapanthera161
Пользователи и аутентификация
Произведения и категории
```

```
https://github.com/vladkataev
Отзывы и комментарии
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Lapanthera161/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

Документация с примерами запросов и ответов на них по адресу:

```
http://127.0.0.1:8000/redoc/
```
