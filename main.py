from stats import get_num_words, character_count, sorted_character_count
import sys

def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #path_and_file = "books/frankenstein.txt"
    path_and_file = sys.argv[1]
    book = get_book_text(path_and_file)
    #print(book)
    #list_of_words = book.split()
    num_words = get_num_words(book)
   # print (f"{num_words} words found in the document")

    chars = character_count(book)
    #for k, v in chars.items():
    #    print(f"'{k}': {v}")

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_and_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    my_list = sorted_character_count(chars)
    for c in my_list:
        #print(c)
        if c["char"].isalpha():
            print(f"{c['char']}: {c['num']}")

    print("============= END ===============")


if __name__ == '__main__':
    main()
