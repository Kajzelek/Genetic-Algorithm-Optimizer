import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from GeneticAlgorithm import GeneticAlgorithm
import tools as tools


class AppGui:
    def __init__(self, root):
        self.root = root
        self.root.title("SGA Solver - Styblinski-Tang (N=27)")
        self.root.geometry("400x500")

        # Kontener na parametry
        frame = ttk.LabelFrame(root, text=" Parametry Algorytmu ", padding=10)
        frame.pack(padx=10, pady=10, fill="x")

        # --- Konfiguracja pól (Label, Zmienna, Domyślna wartość) ---
        self.params_inputs = {}

        # Lista parametrów do stworzenia w pętli dla porządku
        fields = [
            ("Liczba zmiennych (N):", "n_vars", "27"),
            ("Precyzja (bits):", "bits_per_var", "20"),
            ("Wielkość populacji:", "pop_size", "100"),
            ("Liczba epok:", "epochs", "100"),
            ("Prawd. krzyżowania (0-1):", "prob_cross", "0.8"),
            ("Prawd. mutacji (0-1):", "prob_mut", "0.05"),
            ("Prawd. inwersji (0-1):", "prob_inv", "0.01"),
            ("Liczba elity:", "elite_count", "2"),
            ("Rozmiar turnieju:", "tournament_size", "3")
        ]

        for i, (label_text, key, default) in enumerate(fields):
            ttk.Label(frame, text=label_text).grid(row=i, column=0, sticky="w", pady=2)
            entry = ttk.Entry(frame)
            entry.insert(0, default)
            entry.grid(row=i, column=1, sticky="e", pady=2)
            self.params_inputs[key] = entry

        # --- Rozwijane listy dla metod ---
        ttk.Label(frame, text="Metoda selekcji:").grid(row=9, column=0, sticky="w")
        self.combo_select = ttk.Combobox(frame, values=["Tournament", "Roulette", "Best"], state="readonly")
        self.combo_select.set("Tournament")
        self.combo_select.grid(row=9, column=1, pady=5)

        ttk.Label(frame, text="Metoda krzyżowania:").grid(row=10, column=0, sticky="w")
        self.combo_cross = ttk.Combobox(frame, values=["Single-Point", "Two-Point", "Uniform"], state="readonly")
        self.combo_cross.set("Single-Point")
        self.combo_cross.grid(row=10, column=1, pady=5)

        ttk.Label(frame, text="Metoda mutacji:").grid(row=11, column=0, sticky="w")
        self.combo_mutate = ttk.Combobox(frame, values=["One-Point", "Two-Point", "Edge"], state="readonly")
        self.combo_mutate.set("One-Point")
        self.combo_mutate.grid(row=11, column=1, pady=5)

        # --- Przycisk Start ---
        self.btn_run = ttk.Button(root, text="URUCHOM OPTYMALIZACJĘ", command=self.run_ga)
        self.btn_run.pack(pady=20)

    def get_config(self):
        """Zbiera dane z pól i tworzy słownik config."""
        try:
            config = {
                'n_vars': int(self.params_inputs['n_vars'].get()),
                'bits_per_var': int(self.params_inputs['bits_per_var'].get()),
                'pop_size': int(self.params_inputs['pop_size'].get()),
                'epochs': int(self.params_inputs['epochs'].get()),
                'range_min': -5.0,
                'range_max': 5.0,
                'prob_cross': float(self.params_inputs['prob_cross'].get()),
                'prob_mut': float(self.params_inputs['prob_mut'].get()),
                'prob_inv': float(self.params_inputs['prob_inv'].get()),
                'elite_count': int(self.params_inputs['elite_count'].get()),
                'selection_method': self.combo_select.get(),
                'tournament_size': int(self.params_inputs['tournament_size'].get()),
                'crossover_method': self.combo_cross.get(),
                'mutation_method': self.combo_mutate.get()
            }
            return config
        except ValueError:
            messagebox.showerror("Błąd", "Wprowadź poprawne liczby w polach parametrów!")
            return None

    def run_ga(self):
        config = self.get_config()
        if config:
            self.btn_run.state(['disabled'])  # Blokada przycisku na czas obliczeń

            # Uruchomienie algorytmu
            ga = GeneticAlgorithm(config)
            history, best_individual = ga.run()

            # Zapis raportu
            tools.save_report(config, best_individual)

            self.btn_run.state(['!disabled'])

            # Wyświetlenie wykresu
            self.show_plot(history, config['n_vars'])

            # #heatmapa
            # if config['n_vars'] == 2:
            #     decoded = best_ind.decode()
            #     tools.show_heatmap(decoded[0], decoded[1])
            #
            # self.btn_run.state(['!disabled'])
            # messagebox.showinfo("Sukces", f"Optymalizacja zakończona!\nWynik: {best_ind.fitness:.4f}\nRaport zapisany.")

    def show_plot(self, history, n):
        plt.figure("Wyniki Optymalizacji")
        plt.plot(history, color='blue', linewidth=2)
        plt.title(f"Zbieżność SGA dla N={n} (Styblinski-Tang)")
        plt.xlabel("Pokolenie")
        plt.ylabel("Najlepszy Fitness")
        plt.grid(True, linestyle='--')
        plt.show()


# --- Funkcja startowa ---
if __name__ == "__main__":
    root = tk.Tk()
    app = AppGui(root)
    root.mainloop()