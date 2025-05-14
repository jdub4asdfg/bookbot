from stats import get_word_count
from stats import get_character_count

def main():
    file_path = "/home/jdubs/projects/github/bookbot/books/frankenstein.txt"
    text = get_book_text(file_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    print(f"{word_count} words found in the document.")
    print(character_count)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


main()
