from stats import get_word_count
from stats import get_character_count
from stats import clean_dictionary
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    text = get_book_text(file_path)

    word_count = get_word_count(text)

    character_count = get_character_count(text)

    sorted_list = clean_dictionary(character_count)
    
    print("=====BOOKBOT=====")
    print(f"After analysing the book found at {file_path}\n")
    print("-----Word Count-----")
    print(f"Found {word_count} total words\n")
    print("-----Character Counts-----")
    
    for dictionary in sorted_list:
        if dictionary["char"] == "\n":
            continue
        elif dictionary["char"] == " ":
            print(f"<space>: {dictionary['num']}")
            continue

        print(f"{dictionary['char']}: {dictionary['num']}")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

main()
