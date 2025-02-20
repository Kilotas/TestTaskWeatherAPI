# TestTaskWeatherAPI
# Weather API

## Описание
Этот проект представляет собой REST API для получения погоды по городу и регистрации пользователей.

## Установка

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/Kilotas/TestTaskWeatherAPI.git
   cd TestTaskWeatherAPI
   ```

2. **Создайте виртуальное окружение и активируйте его**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для macOS/Linux
   venv\Scripts\activate  # Для Windows
   ```

3. **Установите зависимости**
   ```bash
   pip install -r requirements.txt
   ```

4. **Примените миграции**
   ```bash
   python manage.py migrate
   ```

5. **Запустите сервер**
   ```bash
   python manage.py runserver
   ```

## API Эндпоинты

### 1. Получение погоды
**GET /weather/{city}/**  
Возвращает информацию о погоде в указанном городе.

**Пример запроса:**
```http
GET /weather/London/
```
**Ответ:**
```json
{
    "city": "London",
    "temperature": "15°C",
    "description": "Cloudy"
}
```

### 2. Регистрация пользователя
**POST /register/**  
Позволяет зарегистрировать нового пользователя.

**Пример запроса:**
```json
{
    "username": "admin170",
    "password": "admin170",
    "role": "manager",
    "city": "Moscow"
}
```

**Ответ:**
```json
{
    "id": 1,
    "username": "admin170",
    "role": "manager",
    "city": "Moscow"
}
```

## Документация API
Доступна по адресам:
- Swagger UI: [`/swagger/`](http://127.0.0.1:8000/swagger/)
- Redoc: [`/redoc/`](http://127.0.0.1:8000/redoc/)
- Спецификация OpenAPI: [`/schema/`](http://127.0.0.1:8000/schema/)

## Авторизация
Некоторые эндпоинты требуют авторизации. Используйте JWT или другие механизмы аутентификации в зависимости от настроек проекта.

## Контакты
Если у вас есть вопросы, создайте issue в репозитории или свяжитесь со мной по email.
