"""FastAPI-приложение для модели оттока."""

from fastapi import FastAPI
from fast_api_handler import FastApiHandler

# Запуск: из корня репо: uvicorn app.churn_app:app --reload --port 8081 --host 0.0.0.0
# Документация: http://127.0.0.1:8081/docs


# создаём FastAPI-приложение 
app = FastAPI()

# создаём обработчик запросов для API
app.handler = FastApiHandler()

@app.post("/api/churn/")
def get_prediction_for_item(user_id: str, model_params: dict):
    # Формируем параметры для обработчика
    params = {
        "user_id": user_id,
        "model_params": model_params
    }
    
    # Вызываем обработчик и возвращаем результат
    response = app.handler.handle(params)
    return response
