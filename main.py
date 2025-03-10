def is_palindrome(word: str) -> bool:
    """
    Sprawdza, czy podany wyraz jest palindromem.

    Palindrom to słowo, które czytane od lewej do prawej i od prawej do lewej jest takie samo.
    
    Argumenty:
        word (str): Słowo do sprawdzenia.
    
    Zwraca:
        bool: True, jeśli 'word' jest palindromem, w przeciwnym razie False.
    
    Przykłady:
        is_palindrome("kajak") -> True
        is_palindrome("potop") -> True
        is_palindrome("python") -> False
    """
    word = word.lower()
    return word == word[::-1]

print(is_palindrome("kajak")) # True
print(is_palindrome("python")) # False