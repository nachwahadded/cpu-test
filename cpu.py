import psutil
import time
import matplotlib.pyplot as plt

# Initialisation des listes pour stocker les données
temps = []
utilisation_cpu_par_coeur = [[] for _ in range(psutil.cpu_count())]
utilisation_memoire = []

plt.ion()  # Activer le mode interactif

def afficher_infos_systeme():
    global temps

    # Obtenez les informations sur l'utilisation du CPU
    utilisation_cpu = psutil.cpu_percent(interval=1, percpu=True)
    for i, usage in enumerate(utilisation_cpu):
        utilisation_cpu_par_coeur[i].append(usage)

    # Obtenez les informations sur l'utilisation de la mémoire
    memoire = psutil.virtual_memory()
    utilisation_memoire.append(memoire.percent)

    # Enregistrez le temps actuel
    temps.append(time.time())

    # Affichez les informations sur la console
    print(f"Utilisation du CPU par cœur: {utilisation_cpu}")
    print(f"Utilisation de la mémoire totale: {memoire.total / (1024 ** 3):.2f} Go")
    print(f"Utilisation de la mémoire disponible: {memoire.available / (1024 ** 3):.2f} Go")

def afficher_graphes():
    # Affichez le graphe d'utilisation du CPU par cœur
    plt.figure(1)
    plt.clf()
    for i, usage in enumerate(utilisation_cpu_par_coeur):
        plt.plot(temps, usage, label=f"Core {i}")

    plt.xlabel("Temps (s)")
    plt.ylabel("Utilisation du CPU (%)")
    plt.legend()
    plt.title("Utilisation du CPU par cœur")

    # Affichez le graphe d'utilisation de la mémoire
    plt.figure(2)
    plt.clf()
    plt.plot(temps, utilisation_memoire, label="Mémoire")
    plt.xlabel("Temps (s)")
    plt.ylabel("Utilisation de la mémoire (%)")
    plt.legend()
    plt.title("Utilisation de la mémoire")

    # Mettez à jour les graphes en temps réel
    plt.pause(0.1)

if __name__ == "__main__":
    try:
        while True:
            afficher_infos_systeme()
            afficher_graphes()
            time.sleep(5)  # Mettez à jour toutes les 5 secondes (vous pouvez ajuster cela selon vos besoins)
    except KeyboardInterrupt:
        print("Arrêt du programme.")

