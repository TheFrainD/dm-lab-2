import tkinter as tk
import pickle
import random

A = set()
B = set()
male_names = ['Богдан', 'Віталій', 'Віктор', 'Костя', 'Андрій', 'Антон', 'Денис', 'Сергій', 'Вова']
female_names = ['Маша', 'Аня', 'Оля', 'Елеонора', 'Люда', 'Катя', 'Юля', 'Даша', 'Настя', 'Аліна']
first_relation = []
second_relation = []


def message_window(root, msg):
    window = tk.Toplevel(root)
    window.title('Повідомлення')
    window.focus_set()

    lbl_msg = tk.Label(window,
                       text=msg)
    lbl_msg.pack()
    pass


def draw_graph(canvas, A, B, R, text, direction=tk.LAST):
    a_cords = {}
    b_cords = {}

    canvas.delete('all')
    canvas.create_text(100, 30, text=text, font='Arial 14')

    for i in range(len(A)):
        canvas.create_text(30 + i * 50, 50, text=list(A)[i])
        canvas.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill='green')
        a_cords.update({list(A)[i]: [30 + i * 50, 80]})

    for i in range(len(B)):
        canvas.create_text(30 + i * 50, 190, text=list(B)[i])
        canvas.create_oval([20 + i * 50, 160], [40 + i * 50, 180], fill='blue')
        b_cords.update({list(B)[i]: [30 + i * 50, 160]})
    for i in R:
        canvas.create_line(a_cords[i[0]], b_cords[i[1]], arrow=direction)
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
    global A, B, male_names, female_names

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

    lfr_male_names = tk.LabelFrame(window,
                                   text='Чоловічі імена')

    lbx_male_names = tk.Listbox(lfr_male_names,
                                selectmode=tk.EXTENDED)
    lbx_male_names.bind('<<ListboxSelect>>', lambda event: add_to_set(lbx_male_names, male_names, var.get()))
    lbx_male_names.pack()
    lbx_male_names.insert(tk.END, *male_names)

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
                        text='A = {}\nB = {}'.format(A, B))
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
    global A, B, female_names, male_names, first_relation, second_relation

    window = tk.Toplevel(root)
    window.title('Вікно №3')
    window.focus_set()

    def build_first_relation():
        global A, B, female_names, male_names, first_relation, second_relation

        a = []
        b = []
        for name in A:
            if name in female_names:
                a.append(name)
        for name in B:
            if name in male_names:
                b.append(name)

        first_relation = []
        for i in range(random.randint(1, len(a) - 1)):
            p = random.choice(list(a))
            q = random.choice(list(b))

            if p != q:
                first_relation.append((p, q))

            a.remove(p)
            b.remove(q)
        pass

    def build_second_relation():
        global A, B, female_names, male_names, first_relation, second_relation

        a = []
        b = []
        for name in A:
            if name in female_names:
                a.append(name)
        for name in B:
            if name in male_names:
                b.append(name)

        second_relation = []
        for i in range(random.randint(1, len(a) - 1)):
            p = random.choice(list(a))
            q = random.choice(list(b))

            if p != q and (p, q) not in first_relation:
                second_relation.append((p, q))

            a.remove(p)
            b.remove(q)
        pass

    lfr_set_a = tk.LabelFrame(window,
                              text='A')
    lbx_set_a = tk.Listbox(lfr_set_a,
                           selectmode=tk.EXTENDED)
    lbx_set_a.pack()
    lbx_set_a.insert(tk.END, *A)

    lfr_set_b = tk.LabelFrame(window,
                              text='B')
    lbx_set_b = tk.Listbox(lfr_set_b,
                           selectmode=tk.EXTENDED)
    lbx_set_b.pack()
    lbx_set_b.insert(tk.END, *B)

    build_first_relation()
    build_second_relation()

    can_graph_s = tk.Canvas(window,
                            width=620,
                            height=240)
    draw_graph(can_graph_s, A, B, first_relation, 'a теща b')

    can_graph_r = tk.Canvas(window,
                            width=620,
                            height=240)
    draw_graph(can_graph_r, A, B, second_relation, 'a дружина b')

    lfr_set_a.grid(row=0, column=0, padx=7)
    lfr_set_b.grid(row=0, column=1, padx=7)
    can_graph_s.grid(row=1, columnspan=2)
    can_graph_r.grid(row=2, columnspan=2)
    pass


def forth_window(root):
    global A, B, first_relation, second_relation, male_names, female_names

    window = tk.Toplevel(root)
    window.title('Вікно №4')
    window.focus_set()

    def union():
        set_result = list(set(second_relation).union(set(first_relation)))
        draw_graph(can_result, A, B, set_result, 'R ∪ S')
        pass

    def intersection():
        set_result = list(set(second_relation).intersection(set(first_relation)))
        draw_graph(can_result, A, B, set_result, 'R ∩ S')
        pass

    def difference():
        set_result = list(set(second_relation).difference(set(first_relation)))
        draw_graph(can_result, A, B, set_result, 'R \\ S')
        pass

    def extension():
        global A, B
        U = []
        for r in A:
            for s in B:
                if (r, s) not in second_relation:
                    U.append((r, s))
        U = list(set(U))
        draw_graph(can_result, A, B, U, 'U \\ R')
        pass

    def reverse():
        draw_graph(can_result, A, B, first_relation, 'S⁻¹', tk.FIRST)
        pass

    btn_union = tk.Button(window,
                          text='R ∪ S',
                          command=union)
    btn_intersection = tk.Button(window,
                                 text='R ∩ S',
                                 command=intersection)
    btn_difference = tk.Button(window,
                               text='R \\ S',
                               command=difference)
    btn_extension = tk.Button(window,
                              text='U \\ R',
                              command=extension)
    btn_reversed = tk.Button(window,
                             text='S⁻¹',
                             command=reverse)

    lbl_title = tk.Label(window,
                         text='Результати операцій над множинами')

    can_result = tk.Canvas(window,
                           width=620,
                           height=240)

    btn_union.grid(row=1, column=0)
    btn_intersection.grid(row=2, column=0)
    btn_difference.grid(row=3, column=0)
    btn_extension.grid(row=4, column=0)
    btn_reversed.grid(row=5, column=0)

    lbl_title.grid(row=0, column=1)
    can_result.grid(row=1, column=1, rowspan=5)
    pass


if __name__ == '__main__':
    main_window()
