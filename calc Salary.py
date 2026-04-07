import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


class Finance:
    def __init__(self):
        self.doxod = []
        self.rasxod = []
        self.nalog = 0.13

    def add_doxod(self, amounts):
        self.doxod.extend(amounts)

    def add_rasxod(self, amounts):
        self.rasxod.extend(amounts)

    def sum_doxod(self):
        return sum(self.doxod)

    def sum_rasxod(self):
        return sum(self.rasxod)

    def shet_nalog(self):
        return self.sum_doxod() * self.nalog

    def chisti(self):
        return self.sum_doxod() - self.shet_nalog()

    def balance(self):
        return self.chisti() - self.sum_rasxod()

    def sred_doxod(self):
        return self.sum_doxod() / len(self.doxod) if self.doxod else 0

    def sred_rasxod(self):
        return self.sum_rasxod() / len(self.rasxod) if self.rasxod else 0

    def sled_god(self):
        bud_doxod = self.sred_doxod()
        bud_rasxod = self.sred_rasxod()
        return {
            "income": bud_doxod * 12,
            "expense": bud_rasxod * 12
        }


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Учёт личных финансов")
        self.f = Finance()

        # Поле для ввода дохода
        tk.Label(root, text="Доход (через запятую):").pack()
        self.inc_entry = tk.Entry(root, width=40)
        self.inc_entry.pack(pady=5)
        tk.Button(root, text="Запомнить доход", command=self.add_inc).pack()

        # Поле для ввода расхода
        tk.Label(root, text="Расход (через запятую):").pack()
        self.exp_entry = tk.Entry(root, width=40)
        self.exp_entry.pack()
        tk.Button(root, text="Запомнить расход", command=self.add_exp).pack()

        # Остальные кнопки
        tk.Button(root, text="Налоги", command=self.show_tax).pack()
        tk.Button(root, text="Прогноз на год", command=self.show_fore).pack()
        tk.Button(root, text="График дохода", command=self.plot_inc).pack()
        tk.Button(root, text="График расхода", command=self.plot_exp).pack()

    def parse_input(self, text):
        if not text:
            return []
        numbers = []
        parts = text.split(',')
        for part in parts:
            try:
                num = float(part.strip())
                numbers.append(num)
            except ValueError:
                continue
        return numbers

    def add_inc(self):
        text = self.inc_entry.get().strip()
        if text:
            amounts = self.parse_input(text)
            if amounts:
                self.f.add_doxod(amounts)
                messagebox.showinfo("Успех", f"Добавлено {len(amounts)} доходов")
                self.inc_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Ошибка", "Некорректный ввод")
        else:
            messagebox.showwarning("Ошибка", "Поле пустое")

    def add_exp(self):
        text = self.exp_entry.get().strip()
        if text:
            amounts = self.parse_input(text)
            if amounts:
                self.f.add_rasxod(amounts)
                messagebox.showinfo("Успех", f"Добавлено {len(amounts)} расходов")
                self.exp_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Ошибка", "Некорректный ввод")
        else:
            messagebox.showwarning("Ошибка", "Поле пустое")

    def show_tax(self):
        tax = self.f.shet_nalog()
        net = self.f.chisti()
        messagebox.showinfo("Налоги", f"Налог = {tax} руб.\nЧистый доход = {net} руб.")

    def show_fore(self):
        f = self.f.sled_god()
        bal = f["income"] - f["expense"]
        messagebox.showinfo(
            "Прогноз на следующий год",
            f"Доход: {f['income']:} руб.\n"
            f"Расход: {f['expense']:} руб.\n"
            f"Баланс: {bal:} руб."
        )

    def plot_inc(self):
        if not self.f.doxod:
            messagebox.showwarning("Ошибка", "Нет данных о доходах")
            return

        plt.figure("Доходы", figsize=(8, 6))
        x = list(range(1, len(self.f.doxod) + 1))  
        y = self.f.doxod

        # Линейный график с маркерами
        plt.plot(x, y, marker='o', color='purple', linewidth=2, markersize=8, label='Доход')
        plt.title("Доходы по операциям")
        plt.ylabel("Рубли")
        plt.xlabel("Номер операции")
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.tight_layout()
        plt.show() 

    def plot_exp(self):
        if not self.f.rasxod:
            messagebox.showwarning("Ошибка", "Нет данных о расходах")
            return

        plt.figure("Расходы", figsize=(8, 6))
        x = list(range(1, len(self.f.rasxod) + 1))
        y = self.f.rasxod

        # Линейный график с маркерами 
        plt.plot(x, y, marker='o', color='red', linewidth=2, markersize=8, label='Расход')
        plt.title("Расходы по операциям")
        plt.ylabel("Рубли")
        plt.xlabel("Номер операции")
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()