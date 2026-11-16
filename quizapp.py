
import tkinter as tk

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Pune", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for AI?",
        "options": ["HTML", "Python", "CSS", "Java"],
        "answer": "Python"
    },
    {
        "question": "What is 10 + 5?",
        "options": ["10", "20", "15", "25"],
        "answer": "15"
    }
]

score = 0
current = 0


def show_question():
    global current

    if current == len(questions):
        question_label.config(
            text="Quiz Completed!\nYour Score: " + str(score) + "/3"
        )
        feedback.config(text="Well done!")
        for btn in buttons:
            btn.pack_forget()

        next_btn.config(text="Restart", command=restart)
        return

    q = questions[current]
    question_label.config(text=q["question"])
    feedback.config(text="")

    for i in range(4):
        buttons[i].config(
            text=q["options"][i],
            state="normal"
        )


def check_answer(choice):
    global score

    correct = questions[current]["answer"]

    if buttons[choice]["cget"]("text") == correct:
        feedback.config(text="Correct!", fg="green")
        score += 1
    else:
        feedback.config(
            text="Wrong! Answer: " + correct,
            fg="red"
        )

    for btn in buttons:
        btn.config(state="disabled")


def next_question():
    global current
    current += 1
    show_question()


def restart():
    global score, current
    score = 0
    current = 0
    for btn in buttons:
        btn.pack(pady=5, fill="x")
    next_btn.config(text="Next Question", command=next_question)
    show_question()


# Main window
root = tk.Tk()
root.title("My Quiz App")
root.geometry("400x450")
root.config(bg="#eaf2f8")

title = tk.Label(
    root,
    text="MY QUIZ APP",
    font=("Arial", 22, "bold"),
    bg="#eaf2f8"
)
title.pack(pady=20)

question_label = tk.Label(
    root,
    text="",
    font=("Arial", 15),
    bg="#eaf2f8",
    wraplength=350
)
question_label.pack(pady=20)

buttons = []

for i in range(4):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 12),
        command=lambda x=i: check_answer(x)
    )
    btn.pack(pady=5, fill="x", padx=40)
    buttons.append(btn)

feedback = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="#eaf2f8"
)
feedback.pack(pady=15)

next_btn = tk.Button(
    root,
    text="Next Question",
    font=("Arial", 12, "bold"),
    bg="#2874a6",
    fg="white",
    command=next_question
)
next_btn.pack(pady=10)

show_question()

root.mainloop()
