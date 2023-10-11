from tkinter import *


class App:
    def start_up(self):
        self.root = Tk()
        self.root.title('Калькулятор ИМТ')
        self.root.geometry('300x400+500+150')
        self.root.resizable(True, True)
        self.root.configure(bg='light blue')
        self.root.maxsize(375, 500)
        self.root.protocol("WM_DELETE_WINDOW", self.win_close)

        self.drow()

    def win_close(self):
        self.root.destroy()
        print("Программа завершена")

    def drow(self):
        self.header_label = Label(text='РАСЧЁТ ВАШЕГО ИНДЕКСА МАССЫ ТЕЛА', bg='light blue',
                             font='sans-serif 10')  # заголовок
        self.header_label.pack(anchor="n", pady=5)

        self.first_label = Label(text='Ваш рост (в см):', bg='light blue',
                            font='sans-serif 10', )  # надпись "Ваш рост (в см):"
        self.first_label.pack(anchor="n", padx=50, pady=1)

        self.first_entry = Entry(bg='light gray', width=40,
                            justify=CENTER)  # поле для ввода текста под надписью "Ваш рост (в см):"
        self.first_entry.pack(anchor="n", padx=100, pady=1, )

        self.second_label = Label(text='Ваш вес (в кг):', bg='light blue', font='sans-serif 10')  # надпись "Ваш вес (в кг):"
        self.second_label.pack(anchor="n", padx=50, pady=1)

        self.second_entry = Entry(bg='light gray', width=40,
                             justify=CENTER)  # поле для ввода текста под надписью "Ваш вес (в кг):"
        self.second_entry.pack(anchor="n", padx=100, pady=1)

        self.result_label = Label(text='ВАШ ИМТ:\n-', bg='light blue', font='sans-serif 15')  # надпись "ВАШ ИМТ:"
        self.result_label.pack(anchor="n", padx=50, pady=5)

        self.ref_label = Label(bg='light blue',
                          text='Классификация ИМТ:\n16 и менее — выраженный дефецит массы тела;\n16-18,5 — недостаточная масса тела\n18,5-25 — норма\n25-30 — избыточная масса тела\n30-35 — ожирение 1-й степени\n35-40 — ожирение 2-й степени\n40 и более — ожирение 3-й степени',
                          font='sans-serif 8')
        self.ref_label.pack(fill=BOTH, anchor="n", padx=20, pady=15, expand=True)

        self.button = Button(bg='light pink', text='Вычислить ИМТ', command=self.calc_bmi)  # кнопка "Вычислить ИМТ"
        self.button.pack(fill=X, anchor="center", padx=20, pady=5, ipady=20, expand=True)

        self.root.protocol("WM_DELETE_WINDOW", self.win_close)  # завершение программы

        self.root.mainloop()

    def calc_bmi(self):
        h = self.first_entry.get()
        m = self.second_entry.get()
        if m.isdigit() and h.isdigit():
            h, m = int(h), int(m)
            result = round(m / ((h / 100) ** 2), 1)

            self.result_label.config(text='ВАШ ИМТ:\n' + str(result))
        else:
            self.result_label.config(text='ВАШ ИМТ:\n' + 'Ошибка')


if __name__ == "__main__":
    app = App()
    app.start_up()
