def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())
    
def get_char_stats(text):
    char_counts = {}
    for c in text:
        lower = c.lower()
        if lower not in char_counts:
            char_counts[lower] = 1
        else:
            char_counts[lower] += 1
    return char_counts

def sort_on(items):
    return items["num"]

def sort_char_stats(stats):
    sorted = []
    for key in stats:
        sorted.append({"char": key, "num": stats[key]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted