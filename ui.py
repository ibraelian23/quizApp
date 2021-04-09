from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR,padx=20,pady=20)

        self.label = Label(text=f"Score : {self.score}",bg=THEME_COLOR,fg="white",font=("Arial",10,"bold"))
        self.label.grid(row=0,column=1)

        self.question_canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.question_canvas.create_text(150,125, text="wow",font=("Arial",20,"italic"), width=280)
        self.question_canvas.grid(row=1, columnspan=2,pady=20)

        def true_button():
            if self.quiz.still_has_questions():
                self.score = self.quiz.check_answer("True")
                self.get_next_q()
                self.label.configure(text=f"Score : {self.score}")
            else:
                self.completed_quiz()
        def false_button():
            if self.quiz.still_has_questions():
                self.score = self.quiz.check_answer("False")
                self.get_next_q()
                self.label.configure(text=f"Score : {self.score}")
            else:
                self.completed_quiz()

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=true_img,highlightthickness=0, command=true_button)
        self.false_button = Button(image=false_img,highlightthickness=0, command=false_button)
        self.true_button.grid(row=2, column=0,pady=20)
        self.false_button.grid(row=2, column=1,pady=20)

        self.get_next_q()

        self.window.mainloop()

    def get_next_q(self):
        question_text = self.quiz.next_question()
        self.question_canvas.itemconfig(self.question, text=question_text)

    def completed_quiz(self):
        current_score = self.quiz.score
        question_number = self.quiz.question_number
        self.question_canvas.itemconfig(self.question, text=f"You've completed the quiz\n"
                                                            f"Your final score was: {current_score}/{question_number}")






