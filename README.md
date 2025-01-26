Word Counter Program
This is a simple Python script that counts the number of words in a given text input. The program provides a user-friendly interface for counting words in sentences or paragraphs and handles basic error checking.

## Features
- Counts the number of words in user-provided input.
- Handles empty input gracefully with error messages.
- Allows users to exit the program by typing "exit".

## How to Use
1. Clone this repository or download the `wordcounter.py` file.
2. Open your terminal or command prompt.
3. Navigate to the directory where `wordcounter.py` is located.
4. Run the script using Python:
   ```
   python wordcounter.py
   ```
5. Follow the on-screen prompts:
   - Enter a sentence or paragraph when prompted.
   - View the word count result.
   - Type `exit` to quit the program.

## Example Usage
Welcome to the Word Counter Program!
Please enter a sentence or paragraph (or type 'exit' to quit): This is an example sentence.
The input contains 5 words.
Please enter a sentence or paragraph (or type 'exit' to quit): exit
Thank you for using the Word Counter Program.

## Requirements
- Python 3.x

## File Overview
- `wordcounter.py`: This is the main script that includes the following:
  - A `count_words()` function to count words in a given text.
  - A `main()` function to interact with the user and provide a looping interface for multiple inputs.

## Functions

### `count_words(text: str) -> int`
Counts the number of words in the given text.
- Parameters: `text` (str) – Input text to count words from.
- Returns: `int` – Number of words in the text.

### `main()`
Handles user input, displays the word count, and provides a loop to continuously accept input. This function also gracefully handles empty input and offers an exit option.

License
This project is licensed under the MIT License. See the LICENSE file for details.
