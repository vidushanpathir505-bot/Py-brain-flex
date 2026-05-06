
import random

class QuizEngine:
    
    def __init__(self, all_questions, num_questions=10):
        self.questions = random.sample(all_questions, num_questions)
        self.current_question = 0
        self.score = 0

    def get_current_question(self):
# return the current question
        if not self.is_finished():
            return self.questions[self.current_question]
        return None
    
    def check_answer(self, user_index):
# check user answer right or wrong
        question = self.get_current_question()

        if question is None:
            return False
        
        correct_answer = question['answer']
        if user_index == correct_answer:
            self.score += 1
            return True
        return False
    
    def get_score(self):
# return the final score
        return self.score
    
    def next_question(self):
        self.current_question += 1

    def is_finished(self):
# check questions list ended or not 
        return self.current_question >= len(self.questions)
    
    def reset(self):
        self.current_question = 0
        self.score = 0


    
        