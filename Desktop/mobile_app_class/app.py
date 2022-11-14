import tkinter as tk



window = tk.Tk(screenName='Desktop App')
window.config(height=200, width=400)

contentFrame = tk.Frame(window, background='cyan')
contentFrame.config(height=200, width=200, borderwidth=2, relief='sunken')
contentFrame.pack()
changing_text = tk.StringVar()
num = 0
changing_text.set(f'{num}')
text = tk.Label(contentFrame, text=f'{num}', textvariable=changing_text)
text.pack()
def chaningText():
    global num,changing_text
    num += 1
    changing_text.set(f'{num}')

def chaningTextneg():
    global num,changing_text
    num -= 1
    changing_text.set(f'{num}')

ctlBtn = tk.Button(contentFrame, text='add', command=chaningText)
ctlBtn.pack()

ctlBtn1 = tk.Button(contentFrame, text='subtract', command=chaningTextneg)
ctlBtn1.pack()

image = tk.PhotoImage(name='smart phone', file='smartphone.png')

image_label = tk.Label(contentFrame, image=image)
image_label.pack()
check_var = tk.StringVar()
check_var.set('check on/off')
check_box = tk.Checkbutton(contentFrame, variable=check_var, text='check on/off', offvalue='False', onvalue='true', command=lambda:print(check_var.get()))
check_box.pack()
window.mainloop()