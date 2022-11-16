from data import Test
import random
from tkinter import *


window = Tk()
window.title('Quizz_Game')
window.maxsize(width=500, height=500)
window.minsize(width=500, height=500)
window.config(background='lightGreen')



rand = random.Random()
result = Test['results']
question = result[int(rand.random()* len(result))]['question']

questions = StringVar()
mode = StringVar()
  
display_question = Label(window, textvariable=questions, foreground='darkBlue',
 background='lightGreen', font=('Microsoft JhengHeiUI', 15, 'normal'),
  wraplength=400, justify='center', padx=20, pady=20
  )

def change_question():
    global questions
    rand = random.Random()
    result = Test['results']
    question = result[int(rand.random()* len(result))]['question']
    questions.set(question)

  



display_question.pack()

questions.set(f'Q:{question}')
  
  

changing_button = Button(window, text='Next', relief='groove' , foreground='darkBlue', background='orange', command= change_question)
changing_button.pack(
    side='left',
)

def change_mode():
    if mode.get() == 'dark':
        window.config(background='#2e2e2e')
        display_question.config(foreground='lightGreen', background='#2e2e2e')
        light_mode.config(background='#2e2e2e', fg='white')
    else:
        window.config(background='lightGreen')
        display_question.config(foreground='darkBlue', background='lightGreen')
        light_mode.config(background='lightGreen', fg='black')


light_mode = Checkbutton(window, text='light/dark',  variable=mode, onvalue='dark', offvalue='light', command=change_mode, background='lightGreen',)
light_mode.pack(side='bottom')
window.mainloop()
