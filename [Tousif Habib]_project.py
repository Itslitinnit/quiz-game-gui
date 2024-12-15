from tkinter import *

score = 0

questions = [
    "What is the capital of Bangladesh?",
    "What is the capital of India?",
    "What is the capital of Pakistan?",
    "What is the capital of France?",
    "What is the capital of Germany?",
    "What is the capital of Japan?",
    "What is the capital of Ireland?",
    "What is the capital of Palestine?",
    "What is the capital of Spain?",
    "What is the capital of Canada?"]

answers = ["dhaka","new delhi","islamabad","paris","berlin", "tokyo","dublin", "jerusalem","madrid", "ottawa"]

def quiz():
    global score

    for i in range(len(answers)):
        user_ans = myanswer[i].get().lower()
        correct_ans = answers[i]

        if user_ans == correct_ans:
            score += 5
        else:
            score -= 2


    percentage = (score / 50) * 100
    result_text = f"Your score percentage is {percentage:.2f}% \n"


    if percentage >= 60:
        result_text += "You Passed. Congratulations!"
    else:
        result_text += "You Failed. Better luck next time."


    result_label.config(text=result_text) #result text update hobe
    submit_button.config(state="disabled")  #submit button disable


root = Tk()
root.geometry("500x755")
root.title("Quiz Game")

Label(root, text="Answer the questions and submit to see your score.",
      font=("arial", 10)).pack(pady=10)


myanswer= []  #my answer getting added to this empty list.
for i in range(len(questions)):
    question_label = Label(root, text=f"Q{i+1}: {questions[i]}", font=("arial", 10))
    question_label.pack(pady=5)

    answer_entry = Entry(root, font=("arial", 9))
    answer_entry.pack(pady=5)
    myanswer.append(answer_entry)

submit_button = Button(root, text="Submit",bg="pink", command=quiz, font=("arial", 10)) #submit button
submit_button.pack(pady=5)

result_label = Label(root, text="",fg='blue', font=("arial", 11)) #empty label jeta update hobe
result_label.pack(pady=10)

root.mainloop()
