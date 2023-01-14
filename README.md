## Тестовое задание. Поиск соответствующей формы по входящему шаблону

#### Порядок действий:
1. Клонируйте репозиторий:

`git clone`
2. Если у вас установлен Poetry:
	- Устанавливаем вирт. окружение и зависимости:
	
`poetry install`
`poetry shell`

 Если у вас нет Poetry, то создайте вирт. окружение и устновите зависимости через pip:
 
`python3 -m venv venv`
`pip install -r requirements.txt`

3. Запустите сервер:

`export FLASK_APP=main.py`
`flask run`

В базе данных `db.json` хранятся тествовые данные. Доступен эндпоинт `http://127.0.0.1:5000/get_form`, в URL которого можно передать параметры. Пример запроса:

`http://127.0.0.1:5000/get_form?user_name=Rick&user_email=rick@mai.ru`
	
Не стоит забывать, что при вводе значения поля телефона символ **+** нужно заменить на **%2B**, а **пробел** на **%20**.

Доступен тестовый скрипт для проверки работоспособности. Запустить его можно в консоли только при запущенном сервере:

`python test_requests/test_requests.py`
