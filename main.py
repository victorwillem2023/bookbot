from stats import number_of_words, char_occurences, sort_char_occurences
import sys
def get_book_text(file_path):
    with open (file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_content = get_book_text(sys.argv[1])
        letter_list = sort_char_occurences(char_occurences(book_content))

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(number_of_words(book_content))
        print("--------- Character Count -------")
        for letter in letter_list:
            if letter["char"].isalpha() == True:
                print(f"{letter['char']}: {letter['num']}")
        print("============= END ===============")

if __name__ == "__main__":
    main()
