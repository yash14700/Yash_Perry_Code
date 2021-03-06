"""
########################################################################################
THe Goal of this file is to build a quiz that is uploaded to a professors canvas,
The professor can answer 1 - 4, 1 being a bad questoin and 4 being a good question
########################################################################################
"""

"""
# Short term changes
-> Ask to get lecture title along with JSON files
-> Deal with questions that are not mcq
-> Account for this in the google app script as well

# Long term changes
-> Either export everything to google app script, or use python with canvas (using a combination makes no sense)
"""
import simplejson as json
#import os
import requests
import glob

class CanvasAnswer:
    def __init__(self):
        self.template = {
            "answer_text":"",
            "answer_weight":0
        }

class CanvasQuestion:
    def __init__(self):
        self.template = {
            "question":{
                "question_text":"",
                "points_possible":1,
                "answers":[]
            }
        }

# This function reads a specified json file and returns a list of questions objects
def get_question_list(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data["questions"]

def edit_json(raw_questions):
    #Stuff to run
    CanvasQuiz = list()
    for q in raw_questions:
        if q["answer"] == "(NO ANSWER PROVIDED)":
            continue

        new_question = CanvasQuestion()
        new_question.template["question"]["question_text"] = q["main"]
        # print(q["main"]),
        # print(q["mcq"])
        for ans in q["mcq"]:
            new_answer = CanvasAnswer()
            new_answer.template["answer_text"] = ans["option"]
            if ans["isAnswer"] == "true":
                new_answer.template["answer_weight"] = 1
            # print(json.dumps(new_answer.template, indent=4))
            new_question.template["question"]["answers"].append((new_answer.template))

        # print(json.dumps(new_question.template, indent=4))
        CanvasQuiz.append((new_question.template))
    return CanvasQuiz

    # print(json.dumps(questions, indent=4))


# token = "1770~3FrepjbEWYfZWRYVMUKTxYAwMG6PEdSQ3sygnlgWmL7vPugKSK2Iudy4z2xxOJWx"
# r = requests.post("https://canvas.instructure.com/api/v1/courses/17700000000277379/quizzes?access_token=1770~3FrepjbEWYfZWRYVMUKTxYAwMG6PEdSQ3sygnlgWmL7vPugKSK2Iudy4z2xxOJWx", json={"title":"Test"})
# r2 = requests.get("https://canvas.instructure.com/api/v1/courses/17700000000277379/quizzes?access_token=1770~3FrepjbEWYfZWRYVMUKTxYAwMG6PEdSQ3sygnlgWmL7vPugKSK2Iudy4z2xxOJWx")
# print(json.dumps(r.json(), indent = 4))
# print(json.dumps(r2.json(), indent = 4))
