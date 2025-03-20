# Palindrome Checker

## Overview
This project provides two implementations for checking if a given string is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backward as forward, ignoring case and non-alphanumeric characters.

## Features
- **`is_palindrome`**: Uses string methods to filter out non-alphanumeric characters and checks for palindromes.
- **`is_palindrome_regex`**: Uses regular expressions to filter out non-alphanumeric characters before checking for palindromes.
- Includes test cases to validate the correctness of both implementations.

## Installation
1. Clone this repository:
   ```sh
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```sh
   cd palindrome_checker
   ```
3. Ensure you have Python installed (version 3.x recommended).

## Usage
Run the script to test the palindrome functions:
```sh
python palindrome_checker.py
```

## Example Usage
```python
from palindrome_checker import is_palindrome, is_palindrome_regex

print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome_regex("No 'x' in Nixon"))           # True
```

## Tests
The script includes assertions to verify correctness:
```python
assert is_palindrome("kayak") == True
assert is_palindrome("test") == False
assert is_palindrome("No 'x' in Nixon") == True
assert is_palindrome_regex("No 'x' in Nixon") == True
```

If all tests pass, the script prints:
```
All tests passed successfully.
```

## License
This project is open-source and available under the MIT License.

## Contributions
Feel free to submit issues or contribute by creating pull requests.

