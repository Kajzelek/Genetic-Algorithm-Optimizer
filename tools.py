import numpy as np
import matplotlib.pyplot as plt
import datetime


def save_report(config, best_ind, filename="raport_sga.txt"):
    try:
        decoded_values = best_ind.decode()

        with open(filename, "w", encoding="utf-8") as f:
            f.write("==========================================\n")
            f.write("   RAPORT OPTYMALIZACJI GENETYCZNEJ (SGA) \n")
            f.write(f"   Data: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("==========================================\n\n")

            f.write("--- KONFIGURACJA ---\n")
            f.write(f"Liczba zmiennych (N): {config['n_vars']}\n")
            f.write(f"Wielkość populacji:   {config['pop_size']}\n")
            f.write(f"Liczba epok:          {config['epochs']}\n")
            f.write(f"Metoda selekcji:      {config['selection_method']}\n")
            f.write(f"Metoda krzyżowania:   {config['crossover_method']}\n")
            f.write(f"Prawd. Mutacji:       {config['prob_mut']}\n")
            f.write("-" * 42 + "\n\n")

            f.write("--- WYNIK KOŃCOWY ---\n")
            f.write(f"Najlepszy Fitness: {best_ind.fitness:.6f}\n\n")

            f.write("--- ZDEKODOWANE WARTOŚCI ZMIENNYCH (X) ---\n")
            for i, val in enumerate(decoded_values):
                f.write(f" x{i + 1:02}: {val:>10.6f}\n")

            f.write("\n==========================================\n")

        print(f"Pomyślnie zapisano raport w: {filename}")
        return True
    except Exception as e:
        print(f"Błąd podczas zapisu raportu: {e}")
        return False

def show_heatmap(best_x, best_y):

    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)


    Z = ((X ** 4 - 16 * X ** 2 + 5 * X) + (Y ** 4 - 16 * Y ** 2 + 5 * Y)) / 2

    plt.figure(figsize=(8, 6))
    cp = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar(cp, label='Fitness')


    plt.plot(best_x, best_y, 'r*', markersize=15, label='Znalezione Minimum')
    plt.title("Mapa cieplna Styblinski-Tang (N=2)")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.legend()
    plt.show()