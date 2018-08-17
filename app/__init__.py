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
        self.question['id'] = Question.ques_id
        Question.questions.append(self.question)

    @staticmethod
    def _get_all_questions():
        return Question.questions

    @staticmethod
    def _get_question_byId(ques_id):
        return [question for question in Question.questions if question['id'] == ques_id]

@app.route('/api/v1/questions', methods=['GET'])
def get_all_questions():
    return jsonify({'questions' : Question.questions})

@app.route('/api/v2/questions/<int:questionId>', methods=['GET'])
def get_question_byId(questionId):
    question = Question._get_question_byId(questionId)
    return jsonify({'question': question})

if __name__ == '__main__':
    app.run(debug=True)