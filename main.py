from tkinter import *
from tkinter.messagebox import *
import time
import datetime

root = Tk()


def download(list_text):
    f = open("text.txt")
    for line in f:
        list_text.append(line)
    f.close()


def finish(symbol_per_second, Error):
    S = f"Количество ошибок: {Error}" + '\n' + f'Символов в секунду: {symbol_per_second}'
    answer = askyesno(title='Сохранить статистику?', message=S)
    if (answer):
        f = open('statistics.txt', 'a')
        now = datetime.datetime.now()
        now = now.strftime("%d-%m-%Y %H:%M")
        info = str(now) + ':\n' + S + '\n\n'
        f.write(info)
        f.close()
        root.destroy()


def inp(event):
    global current_line, current_pos, Error, start_input, number_of_lines, time_start, numb_symb
    if event.char != '':
        input_symbol = event.char
        if input_symbol == list_text[current_line][current_pos]:
            if not start_input:
                time_start = time.time()
                start_input = True
            Input.config(state=NORMAL)
            Input.delete("%s-2c" % END)
            Input.insert(END, input_symbol)
            Input.insert(END, '|')
            Input.config(state=DISABLED)
            if current_pos == len(list_text[current_line]) - 2 and current_line + 1 != len(list_text) \
                    or current_line + 1 == len(list_text) and \
                    current_pos == len(list_text[current_line]) - 1:
                current_pos = 0
                current_line += 1
                Input.config(state=NORMAL)
                Input.delete("%s-2c" % END)
                Input.insert(END, '\n')
                Input.insert(END, '|')
                Input.config(state=DISABLED)
            else:
                current_pos += 1

            if len(list_text) == current_line:
                allTime = time.time() - time_start
                symb_per_second = round(numb_symb / allTime, 2)
                finish(symb_per_second, Error)
        else:
            Error += 1


list_text = []
download(list_text)
number_of_lines = len(list_text)
text = ''.join(list_text)
numb_symb = 0
time_start = 0
for i in list_text:
    numb_symb += len(i) - 1
start_input = False
root.update_idletasks()
root.geometry()
s = root.geometry()
s = s.split('+')
s = s[0].split('x')
width_root = int(s[0])
height_root = int(s[1])

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2
h = h // 2
w = w - width_root // 2
h = h - height_root // 2
root.geometry('800x650+{}+{}'.format(w - 400, h - 400))
f_task = LabelFrame(text="Task:")
Task = Label(f_task, text=text, font="Arial 20")
Input = Text(font="Arial 20", wrap=WORD, fg='red')
current_line = 0
current_pos = 0
Error = 0
Input.insert(END, '|')
Input.config(state=DISABLED)
Input.bind('<Key>', inp)
f_task.pack(fill=X, side=TOP)
f_task.pack()
Task.pack()
Input.pack(fill=X, side=TOP)


root.mainloop()
