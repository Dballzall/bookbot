def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}

    text = text.lower()

    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def print_report(word_count, character_counts, path_to_file):
    sorted_chars = sorted(character_counts.items(), key=lambda x: x[1], reverse=True)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")

    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")

    print(f"--- End report ---")


def main():
    path_to_file = 'books/frankenstein.txt'

    with open(path_to_file, 'r') as f:
        file_contents = f.read()

        word_count = count_words(file_contents)
        
        character_counts = count_characters(file_contents)

        print_report(word_count, character_counts, path_to_file)


if __name__ == "__main__":
    main() 