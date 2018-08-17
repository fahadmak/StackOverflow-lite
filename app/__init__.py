from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['TESTING'] = True
app.testing = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

class Question(object):

    ques_id = 0
    questions: list = []

    def __init__(self, name):
        self.question = {}
        self.question['name'] = name
        Question.ques_id += 1
        self.question['id_no'] = Question.ques_id
        Question.questions.append(self.question)

    @staticmethod
    def get_all_questions():
        return Question.questions

question_1 = Question('Who is who?')
question_2 = Question('No man?')
question_2 = Question('wtfd?')
all_questions = Question.questions

@app.route('/api/v1.0/items', methods=['GET'])
def get_all_questions():
    return jsonify({'questions' : all_questions})

if __name__ == '__main__':
    app.run(debug=True)