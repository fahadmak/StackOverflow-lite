from flask import Flask, jsonify, request, abort, Response

from app.model import Question, Answer, questions, answers

from app import app

def checkID(questionid):
    if questionid == "":
        abort(400)
    if type(questionid) != int:
        abort(400)
    if questionid not in [question["qn_id"] for question in Question.get_all_questions()]:
        abort(404)
    return questionid

@app.route('/api/v1/questions', methods=['GET'])
def get_all_questions():
    if len(questions) == 0:
        return jsonify({"message" : "They are currently no questions"})
    qns = Question.get_all_questions()
    return jsonify({"questions" : qns})

@app.route('/api/v1/questions/<int:questionid>', methods=['GET'])
def get_question_byID(questionid):    
    questionid = checkID(questionid)
    qn = Question.get_qn_byID(questionid)   
    return jsonify({"question" : qn})

@app.route('/api/v1/questions', methods=['POST'])
def add_questions():    
    if questions == []:
        questionid = 1
    else:
        questionid = max(question["qn_id"] for question in Question.get_all_questions()) + 1
    data = request.get_json()
    title = data['title']
    if title == "":
        abort(400)
    if type(title) != str:
        abort(400)
    body = data['body']
    if body == "":
        abort(400)
    if type(body) != str:
        abort(400)
    if Question.create_question(questionid, title, body):
        return jsonify({"msg":"Question added"}), 201

@app.route('/api/v1/questions/<int:questionid>/answers', methods=['POST'])
def add_answer(questionid):
    if answers == []:
        answerid = 1
    else:
        answerid = max(answer["qn_id"] for answer in Answer.get_all_answers()) + 1
    data = request.get_json()
    descr = data['descr']
    if descr == "":
        abort(400)
    if type(descr) != str:
        abort(400)
    questionid = checkID(questionid)                      
    if Answer.create_answer(questionid, answerid, descr):
        return jsonify({"msg":"Answer added"}), 201