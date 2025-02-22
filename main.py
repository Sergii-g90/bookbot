from stats import word_count, character_count

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    
    print(f"{word_count(file_contents)} words found in the document")
    print(character_count(file_contents))

main()