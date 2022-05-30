## Описание:
API социальной сети YaTube.


## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

`git clone git@github.com:SimonKabb/api_final_yatube.git`

Cоздать и активировать виртуальное окружение:

`python3 -m venv мenv`
`source env/bin/activate`

Установить зависимости из файла requirements.txt:

`python3 -m pip install --upgrade pip`
`pip install -r requirements.txt`

Выполнить миграции:
`python3 manage.py migrate`

Запустить проект:
`python3 manage.py runserver`
## Аутентификация осуществляется по JWT-токену:
Создание пользователя:
POST `.../auth/users/`
```
{
    "username":"user"
    "password":"pass"
}
```
Получение токена:
POST `.../api/v1/jwt/create/`
```
{
    "username":"user"
    "password":"pass"
}
```
## Примеры запросов:
GET `.../api/v1/` - список стандартных эндпоинтов

