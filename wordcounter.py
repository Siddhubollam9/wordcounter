def count_words(text):
    """
    Counts the number of words in the given text.
    :param text: Input string
    :return: Integer count of words
    """
    words = text.split()
    return len(words)

def main():
    print("Welcome to the Word Counter Program!")
    while True:
        # Prompt user for input
        user_input = input("Please enter a sentence or paragraph (or type 'exit' to quit): ").strip()
        # Exit condition
        if user_input.lower() == 'exit':
            print("Thank you for using the Word Counter Program")
            break
        # Error handling for empty input
        if not user_input:
            print("Error: Input cannot be empty. Please try again.")
            continue
        # Count words and display the result
        word_count = count_words(user_input)
        print(f"The input contains {word_count} words.\n")

if __name__ == "__main__":
    main()
