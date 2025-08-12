import tkinter as tk
from tkinter import messagebox

# Quiz Data
questions = [
    {
        "question": "Which fort is the birthplace of Chhatrapati Shivaji  Maharaj?",
        "options": ["Rajgad Fort", "Raigad Fort", "Purnadar Fort", "Shivneri Fort"],
        "answer": "Shivneri Fort"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Jupiter", "Mars", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "Who developed Python programming language?",
        "options": ["James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup"],
        "answer": "Guido van Rossum"
    },
    {
        "question": " What is the percentage of water on Earth's surface?",
        "options": ["Approximately 51%", " Approximately 60%", "Approximately 61%", "Approximately 71%"],
        "answer": "Approximately 71%"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Quiz Game")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        self.q_index = 0
        self.score = 0
        self.selected_option = tk.StringVar()

        self.title_label = tk.Label(root, text="Online Quiz Game", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=20)

        self.question_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0", wraplength=400, justify="left")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.selected_option, value="", font=("Arial", 12),
                                 bg="#f0f0f0", anchor="w")
            btn.pack(fill="x", padx=50, pady=5)
            self.option_buttons.append(btn)

        self.next_button = tk.Button(root, text="Next", font=("Arial", 12), command=self.next_question, bg="#4CAF50", fg="white", width=10)
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        self.selected_option.set(None)
        question_data = questions[self.q_index]
        self.question_label.config(text=f"{self.q_index + 1}. {question_data['question']}")
        for i, option in enumerate(question_data['options']):
            self.option_buttons[i].config(text=option, value=option)

    def next_question(self):
        selected = self.selected_option.get()
        if selected == "":
            messagebox.showwarning("No selection", "Please select an answer before continuing.")
            return

        correct_answer = questions[self.q_index]['answer']
        if selected == correct_answer:
            self.score += 1

        self.q_index += 1
        if self.q_index < len(questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        percentage = (self.score / len(questions)) * 100
        messagebox.showinfo("Quiz Completed", f"Your Score: {self.score}/{len(questions)}\nPercentage: {percentage:.2f}%")
        self.root.destroy()

# Run the App
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
