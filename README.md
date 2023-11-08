# Тестовое заданние на создание древовидного меню
#### 1) Меню реализовано через template tag 
#### 2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
#### 3) Хранится в БД.
#### 4) Редактируется в стандартной админке Django
#### 5) Активный пункт меню определяется исходя из URL текущей страницы
#### 6) Меню на одной странице может быть несколько. Они определяются по названию.
#### 7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
#### 8)На отрисовку каждого меню требуется ровно 1 запрос к БД
### Стек технологии:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/) [![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/) [![SQLlite](https://img.shields.io/badge/-SQLlite-464646?style=flat-square&logo=SQLlite)](https://www.sqlite.org/)

## Установка
### Клонировать репозиторий: https://github.com/VRN-lab/test_item

### Cоздать и активировать виртуальное окружение:
- python -m venv venv
- source venv/Scripts/activate
- python -m pip install --upgrade pip

### Установить зависимости из файла requirements.txt: 
- pip install -r requirements.txt

### Выполнить миграции:
- python manage.py migrate

### Запустить проект:
- python manage.py runserver

### Вход в админку:
- Логин: admin
- Пароль: admin

## Автор:
# Назипов Виктор