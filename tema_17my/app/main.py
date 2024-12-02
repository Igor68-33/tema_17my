from fastapi import FastAPI
from router import task, user

app = FastAPI()


@app.get("/")
def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router_task)
app.include_router(user.router_user)

