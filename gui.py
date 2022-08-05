import time
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
from main import main
from history import save_txt


# Подумать если введут 1 в равенстве

def center_Window() -> None:
    w = 550
    h = 305

    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()

    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


def show_info() -> None:
    msg = 'Ваш файл сохранен в корне программы'
    mb.showinfo('Информация', msg)


def select_level() -> int | None:
    return level_var.get()


def generate() -> None:
    global counter, size, factor, summa

    try:
        size = int(entry_size.get())
        factor = select_level()
        summa = int(entry_summa.get())
        counter = int(entry_counter.get())
    except ValueError:
        exit(1)

    # DISABLED кнопки при нажатии.
    _on_click_btn()

    progress_bar['maximum'] = counter

    root.update()
    progress_bar['value'] = 0
    root.update()

    arr = []
    while progress_bar['value'] < counter:
        array = main(size, factor, summa)
        arr.append(array)
        progress_bar['value'] += 1
        root.update()
        time.sleep(0.5)
    # Сохранить в файл.
    save_txt(arr)
    # Вывести информацию.
    show_info()
    exit(1)


def _on_click_btn() -> None:
    if btn['state'] == tk.NORMAL:
        btn['state'] = tk.DISABLED


root = tk.Tk()
root.title("Генератор Уравнений")
center_Window()

frame_top = tk.Frame(root)
frame_top.pack()

tk.Label(frame_top, text='Генератор Уравнений',
         font=('Arial', 20, 'bold')).grid(row=0, column=0, columnspan=2, sticky='we')

frame = tk.LabelFrame(root)
frame.pack()

tk.Label(frame, text='Введите кол-во аргументов:', font=('Arial', 14)).grid(row=1, column=0, sticky='e')
entry_size = tk.Entry(frame, font=('Arial', 14), justify=tk.CENTER)
entry_size.grid(row=1, column=1, padx=10, pady=5, columnspan=3, sticky='we')

level_var = tk.IntVar()

tk.Label(frame, text='Выберите множитель:', font=('Arial', 14)).grid(row=2, column=0, sticky='e')

# Множитель.
levels = {
    10: 10,
    100: 100,
    1000: 1000
}

for key, level in enumerate(sorted(levels), 1):
    tk.Radiobutton(frame, text=levels[level],
                   font=('Arial', 14),
                   variable=level_var,
                   value=level,
                   command=select_level,
                   ).grid(row=2, column=key)

tk.Label(frame, text='Введите max сумму равенства:', font=('Arial', 14)).grid(row=3, column=0, sticky='e')
entry_summa = tk.Entry(frame, font=('Arial', 14), justify=tk.CENTER)
entry_summa.grid(row=3, column=1, padx=10, pady=5, columnspan=3, sticky='we')

tk.Label(frame, text='Введите кол-во уравнений:', font=('Arial', 14)).grid(row=4, column=0, sticky='e')
entry_counter = tk.Entry(frame, font=('Arial', 14), justify=tk.CENTER)
entry_counter.grid(row=4, column=1, padx=10, pady=5, columnspan=3, sticky='we')

btn = tk.Button(frame, text='Генерировать',
                font=('Arial', 18, 'bold'),
                bd=5,
                state=tk.NORMAL,
                command=generate)
btn.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky='we')

progress_bar = ttk.Progressbar(frame, orient='horizontal', mode='determinate', maximum=100, value=0)
progress_bar.grid(row=6, column=0, columnspan=4, padx=5, pady=5, sticky='we')

frame.grid_columnconfigure(0, minsize=200)
frame.grid_columnconfigure(1, minsize=50)
frame.grid_columnconfigure(2, minsize=50)
frame.grid_columnconfigure(3, minsize=50)

root.mainloop()
