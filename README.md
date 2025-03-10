---

# Palindrome Checker

A lightweight Python utility to check if a given string is a palindrome. A palindrome is a word that reads the same forwards and backwards (e.g., "kajak", "potop").

## Overview

The `is_palindrome` function is designed to determine whether a provided string is a palindrome. It achieves this by converting the input string to lowercase (ensuring the check is case-insensitive) and comparing it with its reversed version using Python's slicing capabilities.

## Features

- **Case-Insensitive Check:** Automatically converts input to lowercase.
- **Concise Implementation:** Leverages Python's slicing for quick and clear reversal.
- **Comprehensive Documentation:** The function is thoroughly documented with a docstring explaining its usage, parameters, and return type.

## Prerequisites

- Python 3.6 or higher

## Installation

1. **Clone the repository:**

   ```bash
   git clone git@github.com:Bonus1337/palindrome.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd palindrome
   ```

## Usage

You can use the `is_palindrome` function directly in your Python projects. Below is an example of how to integrate and test the function:

```python
def is_palindrome(word: str) -> bool:
    """
    Determines whether the provided string is a palindrome.

    A palindrome is a word that reads the same forwards and backwards.

    Parameters:
        word (str): The string to evaluate.

    Returns:
        bool: True if 'word' is a palindrome, otherwise False.

    Examples:
        is_palindrome("kajak") -> True
        is_palindrome("potop") -> True
        is_palindrome("python") -> False
    """
    word = word.lower()
    return word == word[::-1]

if __name__ == "__main__":
    print(is_palindrome("kajak"))  # Expected output: True
    print(is_palindrome("python")) # Expected output: False
```

To run the script and see the output, execute:

```bash
python palindrome.py
```

## Contributing

Contributions to this project are welcome. If you wish to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch:  
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes with a clear description:  
   ```bash
   git commit -m "Add feature: description of your feature"
   ```
4. Push your branch to GitHub:  
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a pull request detailing your changes.

## License

This project is licensed under the MIT License. For more information, please refer to the [LICENSE](LICENSE) file.

## Contact

For questions, feedback, or further information, please contact.

---
