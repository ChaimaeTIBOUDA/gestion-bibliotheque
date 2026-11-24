
import json


def sauvegarder_json(bibliotheque, chemin):
    """Écrit le catalogue dans un fichier JSON."""

    livres_data = [vars(livre) for livre in bibliotheque.livres]

    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(livres_data, fichier, ensure_ascii=False, indent=4)


def charger_json(chemin):
    """Charge le catalogue depuis un fichier JSON."""

    with open(chemin, "r", encoding="utf-8") as fichier:
        return json.load(fichier)
