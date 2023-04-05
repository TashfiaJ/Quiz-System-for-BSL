from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import JSONResponse
import sqlite3

app = FastAPI()

class Question(BaseModel):
    id: int
    label: str
    choice1: str
    choice2: str
    choice3: str
    choice4: str
    answer: str


@app.get("/getquestions")
async def get_questions():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions")
    data = cursor.fetchall()
    questions = []
    for question in data:
        questions.append({
            "id":question[0],
            "label":question[1],
            "choice1":question[2],
            "choice2":question[3],
            "choice3":question[4],
            "choice4":question[5],
            "answer":question[6]
        })
    conn.close()
    return questions
    

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)