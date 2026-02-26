# 🚀 Релиз модели в продакшен

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Container-blue?style=flat&logo=docker)](https://www.docker.com/)
[![Status](https://img.shields.io/badge/Status-Production-success.svg)]()

**Churn Prediction API:** FastAPI-сервис предсказания оттока клиентов (CatBoost), контейнеризация, готовность к мониторингу.

## 📋 Описание проекта

Проект по выкату ML-модели в продакшен: контейнеризация, API, пайплайн доставки и мониторинг. Демонстрирует полный цикл от обученной модели до работающего сервиса.

### Бизнес-задача

Обеспечить доступ к предсказаниям модели в production-среде с приемлемой задержкой, надёжностью и возможностью мониторинга.

**Бизнес-ценность:**
- Предсказания доступны для продукта или аналитики
- Воспроизводимость и версионирование деплоев
- Контроль качества и деградации модели

### Задача (ML Ops)

**Цель:** Релиз модели в продакшен с использованием современных практик (Docker, API, при необходимости CI/CD и мониторинг).

**Критерии:**
- Сервис отдаёт предсказания по API
- Контейнеризация (Docker)
- Документация по запуску и деплою

## Клонирование и запуск

```bash
git clone https://github.com/DataClasse/production-release.git
cd production-release
pip install -r requirements.txt
uvicorn app.churn_app:app --reload --port 8081 --host 0.0.0.0
```

Документация API и тестовые запросы: `http://127.0.0.1:8081/docs`

**API:**
- `POST /api/churn/` — предсказание оттока (user_id, model_params)
- `GET /docs` — Swagger

Путь к модели задаётся переменной окружения `MODEL_PATH` (по умолчанию `models/catboost_churn_model.bin`).

## 🎯 Ключевые достижения

- ✅ Контейнеризация ML-сервиса (Docker)
- ✅ REST API для получения предсказаний
- ✅ Версионирование артефактов и воспроизводимость деплоя
- ✅ При необходимости — интеграция с CI/CD и мониторингом

## 🛠 Технологический стек

- **Python** 3.8+, **FastAPI** — API
- **CatBoost** — модель оттока
- **Docker** — контейнеризация
- **MLflow** — артефакты и версии моделей
- При необходимости: **Kubernetes**, **Grafana**, **Prometheus**

## 🏗 Архитектура решения

```
Обученная модель (MLflow/S3)
        ↓
   Загрузка в сервис
        ↓
   FastAPI + Docker
        ↓
   Production API
        ↓
   Мониторинг (опционально)
```

## 👤 Автор

**Дмитрий Щербаков**

- 🔗 **Код:** [github.com/DataClasse/production-release](https://github.com/DataClasse/production-release)
- 📧 Email: [aiopendata@gmail.com](mailto:aiopendata@gmail.com)
- 💻 GitHub: [@DataClasse](https://github.com/DataClasse)

---

⭐ Если проект был полезен, поставьте звезду!
