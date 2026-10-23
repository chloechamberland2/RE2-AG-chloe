# Outil de diagnostic réseau

Ce projet est un script Python qui permet de tester plusieurs aspects de la connectivité réseau à partir d'un menu interactif.

## Fonctionnalités

- Ping vers une adresse IP ou un nom de domaine
- Résolution DNS
- Traceroute
- Test d'ouverture d'un port TCP
- Affichage des informations réseau locales

## Prérequis

- Python 3 installé sur la machine
- Système Windows (pour utiliser `ping` et `tracert`)

## Utilisation

1. Ouvrir un terminal dans le dossier du projet.
2. Exécuter la commande suivante :

```bash
python diagnostic.py
```

3. Choisir une option dans le menu.
4. Entrer la cible ou le port demandé.

## Exemple

```text
1. Ping
2. Résolution DNS
3. Traceroute
4. Test de port TCP
5. Informations réseau locales
6. Quitter
```

## Notes

- Le script utilise les bibliothèques `subprocess` et `socket` de Python.
- Les commandes `ping` et `tracert` sont spécifiques à Windows.
- Les erreurs de résolution DNS ou de connexion sont gérées pour éviter un arrêt brut du programme.
