from flask import Flask, jsonify, request

from model import Question

app = Flask(__name__)

question_1 = Question('Held up?')
question_2 = Question('Held up?')
all_questions = Question.questions

@app.route('/api/v1/questions')
def get_all_questions():
    pass

if __name__ == '__main__':
    app.run(debug=True)