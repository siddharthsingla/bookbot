def main():
    filename = "books/frankenstein.txt"
    text = get_text(filename)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document \n\n")
    for char, count in char_count.items():
        print(f"The \'{char}\' character was found {count} times")
    print("--- End report ---")
def get_char_count(text):
    char_count = {}
    for char in text.strip():
        try:
            char = char.lower()
        except:
            pass
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def get_word_count(text):
    words = text.strip().split()
    return len(words)

def get_text(filename):
    with open(filename, "r") as f:
        return f.read()

main()
