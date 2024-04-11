def get_text(path):
    with open(path, "r") as f:
        print(f"Reading {path}")
        return f.read()


def num_words(text):
    words = text.split(" ")
    return len(words)


def count_letters(text):
    map = {}
    letters = "qwertyuiopasdfghjklzxcvbnm"
    for let in text.lower():
        if let not in letters:
            continue
        if let not in map:
            map[let] = 1
        else:
            map[let] += 1
    return map


def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = num_words(text)
    letter_count = count_letters(text)

    print(f"Frankenstein has {word_count} words")
    print(f"Here is the word map for Frankenstein\n")
    for x in letter_count:
        print(f"{x}: {letter_count[x]}")


if __name__ == "__main__":
    main()
