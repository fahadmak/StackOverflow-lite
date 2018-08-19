from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['TESTING'] = True
app.testing = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

class Question(object):

    ques_id = 0
    questions: list = []

    def __init__(self):
        self.question = {}

    @staticmethod
    def _get_all_questions():
        return Question.questions

    @staticmethod
    def _get_question_byId(ques_id):
        return [question for question in Question.questions if question['id'] == ques_id]
    
    def _add_question(self,name):
        Question.ques_id += 1
        self.question['id'] = Question.ques_id
        self.question['name'] = name
        Question.questions.append(self.question)

    @staticmethod
    def _add_answer(id_no, answer):
        for question in Question.questions:
            if question['id'] == id_no:
                question['answer'] = answer

@app.route('/api/v1/questions', methods=['GET'])
def get_all_questions():
    return jsonify({'questions' : Question._get_all_questions()})

@app.route('/api/v2/questions/<int:questionId>', methods=['GET'])
def get_question_byId(questionId):
    questionw = Question._get_question_byId(questionId)
    return jsonify({'question': questionw})

@app.route('/api/v3/questions', methods=['POST'])
def add_question():
    return jsonify({'questions' : Question.questions}), 201

@app.route('/api/v4/questions/<int:questionId>', methods=['POST'])
def add_answer(questionId):
    questionw = Question._get_question_byId(questionId)
    return jsonify({'questions' : questionw}), 201

if __name__ == '__main__':
    app.run(debug=True)