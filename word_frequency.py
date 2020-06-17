import re

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def controller(file):
    """Read in `file` and print out the frequency of words in that file."""
    this_file = open(file)
    text = this_file.readlines()

    word_list = process_text_to_words(text)
    dictionary_info = count_words(word_list)
    print_word_freq(dictionary_info[0], dictionary_info[1])
    this_file.close()

def process_text_to_words(text):
    str = ""
    for item in text:
        str += item
    str = str.lower()
    words = re.sub(r'\[\s-\s|"|,\s|,|\.\n|\.\s|\s|\n|\.|:\]', "*", str)
    words2 = words.split("*")
    words_filtered = [word for word in words2 if len(word) > 1 and word not in STOP_WORDS]
    words_filtered.sort()
    return words_filtered

def count_words(list):
    dictionary = {}
    max_count = 1
    for word in list:
        if word in dictionary:
            dictionary[word] += 1
            if dictionary[word] > max_count:
                max_count = dictionary[word]
        else:
            dictionary[word] = 1
    return [dictionary, max_count]

def print_word_freq(frequency_dictionary, max_count):
    for word_count in range(max_count, 0, -1):
        word_list = [k for k,v in frequency_dictionary.items() if v == word_count]
        if len(word_list) > 0:
            for word in word_list:
                print(word.ljust(15) + "|  " + str(word_count).ljust(3) + " " + (word_count * "*"))


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        controller(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
