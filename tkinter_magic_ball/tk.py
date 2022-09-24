from tkinter import *
from tkinter import messagebox
from random import choice
import time


answers = ['Бесспорно', 'Предрешено', 'Никаких\nсомнений', 'Определённо\nда', 'Можешь быть\nуверен\nв этом',
           'Мне кажется \nда', 'Вероятнее\nвсего', 'Хорошие\nперспективы', 'Знаки говорят\nда', 'Да',
           'Даже\nне думай', 'Мой ответ\nнет', 'По моим данным\nнет', 'Перспективы\nне очень\nхорошие',
           'Весьма\nсомнительно', 'Пока неясно,\nпопробуй снова', 'Спроси\nпозже', 'Лучше\nне рассказывать',
           'Сейчас\nнельзя\nпредсказать', 'Сконцентрируйся\nи спроси опять']


def choice_answer():        # функция для выбора ответа
    time.sleep(0.3)
    global ans_old
    ans_new = ans_old
    while ans_new == ans_old:   # чтобы один и тот же ответ не выпал два раза подряд
        ans_new = choice(answers)
    ans_old = ans_new
    canvas.itemconfig(answer, text=ans_old)


def on_restart():
    canvas.itemconfig(answer, text='Добро\nпожаловать!')


def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        root.destroy()


def window_close(this_window):      # функция чтобы окно инфо не дублировалось
    global window_open
    window_open = False
    this_window.destroy()


def press_info():
    global window_open
    if window_open:
        return
    info_window = Toplevel(root)
    info_window.title('Инфо')
    info_window.geometry('350x350+770+320')
    info_window.resizable(0, 0)
    info_window.iconphoto(False, icon)
    info_window.focus()
    info_window.wm_attributes("-topmost", 1)
    info_window.protocol("WM_DELETE_WINDOW", lambda this_window=info_window: window_close(this_window))
    window_open = True

    canvas_1 = Canvas(info_window, width=350, height=350,
                      bg="#391558", highlightthickness=0)  # включаем canvas
    canvas_1.pack()

    canvas_1.create_text(175, 80, text="Автор:\nИлья Панкратов", font=("WiGuru 2", 20),
                         fill='white', justify=CENTER, anchor=CENTER)

    canvas_1.create_text(175, 160, text="ilya-pankratov@list.ru", font=("WiGuru 2", 15),
                         fill='white', justify=CENTER, anchor=CENTER)

    canvas_1.create_text(175, 280, text="Создано на Python\nс помощью модуля tkinter", font=("WiGuru 2", 15),
                         fill='white', justify=CENTER, anchor=CENTER)


root = Tk()
root.title('Магический шар')        # параметры окна
root.geometry('700x556+600+200')
root.resizable(0, 0)

icon = PhotoImage(file='img/logo.png')      # иконка в углу
root.iconphoto(False, icon)

canvas = Canvas(root, width=700, height=556, highlightthickness=0)  # включаем canvas
canvas.pack()

img_obj1 = PhotoImage(file="img/magic_ball.png")        # фоновое изображение
canvas.create_image(0, 0, anchor=NW, image=img_obj1)

img_obj2 = PhotoImage(file="img/title.png")        # главный заголовок
canvas.create_image(-38, 10, anchor=NW, image=img_obj2)

ans_old = 'Добро\nпожаловать!'                              # текст с ответом
answer = canvas.create_text(345, 300, text=ans_old,
                            font=("WiGuru 2", 20), fill='white',
                            justify=CENTER, anchor=CENTER)

b1 = Button(root, text='ЗАДАЙ ВОПРОС И НАЖМИ',              # главная кнопка
            font=("WiGuru 2", 15), command=choice_answer,
            bg='#9FEE00', bd=8)
b1.place(x=182, y=480, width=330, height=50)


our_button1 = PhotoImage(file="img/button_restart.png")         # кнопка обновления
id_button1 = Button(root, image=our_button1, highlightthickness=0,
                    bg='#9FEE00', bd=4, command=on_restart)
id_button1.place(x=15, y=505)

our_button2 = PhotoImage(file="img/button_exit.png")            # кнопка выхода
id_button2 = Button(root, image=our_button2, highlightthickness=0,
                    bg='#9FEE00', bd=4, command=on_closing)
id_button2.place(x=645, y=505)

window_open = False
our_button3 = PhotoImage(file="img/button_info.png")            # кнопка инфо
id_button3 = Button(root, image=our_button3, highlightthickness=0,
                    bg='#9FEE00', bd=4, command=press_info)
id_button3.place(x=15, y=450)


root.mainloop()

