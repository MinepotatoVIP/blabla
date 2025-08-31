import random
import string

def charabia(n=32):
    """Génère une chaîne aléatoire de lettres (majuscules et minuscules) de longueur n."""
    return ''.join(random.choices(string.ascii_letters, k=n))
