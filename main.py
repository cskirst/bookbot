from stats import count_words, character_count, sort_characters
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath, 'r') as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    contents = get_book_text(book)
    num_words = count_words(contents)
    print(f"{num_words} words found in the document")
    sorted = sort_characters(character_count(contents))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")


if __name__ == "__main__":
    main()