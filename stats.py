def number_of_words(book_content):
    number_of_words = 0
    for words in book_content.split():
        number_of_words += 1
    return f"Found {number_of_words} total words"

def char_occurences(book_content):
    char_dict = {}
    for char in book_content:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_char_occurences(char_dict):
    sorted_chars = []
    for char in char_dict:
        sorted_chars.append(
            {
                "char": char, 
                "num": char_dict[char]
            }
        )
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars

    
