from GeneticAlgorithm import GeneticAlgorithm
import matplotlib.pyplot as plt
import tkinter as tk
from AppGui import AppGui



def run_test():
    # To jest nasz słownik konfiguracyjny - odpowiednik tego, co potem wpiszesz w GUI
    config = {
        'n_vars': 27,  # Twoje legendarne N=27
        'bits_per_var': 20,  # Precyzja (m)
        'pop_size': 100,  # Wielkość populacji
        'epochs': 800,  # Liczba pokoleń
        'range_min': -5.0,  # Zakres Styblinski-Tang
        'range_max': 5.0,
        'prob_cross': 0.8,  # Szansa na krzyżowanie (80%)
        'prob_mut': 0.05,  # Szansa na mutację (5%)
        'prob_inv': 0.01,  # Szansa na inwersję (1%)
        'elite_count': 2,  # Strategia elitarna (2 najlepszych przechodzi)
        'selection_method': "Tournament",
        'tournament_size': 3,
        'crossover_method': "Single-Point",
        'mutation_method': "One-Point"
    }

    print("Uruchamiam Algorytm Genetyczny...")
    print(f"Szukanie minimum funkcji Styblinski-Tang dla N={config['n_vars']} zmiennych.")

    # Inicjalizacja silnika
    ga = GeneticAlgorithm(config)

    # Uruchomienie ewolucji
    history = ga.run()

    print("\nOptymalizacja zakończona!")
    print(f"Najlepszy znaleziony wynik: {history[-1]}")

    # Wyświetlenie wykresu zbieżności
    plt.figure(figsize=(10, 6))
    plt.plot(history, label='Best Fitness')
    plt.title(f"Zbieżność algorytmu dla N={config['n_vars']}")
    plt.xlabel("Epoka")
    plt.ylabel("Wartość funkcji celu")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = AppGui(root)
    root.mainloop()