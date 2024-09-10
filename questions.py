import json
import random


def get_questions(category , userID):
    question_json = open('question.json')
    user_json = open('user.json')
    # returns JSON object as a dictionary
    question_data = json.load(question_json)
    user_data = json.load(user_json)
    user ={}
    for i in user_data["user"]:
        if i["user_id"] == userID:
            user = i
            i["answers"] = []
            break
    #print(user)
    #print(category)
    #print([a for a in question_data["question"] if category == a["category"] and user["lastquestion"] <a['id'] < user["lastquestion"]+16 ])
    
    random_question = random.sample([a for a in question_data["question"] if category == a["category"] and user["lastquestion"]<a['id'] < user["lastquestion"]+16 ],5)
    return (random_question)


def update_answer(answer , userID):
    
    user_json = open('user.json')
    # returns JSON object as a dictionary
    question_json = open('question.json')
    user_data = json.load(user_json)
    for i in user_data["user"]:
        if i["user_id"] == userID:
            i["answers"].append(answer)
            i["lastquestion"] = answer["question_id"]
            break
    question_data = json.load(question_json)
    for j in question_data["question"]:
        j["attempt"] +=1
        if answer["isCorrect"] == True:
            j["correctattempt"] +=1
        j["time"] += answer["timespent"]
    return True



