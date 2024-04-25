from fastapi import FastAPI #импортирует класс FastAPI из библиотеки FastAPI.

app = FastAPI() # Создает экземпляр класса FastAPI и присваивает его переменной app


@app.get("/")
async def root():
    return {"message": "Hello World"} #Эта строка возвращает словарь с ключом "message" и значением "Hello World"