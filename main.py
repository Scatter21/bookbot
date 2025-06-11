from stats import *
import sys


def get_book_text(path_to_file):
        with open(path_to_file) as f:
            return f.read()

    
def main():
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    words = count_words(text)
    dic = char_counter(text)
    sort_dic = dic_sorter(dic)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count -----------")
    print(f"Found {words} total words")
    print("--------- Character Count ---------")
    for item in sort_dic:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END =============")
    
    
    
    

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main()