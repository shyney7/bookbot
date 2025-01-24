def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    report(num_chars, num_words)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_chars(text):
    char_count = {}
    for c in text:
        if c.lower() in char_count:
            char_count[c.lower()] += 1
        else:
            char_count[c.lower()] = 1
    return sorted(char_count.items(),key=lambda x: int(x[1]), reverse=True)

def report(sorted_char_count, num_words):
    print("--- Begin report of book books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for c in sorted_char_count:
        k, v = c
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")
    print("--- End report ---")


main()