Конечно! Вот профессиональный README.md для этого проекта:

```markdown
# LearnAuth - Система аутентификации и управления правами на Django

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.0-green.svg)
![DRF](https://img.shields.io/badge/Django_REST_Framework-3.12-red.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-purple.svg)

Учебный проект, реализующий систему аутентификации и разграничения прав доступа с использованием Django и Django REST Framework.

## 🚀 Функциональность

### 🔐 Система аутентификации
- **JWT-аутентификация** с использованием Simple JWT
- Регистрация новых пользователей
- Вход в систему и получение токенов
- Обновление access-токенов
- Верификация токенов

### 👥 Управление пользователями и правами
- Система ролей пользователей (пользователь, модератор, администратор)
- Групповые и индивидуальные разрешения
- Кастомные permission-классы
- Управление доступом к API-эндпоинтам

### 📊 Модели данных
- **Пользователи** - кастомная модель User с дополнительными полями
- **Статьи/Посты** - контент с различными уровнями доступа
- **Категории** - организация контента с правами доступа

## 🛠 Технологический стек

- **Backend**: Python 3.8+, Django 4.0, Django REST Framework 3.12
- **База данных**: PostgreSQL
- **Аутентификация**: JWT (djangorestframework-simplejwt)
- **Документация**: Swagger/OpenAPI
- **Тестирование**: pytest, Django Test Framework

## 📦 Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/VsevolodLunev/home_work_19.2.git
cd home_work_19.2
```

### 2. Создание виртуального окружения
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# или
venv\Scripts\activate  # Windows
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Настройка базы данных
```bash
python manage.py migrate
```

### 5. Создание суперпользователя
```bash
python manage.py createsuperuser
```

### 6. Запуск сервера
```bash
python manage.py runserver
```

## 🔑 API Endpoints

### Аутентификация
- `POST /api/token/` - получение JWT-токена
- `POST /api/token/refresh/` - обновление токена
- `POST /api/register/` - регистрация нового пользователя

### Пользователи
- `GET /api/users/` - список пользователей (только для администраторов)
- `GET /api/users/{id}/` - детали пользователя
- `PUT /api/users/{id}/` - обновление данных пользователя

### Статьи
- `GET /api/posts/` - список статей (разные права доступа)
- `POST /api/posts/` - создание статьи (аутентифицированные пользователи)
- `GET /api/posts/{id}/` - детали статьи
- `PUT /api/posts/{id}/` - обновление статьи (автор или модератор)
- `DELETE /api/posts/{id}/` - удаление статьи (автор или администратор)

## 🧪 Тестирование

Запуск тестов:
```bash
pytest
# или
python manage.py test
```

Тесты покрывают:
- Аутентификацию и авторизацию
- Permission-классы
- Бизнес-логику моделей
- API-эндпоинты

## 📚 Примеры использования

### Регистрация пользователя
```python
import requests

response = requests.post('http://localhost:8000/api/register/', {
    'username': 'newuser',
    'email': 'user@example.com',
    'password': 'securepassword123',
    'first_name': 'John',
    'last_name': 'Doe'
})
```

### Получение токена
```python
response = requests.post('http://localhost:8000/api/token/', {
    'username': 'newuser',
    'password': 'securepassword123'
})
token = response.json()['access']
```

### Доступ к защищенному эндпоинту
```python
headers = {'Authorization': f'Bearer {token}'}
response = requests.get('http://localhost:8000/api/posts/', headers=headers)
```

## 🏗 Архитектура

### Модели
- **CustomUser** - кастомная модель пользователя с расширенными полями
- **Post** - модель статей с системой прав доступа
- **Category** - категории для организации контента

### Permission-классы
- **IsOwnerOrReadOnly** - разрешение для владельца объекта
- **IsModerator** - права модератора
- **IsAdmin** - права администратора

### Сериализаторы
- Сериализаторы для всех моделей с валидацией данных
- Вложенные сериализаторы для связанных данных

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для фичи (`git checkout -b feature/amazing-feature`)
3. Закоммитьте изменения (`git commit -m 'Add amazing feature'`)
4. Запушьте в ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📄 Лицензия

Этот проект лицензирован под MIT License - смотрите файл [LICENSE](LICENSE) для деталей.

## 👨‍💻 Автор

**Всеволод Лунев**
- GitHub: [@VsevolodLunev](https://github.com/VsevolodLunev)
- Telegram: @iwizz
- Email: sevalunev@list.ru

---

⭐ Не забудьте поставить звезду репозиторию, если проект был полезен!
```
