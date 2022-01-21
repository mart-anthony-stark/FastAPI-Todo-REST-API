from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# app object
app = FastAPI()

origins = [
    'https://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {"Data": "Hello"}

@app.get('/api/todo')
async def get_todo():
    return 1

@app.get('/api/todo/{id}')
async def get_todo_by_id(id: str):
    return id

@app.post('/api/todo')
async def create_todo(todo):
    return todo

@app.put('/api/todo/{id}')
async def update_todo(id, data):
    return id

@app.delete('/api/todo/{id}')
async def delete_todo_by_id(id):
    return id