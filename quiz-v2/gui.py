import tkinter as tk
from logic import QuizEngine
from questions import questions
from time_calculate import QuizTimer

BG_COLOR = "#F0F2F5"  
PRIMARY = "#4A90E2"   
TEXT_COLOR = "#333333"

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Quiz App')
        self.root.geometry('400x550')
        self.root.configure(bg=BG_COLOR)

        self.show_start_screen()

    def show_start_screen(self):
# first screen of the app
        self.clear_screen()

        tk.Label(self.root, text="Quiz Time", font=("Helvetica", 24, "bold"), 
                 bg=BG_COLOR, fg=PRIMARY).pack(pady=50)

        tk.Button(self.root, text="START", font=("Helvetica", 12, "bold"),
                  bg=PRIMARY, fg="white", width=15, height=2, bd=0,
                  command=self.start_quiz).pack(pady=20)

    def clear_screen(self):
# delete all the widgest
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_quiz(self):
# using quizengine class start the quiz
        self.quiz = QuizEngine(questions, num_questions=10)

        self.timer = QuizTimer()
        self.timer.start()

        self.show_quiz_screen()

    def show_quiz_screen(self):
# second screen that show user to question
        self.clear_screen()

        header = tk.Frame(self.root, bg=BG_COLOR)
        header.pack(fill="x", padx=20, pady=10)

        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 14), 
                                      wraplength=350, bg=BG_COLOR, fg=TEXT_COLOR)
        self.question_label.pack(pady=40)

        self.buttons = []
            
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Helvetica", 11),
                            bg="white", fg=TEXT_COLOR, width=30, pady=10, 
                            bd=1, relief="flat", command=lambda i=i: self.handle_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.score_label = tk.Label(header, text="Score: 0", bg=BG_COLOR, font=("Helvetica", 10))
        self.score_label.pack(side="left")

        self.timer_label = tk.Label(header, text="Time: 0s", bg=BG_COLOR, font=("Helvetica", 10))
        self.timer_label.pack(side="right")

        self.load_question()
        self.update_timer()

    def load_question(self):
# get the question and option
        question = self.quiz.get_current_question()

        if question is None:
            self.show_result_screen()
            return
            
        self.question_label.config(text=question['question'])

        for i, option in enumerate(question['options']):
            self.buttons[i].config(text=option, bg='white', fg=TEXT_COLOR, state='normal')

    def handle_answer(self, index):
# check answer
        
        correct_index = self.quiz.get_current_question()['answer']

        for btn in self.buttons:
            btn.config(state='disabled')

        if index == correct_index:
            self.buttons[index].config(bg='#2ECC71', fg='white')
        else:
            self.buttons[index].config(bg='#E74C3C', fg='white')
            self.buttons[correct_index].config(bg='#2ECC71', fg='white')

        self.quiz.check_answer(user_index=index)
        score = self.quiz.get_score()
        self.score_label.config(text=f"Score: {score}")

        self.root.after(1000, self.move_to_next)    

    def show_result_screen(self):
# screen that show result and time
        self.clear_screen()
        self.timer.stop()
        
        tk.Label(self.root, text="Finished!", font=("Helvetica", 20), bg=BG_COLOR).pack(pady=40)
        tk.Label(self.root, text=f"Total Score: {self.quiz.get_score()}", bg=BG_COLOR).pack()
        tk.Label(self.root, text=f"Time: {self.timer.get_elapsed_time()}s", bg=BG_COLOR).pack(pady=10)
        
        tk.Button(self.root, text="RESTART", bg=PRIMARY, fg="white", 
                  command=self.show_start_screen, bd=0, padx=20, pady=10).pack(pady=30)

        
    def update_timer(self):
# show time in the screen
        if not self.quiz.is_finished():
            self.timer_label.config(text=f"Time: {self.timer.get_elapsed_time()}s")
            self.root.after(1000, self.update_timer)

    def move_to_next(self):
# move to next question 
        self.quiz.next_question()
        self.load_question()
