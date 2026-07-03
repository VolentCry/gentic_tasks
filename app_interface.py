import customtkinter as ctk
import dnk_calculation as dnk_calc
import genetic_calculation as gen_calc

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Биологический калькулятор")
        self.geometry("500x600")

        # Создаем вкладки
        self.tabview = ctk.CTkTabview(self, width=450, height=550)
        self.tabview.pack(padx=20, pady=20, fill="both", expand=True)

        self.tabview.add("ДНК / РНК")
        self.tabview.add("Генетика")

        self.setup_dnk_tab()
        self.setup_genetic_tab()

    def setup_dnk_tab(self):
        tab = self.tabview.tab("ДНК / РНК")

        self.seq_input = ctk.CTkEntry(tab, placeholder_text="Введите последовательность (напр. АТЦГ)", width=400)
        self.seq_input.pack(pady=15)

        # Кнопки для разных операций
        self.btn_dnk_to_rnk = ctk.CTkButton(tab, text="ДНК -> РНК (иРНК, тРНК)", command=self.dnk_to_rnk)
        self.btn_dnk_to_rnk.pack(pady=5)

        self.btn_rnk_to_dnk = ctk.CTkButton(tab, text="иРНК -> ДНК", command=self.rnk_to_dnk)
        self.btn_rnk_to_dnk.pack(pady=5)

        self.btn_decode_dnk = ctk.CTkButton(tab, text="Расшифровать ДНК", command=self.decode_dnk)
        self.btn_decode_dnk.pack(pady=5)

        self.btn_decode_rnk = ctk.CTkButton(tab, text="Расшифровать РНК", command=self.decode_rnk)
        self.btn_decode_rnk.pack(pady=5)

        # Поле вывода
        self.dnk_output = ctk.CTkTextbox(tab, width=400, height=200)
        self.dnk_output.pack(pady=15, fill="both", expand=True)

    def setup_genetic_tab(self):
        tab = self.tabview.tab("Генетика")

        self.parent1_input = ctk.CTkEntry(tab, placeholder_text="Родитель 1 (напр. AABB)", width=400)
        self.parent1_input.pack(pady=10)

        self.parent2_input = ctk.CTkEntry(tab, placeholder_text="Родитель 2 (напр. aabb)", width=400)
        self.parent2_input.pack(pady=10)

        self.mendel_var = ctk.IntVar(value=0)
        self.mendel_switch = ctk.CTkSwitch(tab, text="Вывести таблицу Менделя", variable=self.mendel_var)
        self.mendel_switch.pack(pady=10)

        self.btn_calc_gen = ctk.CTkButton(tab, text="Рассчитать поколения", command=self.calc_genetic)
        self.btn_calc_gen.pack(pady=15)

        self.gen_output = ctk.CTkTextbox(tab, width=400, height=200)
        self.gen_output.pack(pady=10, fill="both", expand=True)

    # --- Функции ДНК/РНК ---
    def out_dnk(self, text):
        self.dnk_output.delete("0.0", "end")
        self.dnk_output.insert("0.0", text)

    def dnk_to_rnk(self):
        seq = self.seq_input.get()
        try:
            info, trans = dnk_calc.dnk_convertor_in_rnk(seq)
            self.out_dnk(f"иРНК: {info}\nтРНК: {trans}")
        except Exception as e:
            self.out_dnk(f"Ошибка: {e}")

    def rnk_to_dnk(self):
        seq = self.seq_input.get()
        try:
            dnk = dnk_calc.rnk_convertor_in_dnk(seq)
            self.out_dnk(f"ДНК: {dnk}")
        except Exception as e:
            self.out_dnk(f"Ошибка: {e}")

    def decode_dnk(self):
        seq = self.seq_input.get()
        try:
            result = dnk_calc.protein_search_for_dnk(seq)
            self.out_dnk(f"Аминокислоты:\n{result}")
        except Exception as e:
            self.out_dnk(f"Ошибка: {e}")

    def decode_rnk(self):
        seq = self.seq_input.get()
        try:
            result = dnk_calc.protein_search_for_rnk(seq)
            self.out_dnk(f"Аминокислоты:\n{result}")
        except Exception as e:
            self.out_dnk(f"Ошибка: {e}")

    # --- Функции Генетики ---
    def calc_genetic(self):
        p1 = self.parent1_input.get()
        p2 = self.parent2_input.get()
        m_status = self.mendel_var.get()
        
        self.gen_output.delete("0.0", "end")
        
        try:
            result = gen_calc.genetic_programme(p1, p2, m_status)
            if not result:
                self.gen_output.insert("end", "Произошла ошибка при вычислениях (проверьте ввод).")
                return

            # Форматируем вывод в зависимости от того, что вернула функция
            output_str = "Результаты расчёта:\n" + "-"*30 + "\n"
            for i, item in enumerate(result):
                output_str += f"[{i+1}]:\n{item}\n\n"
                
            self.gen_output.insert("end", output_str)
        except Exception as e:
            self.gen_output.insert("end", f"Ошибка: {e}")


if __name__ == "__main__":
    app = App()
    app.mainloop()