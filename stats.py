def word_count(text):
    words = text.split()
    return len(words)


def character_count(text):
    unique_chars = set(text.lower())
    chars_count = dict()
    for char in unique_chars:
        chars_count[char] = text.lower().count(char)

    return chars_count


def sorted_list_of_chars(dict_of_chars):
    return sorted(dict_of_chars.items(), key=lambda x: x[1], reverse=True)