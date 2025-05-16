def get_word_count(text):
    count = 0

    # Splitting the words into a list
    list_of_words = text.split()

    # Counting all words in the list
    for word in list_of_words:
        count += 1

    return count

def get_character_count(text):
    character_count = {}
    lower_text = text.lower()
    
    # Counting all characters in text and adding them into a dictionary
    for character in lower_text:
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1

    return character_count

def clean_dictionary(character_count):
    # Sorting the characters by count from largest to smallest
    sorted_list = list()

    sorted_character_count = dict(sorted(character_count.items(), key = lambda item: item[1], reverse = True))
    for key, value in sorted_character_count.items():
            dictionary = {}
            dictionary["char"] = key
            dictionary["num"] = value
            sorted_list.append(dictionary)
    
    return sorted_list
