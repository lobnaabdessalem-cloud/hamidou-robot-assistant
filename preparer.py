import json
import random
import re

FICHIER = "TT.txt"

SYSTEM = (
    "Tu es Hamidou, un robot assistant et accompagnant créé par Ranim, Lobna "
    "et Amenallah à l'ISIMa (Mahdia, Tunisie). Tu parles derja tunisienne, "
    "arabe et français, dans la langue de la personne. Tes réponses sont "
    "courtes et claires, sans liste ni emoji. Tu ne promets jamais ce que "
    "tu ne sais pas faire."
)

def nettoyer(texte):
    texte = re.sub(r"\s+", " ", texte).strip()          # espaces en trop
    texte = re.sub(r"\s+([,.!?؟،])", r"\1", texte)      # espace avant ponctuation
    for nom in ["Ranim", "Lobna", "Amenallah"]:         # noms propres
        texte = re.sub(nom, nom, texte, flags=re.IGNORECASE)
    return texte

# 1. Lire le fichier
exemples = []
question = None
with open(FICHIER, encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()
        if ligne.startswith("Question:"):
            question = nettoyer(ligne[len("Question:"):])
        elif ligne.startswith("Réponse:") and question:
            reponse = nettoyer(ligne[len("Réponse:"):])
            if question and reponse:
                exemples.append((question, reponse))
            question = None

# 2. Vérifications
mots_a_surveiller = ["rappellerai", "نذكرك", "سأذكرك", "nedhakrek"]
for q, r in exemples:
    if any(m in r for m in mots_a_surveiller):
        print("ATTENTION, promesse de rappel :", q, "->", r)
    if len(r) > 200:
        print("ATTENTION, réponse trop longue :", q)

# 3. Supprimer les doublons de questions
vus = set()
uniques = []
for q, r in exemples:
    if q not in vus:
        vus.add(q)
        uniques.append((q, r))
exemples = uniques

# 4. Mélanger et séparer : 90% entraînement, 10% test
random.seed(42)
random.shuffle(exemples)
n_test = 1
test = exemples[:n_test]
train = exemples[n_test:]

def ecrire(nom, liste):
    with open(nom, "w", encoding="utf-8") as f:
        for q, r in liste:
            ligne = {"messages": [
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": q},
                {"role": "assistant", "content": r},
            ]}
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n")

ecrire("train.jsonl", train)
ecrire("test.jsonl", test)

print(f"Total : {len(exemples)} exemples")
print(f"Entraînement : {len(train)} | Test : {len(test)}")
print("Fichiers créés : train.jsonl et test.jsonl")