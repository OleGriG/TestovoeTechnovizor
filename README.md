API для Yatube
Python Django Pytest Postman

Python Django Pytest Postman

Описание
Тестовое задание в компанию Техновизор. Веб-приложение для заказа копроративной еды.

Функционал
Заказ еды, просмотр отчета о заказе, просмотр истории заказов
Установка
Клонировать репозиторий:

git clone https://github.com/OleGriG/TestovoeTechnovizor.git

Установить виртуальное окружение для проекта:

python -m venv venv
Активировать виртуальное окружение для проекта:

# для OS Lunix и MacOS
source venv/bin/activate

# для OS Windows
source venv/Scripts/activate
Установить зависимости:

python3 -m pip install --upgrade pip
pip install -r requirements.txt
Выполнить миграции на уровне проекта:


python3 manage.py makemigrations
python3 manage.py migrate
Запустить проект:

python manage.py runserver