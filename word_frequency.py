import re

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

#manages all other functions to process and print word frequency
def controller(file):
    """Read in `file` and print out the frequency of words in that file."""
    this_file = open(file)
    text = this_file.readlines()
    word_list = process_text_to_words(text)
    dictionary_info = count_words(word_list)
    print_word_freq(dictionary_info)
    this_file.close()

#does all of the processing of the text from raw file lines into an array of words
def process_text_to_words(text):
    str = ""
    for item in text:
        str += item
    str = str.lower()
    words = re.sub(r'[?|—|:|"|,|\.\n|\.|\s|\n|]+', "*", str)
    words_split = words.split("*")
    words_filtered = [word for word in words_split if len(word) > 1 and word not in STOP_WORDS] #The len(word) check is here because there's still one piece of white space I haven't pinned down in each file.  I haven't taken the time to figure out a quick way to look at all the whitespace characters yet.
    words_filtered.sort()
    return words_filtered


#puts all words into a dictionary, incrementing the count value for each time it's encountered
def count_words(list):
    dictionary = {}
    for word in list:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    letter_sorted = sorted(dictionary.items(), key=lambda entry: entry[0])   #sorts dictionary into alphabetized tuples
    count_sorted = sorted(letter_sorted, key=lambda seq: seq[1], reverse=True) #sorts alphabetical tuples into count order
    return count_sorted

#prints word frequency in desired format
def print_word_freq(frequency_dictionary):
    for item in frequency_dictionary:
        print(item[0].rjust(15) + "  |  " + str(item[1]).ljust(3) + " " + (item[1] * "*"))


#given function to check arguments list and call the controller function with a file name to be processed
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
