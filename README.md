# Hamidou : robot assistant et accompagnant en derja, arabe et français

## Objectif
Créer un assistant IA pour un robot (Raspberry Pi 5) qui dialogue en derja
tunisienne, arabe et français. Projet de l'ISIMa (Institut Supérieur
d'Informatique de Mahdia).

## Équipe
Ranim, Lobna, Amenallah

## Méthode
- Modèle de base : Qwen2.5-3B-Instruct
- Fine-tuning LoRA avec Unsloth sur Google Colab (GPU T4)
- Données : ~200 exemples question/réponse écrits à la main
  (derja en lettres latines et arabes, arabe, français)
- Export en GGUF, exécution avec Ollama

## Contenu du dépôt
- `TT.txt` : données brutes
- `preparer.py` : convertit TT.txt en train.jsonl / test.jsonl
- `hamidou.ipynb` : notebook d'entraînement
- `Modelfile` : configuration Ollama

## Utilisation
1. `python preparer.py`
2. Entraîner avec `hamidou.ipynb` sur Colab
3. Placer le `.gguf` à côté du Modelfile
4. `ollama create hamidou -f Modelfile` puis `ollama run hamidou`

## Résultats
| Test | Avant fine-tuning | Après |
|---|---|---|
| Qui t'a créé ? | Alibaba Cloud | Ranim, Lobna et Amenallah |
| شنوة اسمك ؟ | محمود | اسمي حميدو |

## Limites
Peu de données : le modèle généralise mal sur des phrases de derja
jamais vues. Amélioration prévue : plus d'exemples et équilibrage.

## Modèle
Fichier GGUF (trop gros pour GitHub) : [lien à ajouter]
