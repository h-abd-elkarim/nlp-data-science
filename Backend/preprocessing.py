import gzip
import xml.etree.ElementTree as ET
import spacy
from nltk import Tree


try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import spacy.cli

    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def decompress_gz(xml_file):
    """Décompresse un fichier .gz."""
    if xml_file.endswith(".gz"):
        print("Décompression du fichier en cours...")
        with gzip.open(xml_file, 'rb') as f_in:
            decompressed_path = xml_file[:-3]
            with open(decompressed_path, 'wb') as f_out:
                f_out.write(f_in.read())
        print(f"Fichier décompressé : {decompressed_path}")
        return decompressed_path
    return xml_file


def extract_abstracts(xml_file, limit=15):
    """Extrait les 15 premiers abstracts du fichier XML."""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    abstracts = []
    count = 0
    for abstract in root.iter("AbstractText"):
        if abstract.text:
            abstracts.append(abstract.text.strip())
            count += 1
        if count >= limit:
            break

    return abstracts


def generate_parse_tree(sentence):
    """Génère l'arbre syntaxique d'une phrase."""
    doc = nlp(sentence)

    def token_to_nltk_tree(token):
        """Convertit un token spaCy en sous-arbre nltk."""
        if token.n_lefts + token.n_rights > 0:
            return Tree(token.orth_, [token_to_nltk_tree(child) for child in token.children])
        else:
            return token.orth_

    return token_to_nltk_tree(doc.root)


# Spécifie le chemin du fichier XML
xml_path = "C:/Users/user/Downloads/sample-0001.xml.gz"
xml_file = decompress_gz(xml_path)

# Extraire les 15 premiers abstracts
abstracts = extract_abstracts(xml_file, limit=15)

# Afficher les analyses morphosyntaxiques
print(f"Extraits des {len(abstracts)} premiers abstracts avec analyse morphosyntaxique :")

for i, abstract in enumerate(abstracts, 1):
    print(f"\nAbstract {i} : {abstract}")

    # Segmenter en phrases
    doc = nlp(abstract)
    sentences = list(doc.sents)

    for j, sentence in enumerate(sentences[:3], 1):
        print(f"\n--- Phrase {j} ---\n{sentence.text}")

        # Générer et afficher l'arbre syntaxique
        parse_tree = generate_parse_tree(sentence.text)
        parse_tree.pretty_print()
