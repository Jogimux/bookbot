def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    
    total_words = countwords(text)
    print(f"Word count: {total_words}")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def countwords(text):
    words = text.split()
    wordcount = len(words)
    return wordcount



main()
