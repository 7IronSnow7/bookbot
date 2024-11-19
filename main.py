def number_of_characters(text):
    char_count = {}
    for char in text:
        char = char.lower()
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def get_book_text(path):
    # Reading the contents in the book
    with open(path) as f:
        return f.read()
    
def number_of_words(text):
    # Counting the words in the book
    word_count = len(text.split())
    return word_count 

# Contents of the book Frankenstein
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    num_of_char = number_of_characters(text)
  
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    
    # Sort characters in book
    sorted_char = dict(sorted(num_of_char.items()))
    
    for key, value in sorted_char.items():
       if not key.isalpha():
           continue
       else:
           print(f"The {key} character was found {value} times")
    print("--- End report ---")
    
    
if __name__ == "__main__":
    main()
