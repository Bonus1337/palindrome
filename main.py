import re

def is_palindrome(word: str) -> bool:
    """
    Checks if the given string is a palindrome.
    
    This version uses string methods:
      - Converts the string to lowercase.
      - Removes non-alphanumeric characters (e.g., spaces, punctuation).
      - Checks if the filtered string reads the same backward.
    
    Arguments:
        word (str): The string to check.
    
    Returns:
        bool: True if 'word' is a palindrome, otherwise False.
    """
    word = word.lower()
    filtered = "".join(c for c in word if c.isalnum())
    return filtered == filtered[::-1]

def is_palindrome_regex(word: str) -> bool:
    """
    Checks if the given string is a palindrome using regular expressions.
    
    Method:
      - Converts the string to lowercase.
      - Uses a regular expression to remove all non-alphanumeric characters.
      - Checks if the filtered string reads the same backward.
    
    Arguments:
        word (str): The string to check.
    
    Returns:
        bool: True if 'word' is a palindrome, otherwise False.
    """
    word = word.lower()
    filtered = re.sub(r'[\W_]', '', word)
    return filtered == filtered[::-1]

if __name__ == '__main__':
    print("is_palindrome:")
    print(is_palindrome("kayak"))                           
    print(is_palindrome("Python"))                          
    print(is_palindrome("A man, a plan, a canal, Panama"))  

    print("\nis_palindrome_regex:")
    print(is_palindrome_regex("kayak"))                           
    print(is_palindrome_regex("Python"))                          
    print(is_palindrome_regex("A man, a plan, a canal, Panama"))  

    assert is_palindrome("kayak") == True
    assert is_palindrome("test") == False
    assert is_palindrome("No 'x' in Nixon") == True
    assert is_palindrome_regex("No 'x' in Nixon") == True

    print("\nAll tests passed successfully.")