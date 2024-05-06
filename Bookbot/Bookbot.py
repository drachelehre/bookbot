def word_count(document):
    count = 0
    for word in document:
        count += 1
    return count

def letter_count(document):
    letters = {}
    prepped_doc = document.lower()
    for char in prepped_doc:
        if char.isalpha():  # Consider only alphabetic characters
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1
    print_letters(letters)

def print_letters(dict):
    sorted_letters = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    for letter, count in sorted_letters:
        print(f"{letter} was found {count} times")

def main():
    with open("books/.gitignore/frankenstein.txt") as f:
        file_contents = f.read()
        wordNumber = word_count(file_contents)
        print("Report of books/frankenstein.txt")
        print(f"{wordNumber} word were found\n")
        letter_count(file_contents)
        
        


main()