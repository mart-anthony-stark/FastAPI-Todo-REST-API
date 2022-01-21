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