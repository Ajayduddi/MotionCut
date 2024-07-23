def count_words(sentence):
    """
    Counts the number of words in the input sentence.

    Args:
        sentence (str): The input sentence or paragraph.

    Returns:
        int: The total number of words.
    """
    # Split the sentence into words using whitespace as the delimiter
    words = sentence.split()

    # Return the count of words
    return len(words)

def main():
    print("Welcome to the Word Count Program!")
    user_input = input("Please enter a sentence or paragraph: ")

    # Check for empty input
    if not user_input.strip():
        print("Error: Empty input. Please enter some text.")
        return

    # Calculate word count
    word_count = count_words(user_input)
    print(f"Word count: {word_count}")

if __name__ == "__main__":
    main()

