from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/submit/")
async def submit_data(name: str = Form(...), age: int = Form(...)):
    return {"name": name, "age": age}

