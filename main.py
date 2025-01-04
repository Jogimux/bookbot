def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    total_words = count_words(text)
    letter_count = count_characters(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{total_words} words found in the document\n")
    
    for char in letter_count:
        print(f"The '{char['char']}' character was found {char['num']} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    wordcount = len(words)
    return wordcount

def sort_on(dict):
    return dict["num"]

def count_characters(text):
    characters = {}

    lowered_text = text.lower()

    for letters in lowered_text:
        if letters.isalpha():
            if letters in characters:
                characters[letters] += 1
            else:
                characters[letters] = 1

    chars_list = []
    for letter, count in characters.items():
        letter_dict = {"char":letter,"num":count}
        chars_list.append(letter_dict)
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list


main()
