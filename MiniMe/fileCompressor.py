from typing import AnyStr

class FileCompressor:

    def __init__(self, file: AnyStr, path: str):
        self.file: bytes = file
        self.path = path
        print(file)
        print(len(file))
        print(file.decode('utf-8'))

"""
b'coucou mon b\xc3\xa9b\xc3\xa9 ! \xf0\x9f\x98\x8a'
24
coucou mon bébé ! 😊

Voici un exemple d'un texte d'abbord convertis en ASCII (première ligne) suivit du nombre d'octets que prend cette ligne.
La dernière représente la même ligne converti en utf-8.

Le principe est le suivant : tous les caractères de l'alphabet latin + les nombres et certains caractères ne prennent que 1 octet pour être stocké.
Chaque caractère prenant plus de 1 octet sera enlever et stocké dans un dictionnaire avec les positions de celui-ci dans le texte.

PROBLEME : prend plus de place pour stocké les positions que de laisser le caractère en place (si le nombre dépasse ou est égale au nombre d'octet de celui-ci)
"""

