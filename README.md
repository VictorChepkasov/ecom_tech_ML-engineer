# ecom_tech_ML-engineer
Тестовое задание в Ecom.tech на позицию ML-engineer - REST API сервис для загрузки и анализа успеваемости студентов.

---

# Запуск проекта

1. Клонирование репозитория
```bash
git clone <repo_url>
cd student-grades-api
```

2. Создание .env
```bash
cp .env.example .env
```

3. Сбор контейнера  

Для Linux Fedora:
```bash
docker build --network=host -t ecom_tech_ml-engineer-app .
docker compose up
```

Для Windows:
```bash
docker compose build
```

После запуска документация доступна по адресу:
http://localhost:8000/docs

## Применить миграции
```bash
docker compose exec app alembic upgrade head
```

## Запуск тестов
```bash
docker compose exec app pytest
```

---

# Функциональность

- Загрузка CSV-файла с оценками студентов
- Валидация данных
- Сохранение данных в PostgreSQL
- Аналитические endpoint'ы
- SQL-only реализация (без ORM)
- Docker 
- Alembic migrations
- Pytest tests

## Особенности реализации
- Перед загрузкой новых данных таблица очищается
- ORM не используется
- Используются транзакции PostgreSQL

---

# SQL-схема

SQL-скрипт создания таблицы находится в:

```text
sql/init.sql
```

Миграции Alembic находятся в:

```text
migrations/
```
---

# Технологии

- FastAPI
- PostgreSQL
- psycopg3
- Alembic
- Docker
- Pytest

---

# Зависимости

- Docker
- Docker Compose

Проверено на:
- Linux (Fedora)
