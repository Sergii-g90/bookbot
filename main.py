from stats import word_count, character_count, sorted_list_of_chars

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(file_contents)} total words")
    print("--------- Character Count -------")
    for item in sorted_list_of_chars(character_count(file_contents)):
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
    print("============= END ===============")

main()