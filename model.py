class Question(object):
    ques_id = 0
    questions = [] 

    def __init__(self, title):
        self.question = {}
        self.question['title'] = title
        self.question['id_no'] += 1
        
    @staticmethod
    def get_all_questions(questions):
        pass
        

            

 
