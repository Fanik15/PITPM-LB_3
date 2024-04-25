from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}/items/{item_id}")
async def read_item( item_id: str, q: str | None = None, short: bool = False #определение функции и принимает аргументы
):
    item = {"Ваня": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )# операторы добавляют значение q
    return item