class Questions(object):
    ques_id = 0
    questions: list = [] 

    def __init__(self, title):
        self.question = {}
        self.question['title'] = title
        Questions.ques_id += 1
        self.question['id_no'] = Questions.ques_id
        Questions.questions.append(self.questions)
        
    @staticmethod
    def get_all_questions(questions):
        if len(Questions.questions) == 0:
            raise ValueError("No questions!")
        else:
            return Questions.questions
        

            

 
