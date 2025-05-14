from stats import get_word_count
from stats import get_character_count
from stats import clean_dictionary

def main():
    file_path = "/home/jdubs/projects/github/bookbot/books/frankenstein.txt"

    text = get_book_text(file_path)

    word_count = get_word_count(text)

    character_count = get_character_count(text)

    sorted_list = clean_dictionary(character_count)
    
    print("=====BOOKBOT=====")
    print(f"After analysing the book found at {file_path}\n")
    print("-----Word Count-----")
    print(f"Found {word_count} total words")
    print("-----Character Counts-----")
    
    for dictionary in sorted_list:
        if dictionary["char"] == "\n" or dictionary["char"] == " ":
            continue
        print(f"{dictionary['char']}: {dictionary['num']}")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

main()
