# NLP & Data Science — Classification de textes et modèles prédictifs

Projets d'analyse de données et de traitement du langage naturel réalisés en Master Sciences des Données & NLP (2024-2025).

## Contenu

### Application NLP (Backend / Frontend)
Application de traitement de texte avec API Python :
- `Backend/preprocessing.py` — nettoyage et préparation des textes
- `Backend/nlp_tasks.py` — tâches NLP (tokenisation, vectorisation, classification)
- `Backend/api.py` — exposition des traitements via API
- `Frontend/app.py` — interface utilisateur

### Notebooks
| Notebook | Sujet |
|----------|-------|
| `classification-20newsgroups.ipynb` | Classification de 18 000 articles (20 Newsgroups) : nettoyage, TF-IDF, K-NN, analyse des métriques (précision, rappel, F1) |
| `prediction-diabete.ipynb` | Modèle prédictif sur données médicales réelles (scikit-learn) |
| `reconnaissance-chiffres-manuscrits.ipynb` | Reconnaissance de chiffres manuscrits par apprentissage supervisé |

## Stack
Python · pandas · NumPy · scikit-learn · NLTK · Matplotlib

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r Data/requirements.txt
python main.py
```


