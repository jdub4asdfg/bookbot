def get_word_count(text):
    count = 0
    list_of_words = text.split()

    for word in list_of_words:
        count += 1

    return count

def get_character_count(text):
    character_count = {}
    lower_text = text.lower()
    
    for character in lower_text:
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1

    return character_count
