# diagnostic.py

import subprocess
import socket

# Fonction Ping
def ping():

    cible = input("Entrez une adresse IP ou un nom de domaine : ")

    resultat = subprocess.run(
        ["ping", "-n", "4", cible],
        capture_output=True,
        text=True
    )

    print(resultat.stdout)


# Fonction Résolution DNS
def dns_lookup():

    domaine = input("Entrez un nom de domaine : ")

    try:
        ip = socket.gethostbyname(domaine)

        print(f"\nAdresse IP trouvée : {ip}")

    except socket.gaierror:
        print("Impossible de résoudre ce domaine.")


# Fonction Traceroute
def traceroute():

    cible = input("Entrez une adresse IP ou un nom de domaine : ")

    resultat = subprocess.run(
        ["tracert", cible],
        capture_output=True,
        text=True
    )

    print(resultat.stdout)


# Fonction Test Port TCP
def test_port():

    hote = input("Entrez une adresse IP ou un nom de domaine : ")
    port = int(input("Entrez le numéro du port : "))

    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion.settimeout(3)

    resultat = connexion.connect_ex((hote, port))

    if resultat == 0:
        print(f"Le port {port} est ouvert.")
    else:
        print(f"Le port {port} est fermé.")

    connexion.close()


# Informations réseau locales
def infos_reseau():

    resultat = subprocess.run(
        ["ipconfig", "/all"],
        capture_output=True,
        text=True
    )

    print(resultat.stdout)


# Affichage du menu
def afficher_menu():

    print("\n------------------ OUTIL DE DIAGNOSTIC RÉSEAU ------------------")
    print("1. Ping")
    print("2. Résolution DNS")
    print("3. Traceroute")
    print("4. Test de port TCP")
    print("5. Informations réseau locales")
    print("6. Quitter")


# Menu principal
def menu_principal():

    while True:

        afficher_menu()

        choix = input("\nVeuillez entrer le numéro de votre choix : ")

        match choix:

            case "1":
                ping()

            case "2":
                dns_lookup()

            case "3":
                traceroute()

            case "4":
                test_port()

            case "5":
                infos_reseau()

            case "6":
                print("Au revoir !")
                break

            case _:
                print("Choix invalide.")


# Programme principal
if __name__ == "__main__":
    menu_principal()