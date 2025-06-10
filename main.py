from stats import *
import sys

if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
script_name = sys.argv[0]
bookpath = str(sys.argv[1])

def get_book_text(path_to_file):
    file_contens = None
    with open(path_to_file) as f:
        file_contens = f.read()

    return file_contens

def main():
    #bookpath = "books/frankenstein.txt"
    text = get_book_text(bookpath)
    chars = get_char_list(get_char_count(text))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_words_count(text)} total words")
    print("--------- Character Count -------")
    for char in chars:
        print (f"{char['name']}: {char['num']}")
    print("============= END ===============")

    get_char_list(get_char_count(text))

#### Run

main()