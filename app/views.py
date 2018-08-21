from flask import Flask, jsonify, request

from app.model import Question, Answer, questions, answers

from app import app

@app.route('/api/v1/questions', methods=['GET'])
def get_all_questions():
    return jsonify({"questions" : Question.get_all()})

@app.route('/api/v1/questions/<questionid>', methods=['GET'])
def get_question_byID(questionid):
    questionid = int(questionid)
    return jsonify({"question" : Question.get_qn_byID(questionid) })

@app.route('/api/v1/questions', methods=['POST'])
def add_questions():
    if len(questions) == 0:
        questionid = 1
    else:
        questionid = len(questions) + 1
    data = request.get_json()
    title = data['title']
    body = data['body']
    if Question.create_question(questionid, title, body):
        return jsonify({"msg":"Question added"}), 201

@app.route('/api/v1/questions/<questionid>/answers', methods=['POST'])
def add_answer(questionid):
    if len(answers) == 0:
        an_id = 1
    else:
        an_id = len(answers) + 1
    data = request.get_json()
    descr = data['descr']
    qn_id = questionid
    if Question.create_question(qn_id, an_id, descr):
        return jsonify({"msg":"Answer added"}), 201