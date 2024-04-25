from fastapi import FastAPI #импортирует класс FastAPI из библиотеки FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")#Определение маршрута для HTTP GET запроса по пути
async def read_file(file_path: str):
    return {"file_path": file_path}