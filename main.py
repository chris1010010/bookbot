import sys
from stats import get_book_text
from stats import count_words
from stats import get_char_stats
from stats import sort_char_stats

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    content = get_book_text(filepath)
    word_count = count_words(content)
    char_stats = get_char_stats(content)
    sorted_stats = sort_char_stats(char_stats)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for item in sorted_stats:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()
