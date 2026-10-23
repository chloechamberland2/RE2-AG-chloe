# diagnostic.py

import subprocess
import os
import socket

def pause():
    input("\nAppuyez sur Entrée pour continuer...")

def clear():
    os.system("cls")

# Fonction Ping
def ping():

    cible = input("Entrez une adresse IP ou un nom de domaine : ")

    if not cible:
        print("Veuillez entrer une valeur.")
        return

    try:
        resultat = subprocess.run(["ping", "-n", "4", cible],capture_output=True,text=True, timeout=10)
        print(resultat.stdout)

    except Exception as erreur:
        print("Erreur :", erreur)

# Fonction Résolution DNS
def dns_lookup():

    domaine = input("Entrez un nom de domaine : ")

    if not domaine:
        print("Veuillez entrer une valeur.")
        return

    try:
        ip = socket.gethostbyname(domaine)

        print(f"\nAdresse IP trouvée : {ip}")

    except socket.gaierror:
        print("Impossible de résoudre ce domaine.")


# Fonction Traceroute
def traceroute():

    cible = input("Entrez une adresse IP ou un nom de domaine : ")

    if not cible:
        print("Veuillez entrer une valeur.")
        return

    try:
        resultat = subprocess.run(["tracert", cible],capture_output=True,text=True,timeout=30)
        print(resultat.stdout)

    except Exception as erreur:
        print("Erreur :", erreur)

# Fonction Test Port TCP
def test_port():

    hote = input("Entrez une adresse IP ou un nom de domaine : ")

    if not hote:
        print("Veuillez entrer une valeur.")
        return

    try:
        port = int(input("Entrez le numéro du port : "))

        if port < 1 or port > 65535:
            print("Le port doit être compris entre 1 et 65535.")
            return
    except ValueError:
        print("Veuillez entrer un numéro valide.")
        return

    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion.settimeout(3)

    try:

        resultat = connexion.connect_ex((hote, port))

        if resultat == 0:
            print(f"Le port {port} est ouvert.")
        else:
            print(f"Le port {port} est fermé.")

    except socket.gaierror:
        print("Nom d'hôte invalide.")

    finally:
        connexion.close()

# Informations réseau locales
def infos_reseau():

    resultat = subprocess.run(["ipconfig", "/all"],capture_output=True,text=True)

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
        clear()
        afficher_menu()

        choix = input("\nVeuillez entrer le numéro de votre choix : ").strip()

        match choix:

            case "1":
                print("\n----- RÉSULTAT DU PING -----")
                ping()
                pause()

            case "2":
                print("\n----- RÉSOLUTION DNS -----")
                dns_lookup()
                pause()
            case "3":
                print("\n----- TRACEROUTE -----")
                traceroute()
                pause()

            case "4":
                print("\n----- TEST PORT -----")
                test_port()
                pause()

            case "5":
                print("\n----- INFO RÉSEAU -----")
                infos_reseau()
                pause()

            case "6":
                print("Au revoir !")
                break

            case _:
                print("Choix invalide.")
                


# Programme principal
if __name__ == "__main__":
    menu_principal()