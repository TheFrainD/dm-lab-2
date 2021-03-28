import tkinter as tk
import pickle

A = set()
B = set()


def message_window(root, msg):
    window = tk.Toplevel(root)
    window.title('Повідомлення')
    window.focus_set()

    lbl_msg = tk.Label(window,
                       text=msg)
    lbl_msg.pack()
    pass


def main_window():
    def info_window():
        z = (8 + 5 % 60) % 30 + 1

        window = tk.Toplevel(root)
        window.title('Відомості про студента')
        window.focus_set()

        # Print info
        lbl_name = tk.Label(window, text="ПІБ: Зиков Дмитро Олексійович")
        lbl_group = tk.Label(window, text="Група: ІО-05")
        lbl_number = tk.Label(window, text="Номер у списку: 8")
        lbl_variant = tk.Label(window, text="Варіант: {}".format(str(z)))

        lbl_name.pack(padx=30)
        lbl_group.pack()
        lbl_number.pack()
        lbl_variant.pack()
        pass

    root = tk.Tk()
    root.title('Лабораторна робота №2')
    root.geometry('320x120')

    btn_info = tk.Button(root,
                         text='Відомості про студента',
                         command=info_window)
    btn_second_window = tk.Button(root,
                                  text='Вікно №2',
                                  command=lambda: second_window(root))
    btn_third_window = tk.Button(root,
                                 text='Вікно №3',
                                 command=lambda: third_window(root))
    btn_forth_window = tk.Button(root,
                                 text='Вікно №4',
                                 command=lambda: forth_window(root))

    btn_info.pack()
    btn_second_window.pack()
    btn_third_window.pack()
    btn_forth_window.pack()

    root.mainloop()
    pass


def second_window(root):
    global A, B

    window = tk.Toplevel(root)
    window.title('Вікно №2')
    window.focus_set()

    def update_sets_label():
        lbl_sets['text'] = 'A = {}\nB = {}'.format(A, B)

    def clear_set(choice):
        global A, B

        if choice == 0:
            A = set()
        else:
            B = set()

        update_sets_label()
        pass

    def radio_select():
        pass

    def add_to_set(listbox, names, set_choice):
        for i in listbox.curselection():
            if set_choice == 0:
                A.add(names[i])
            elif set_choice == 1:
                B.add(names[i])

        update_sets_label()
        pass

    def save_to_file(choice):
        global A, B

        if choice == 0:
            file = open('set_a.txt', 'wb')
            pickle.dump(A, file)
        else:
            file = open('set_b.txt', 'wb')
            pickle.dump(B, file)
        file.close()

        message_window(root, 'Збережено успішно!')
        pass

    def load_from_file(choice):
        global A, B

        if choice == 0:
            file = open('set_a.txt', 'rb')
            A = pickle.load(file)
        else:
            file = open('set_b.txt', 'rb')
            B = pickle.load(file)
        file.close()

        message_window(root, 'Зчитано успішно!')
        update_sets_label()
        pass

    var = tk.IntVar()

    rad_set_a = tk.Radiobutton(window,
                               text='Множина А',
                               variable=var,
                               value=0,
                               command=radio_select)
    rad_set_a.select()

    rad_set_b = tk.Radiobutton(window,
                               text='Множина B',
                               variable=var,
                               value=1,
                               command=radio_select)

    male_names = ['Андрій', 'Антон', 'Денис', 'Богдан', 'Віталій', 'Віктор', 'Костя', 'Сергій', 'Вова']

    lfr_male_names = tk.LabelFrame(window,
                                   text='Чоловічі імена')

    lbx_male_names = tk.Listbox(lfr_male_names,
                                selectmode=tk.EXTENDED)
    lbx_male_names.bind('<<ListboxSelect>>', lambda event: add_to_set(lbx_male_names, male_names, var.get()))
    lbx_male_names.pack()
    lbx_male_names.insert(tk.END, *male_names)

    female_names = ['Настя', 'Маша', 'Аня', 'Катя', 'Юля', 'Даша', 'Оля', 'Люда']

    lfr_female_names = tk.LabelFrame(window,
                                     text='Жіночі імена')

    lbx_female_names = tk.Listbox(lfr_female_names,
                                  selectmode=tk.EXTENDED)
    lbx_female_names.bind('<<ListboxSelect>>', lambda event: add_to_set(lbx_female_names, female_names, var.get()))
    lbx_female_names.pack()
    lbx_female_names.insert(tk.END, *female_names)

    btn_save_a = tk.Button(window,
                           text='Зберегти множину А у файл',
                           command=lambda: save_to_file(0))
    btn_load_a = tk.Button(window,
                           text='Зчитати множину А з файлу',
                           command=lambda: load_from_file(0))
    btn_clear_a = tk.Button(window,
                            text='Очистити множину А',
                            command=lambda: clear_set(0))

    btn_save_b = tk.Button(window,
                           text='Зберегти множину B у файл',
                           command=lambda: save_to_file(1))
    btn_load_b = tk.Button(window,
                           text='Зчитати множину B з файлу',
                           command=lambda: load_from_file(1))
    btn_clear_b = tk.Button(window,
                            text='Очистити множину B',
                            command=lambda: clear_set(1))

    lfr_sets = tk.LabelFrame(window,
                             text='Множини')
    lbl_sets = tk.Label(lfr_sets,
                        text='A = {}\nB = {}')
    lbl_sets.pack()

    rad_set_a.grid(row=0, column=0)
    rad_set_b.grid(row=0, column=1)

    lfr_male_names.grid(row=1, column=0)
    lfr_female_names.grid(row=1, column=1)

    btn_load_a.grid(row=2, column=0, padx=20, pady=5)
    btn_load_b.grid(row=2, column=1)

    btn_save_a.grid(row=3, column=0, pady=5)
    btn_save_b.grid(row=3, column=1)

    btn_clear_a.grid(row=4, column=0, pady=5)
    btn_clear_b.grid(row=4, column=1)

    lfr_sets.grid(row=5, column=0, columnspan=2, sticky='W')
    pass


def third_window(root):
    window = tk.Toplevel(root)
    window.title('Вікно №3')
    window.focus_set()
    pass


def forth_window(root):
    window = tk.Toplevel(root)
    window.title('Вікно №4')
    window.focus_set()
    pass


if __name__ == '__main__':
    main_window()
