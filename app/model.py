questions = []
answers = []

class Question(object):
   
    def __init__(self, qn_id, title, body):
        self.title = title
        self.qn_id = qn_id
        self.body = body
    
    def to_json(self):
        data = {'qn_id' : self.qn_id, 'title' : self.title, 'body' : self.body}
        return data

    @classmethod
    def create_question(cls, qn_id, title, body):
        question = Question(qn_id, title, body)
        questions.append(question)
        return True

    @classmethod
    def get_qn_byID(cls, qn_id):
        qn = []
        for question in questions:
            quest = question.to_json()            
            qn.append(quest)
        qid = [ques_id for ques_id in qn if ques_id['qn_id'] == qn_id]
        return qid
            
    @classmethod
    def get_all(cls):
        quns =[]
        for question in questions:
            quest = question.to_json()            
            quns.append(quest)
            print(quns)
        return quns

class Answer(object):

    def __init__(self, qn_id, an_id, descr):
        self.descr = descr
        self.qn_id = qn_id
        self.an_id = an_id

    @classmethod
    def create_answer(cls, qn_id, an_id, descr):
        for question in questions:
            if question.qn_id == qn_id: 
                answer = Answer(qn_id, an_id, descr)
                answers.append(answer)
                return True

    def to_json(self):
        data = {'qn_id' : self.qn_id, 'an_id' : self.an_id, 'descr' : self.descr}
        return data


        