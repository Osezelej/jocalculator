from Data import data
import random
from tkinter import *


window = Tk()
window.title('Quizz_Game')
window.maxsize(width=500, height=500)
window.minsize(width=500, height=500)
window.config(background='lightGreen')



rand = random.Random()
rand.shuffle(data['results'])
result = data['results']
question_list = [item['question'] for item in result]
answers = []
correct_answer = [item['correct_answer'] for item in result]
incorrect_answer = [item['incorrect_answers'] for item in result]

for inc_a, c_a in zip(incorrect_answer, correct_answer):
    inc_a.append(c_a)
    rand.shuffle(inc_a)
    answers.append(inc_a)

question_index = 0
question = question_list[question_index]
answer = answers[question_index]

questions = StringVar()
mode = StringVar()
optiona = StringVar()  
optionb = StringVar()  
optionc = StringVar()
optiond = StringVar()

options = [optiona, optionb, optionc, optiond]
alpha = ['a', 'b', 'c', 'd']

display_question = Label(window, textvariable=questions, foreground='darkBlue',
 background='lightGreen', font=('Microsoft JhengHeiUI', 15, 'normal'),
  wraplength=400, justify='center', padx=20, pady=20
  )

def change_question():
    global questions, question_index, answer

    if question_index < len(question_list) - 1:
        question_index += 1
        question = question_list[question_index]
        answer = answers[question_index]
        questions.set(f'Q{question_index + 1}:{question}')
        num = 0
        for ans, option, a in zip(answer, options, alpha):
            num += 1
            option.set(f'{a}. {ans}')
        if num < 4:
            d = 1
            for i in range(num):
                options[-d].set('')
                d += 1

    else:
        
        question_index += 1
        questions.set(f'YOU HAVE COMPLETED THE QUESTIONS')
        optiona.set('')
        optionb.set('')
        optionc.set('')
        optiond.set('')
        next_button.config(text='Finish')



def change_questionback():
    global questions, question_index
    if question_index > 0:
        question_index -= 1
        question = question_list[question_index]
        answer = answers[question_index]
        questions.set(f'Q{question_index + 1}:{question}')
        num = 0
        for ans, option, a in zip(answer, options, alpha):
            num += 1
            option.set(f'{a}. {ans}')
        if num < 4:
            d = 1
            for i in range(num):
                options[-d].set('')
                d += 1
    
display_question.pack()

questions.set(f'Q{question_index + 1}:{question}')
  
  

next_button = Button(window, text='Next', relief='groove' , foreground='darkBlue', background='orange', command= change_question)
next_button.pack(
    side='right',
)
prev_button = Button(window, text='Prev', relief='groove' , foreground='darkBlue', background='orange', command= change_questionback)
prev_button.pack(
    side='left',
)

def change_mode():
    if mode.get() == 'dark':
        window.config(background='#2e2e2e')
        display_question.config(foreground='lightGreen', background='#2e2e2e')
        option_a.config(foreground='lightGreen', background='#2e2e2e')
        option_b.config(foreground='lightGreen', background='#2e2e2e')
        option_c.config(foreground='lightGreen', background='#2e2e2e')
        option_d.config(foreground='lightGreen', background='#2e2e2e')
        light_mode.config(background='#2e2e2e', fg='white')
    else:
        window.config(background='lightGreen')
        display_question.config(foreground='darkBlue', background='lightGreen')
        option_a.config(foreground='darkBlue', background='lightGreen')
        option_b.config(foreground='darkBlue', background='lightGreen')
        option_c.config(foreground='darkBlue', background='lightGreen')
        option_d.config(foreground='darkBlue', background='lightGreen')
        light_mode.config(background='lightGreen', fg='black')


light_mode = Checkbutton(window, text='light/dark',  variable=mode, onvalue='dark', offvalue='light', command=change_mode, background='lightGreen',)
light_mode.pack(side='bottom')



for ans, option, a in zip(answer, options, alpha):
    option.set(f'{a}. {ans}')

option_a = Label(window, textvariable=optiona, foreground='darkBlue',
 background='lightGreen', font=('Microsoft JhengHeiUI', 12, 'normal'),
  wraplength=400, justify='center', padx=20, pady=15
  )
option_a.pack()

option_b = Label(window, textvariable=optionb, foreground='darkBlue',
 background='lightGreen', font=('Microsoft JhengHeiUI', 12, 'normal'),
  wraplength=400, justify='center', padx=20, pady=15
  )
option_b.pack()

option_c = Label(window, textvariable=optionc, foreground='darkBlue',
 background='lightGreen', font=('Microsoft JhengHeiUI', 12, 'normal'),
  wraplength=400, justify='center', padx=20, pady=15
  )
option_c.pack()

option_d = Label(window, textvariable=optiond, foreground='darkBlue',
 background='lightGreen', font=('Microsoft JhengHeiUI', 12, 'normal'),
  wraplength=400, justify='center', padx=20, pady=15
  )
option_d.pack()

window.mainloop()
