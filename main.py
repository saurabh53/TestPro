from typing import Union

from fastapi import FastAPI , Request
from questions import get_questions ,update_answer
from stats import mystat
app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/question/{category}")
def get_question(category: str ,request: Request):
    #userId = request.headers.get('userId')
    userId = 12
    item_id = get_questions(category , userId)
    return {"item_id": item_id}

@app.post("/updateanswer")
def update_answers( request: Request):
    #userId = request.headers.get('userId')
    #answer = request.json()
    answer =  {"question_id": 7 , "isCorrect":True,"myAnswer":"B","timespent":40}
    userId = 12
    updated = update_answer( answer, userId)
    return {"Updated": updated}

@app.get("/userstats/")
def get_stats(request: Request):
    #userId = request.headers.get('userId')
    userId = 12
    stats = mystat( userId)
    return {"stats": stats}