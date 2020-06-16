import re

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    this_file = open(file)
    text = this_file.readlines()
    word_list = process_text_to_words(text)
    print(word_list)

def process_text_to_words(text):
    str = ""
    for item in text:
        str += item
    words = re.sub(r'\[\s-\s|"|,\s|,|\.\n|\.\s|\s|\n|\.|:\]', "*", str)
    words2 = words.split("*")
    words_filtered = [word for word in words2 if len(word) > 1 and word not in STOP_WORDS]
    words_filtered.sort()
    return words_filtered






if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
