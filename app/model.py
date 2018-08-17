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

