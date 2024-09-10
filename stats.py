import json
def mystat(userID):
    user_json = open('user.json')
    # returns JSON object as a dictionary
    question_json = open('question.json')
    user_data = json.load(user_json)
    question_data = json.load(question_json)
    data = []
    for i in user_data["user"]:
        if i["user_id"] == userID:
            for questiondetails in i ["answers"]:
                for questions in question_data:
                    if questiondetails["question_id"] == questions["id"]:
                        data.append({"question":questions["question"][0:questions["question"].find('.')],"attempt":questions["attempt"],"correctattempt":questions["correctattemp"],"myattempt":questiondetails["isCorrect"],"mytime":questiondetails["timespent"]})
        break
    return(data)

                