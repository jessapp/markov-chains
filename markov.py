from random import choice

import sys

while True:
    try:
        print 'How long would you like your n-grams to be?'
        n = int(raw_input('> '))
        break
    except ValueError:
        print "Please input a valid integer."
        continue


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    open_file = open(file_path)

    return open_file.read()


def make_chains_bi_gram(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    words = text_string.split()

    for i in range(len(words) - 2):
        key = (words[i],words[i+1])

        if key in chains:
            chains[key].append(words[i+2])
        else:
            chains[key] = [words[i+2]]


    last_key = (words[-1], words[0])

    if last_key in chains:
        chains[last_key].append(words[1])
    else:
        chains[last_key] = [words[1]]


    second_to_last_key = (words[-2], words[-1])

    if second_to_last_key in chains:
        chains[second_to_last_key].append(words[0])
    else:
        chains[second_to_last_key] = [words[0]]

    print chains

    return chains


def make_chains_n_gram(text_string, n):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    words = text_string.split()

    for i in range(len(words) - n):
        key = tuple(words[i:i+n])

        if key in chains:
            chains[key].append(words[i+n])
        else:
            chains[key] = [words[i+n]]

    return chains



def make_text(chains, n):
    """Takes dictionary of markov chains; returns random text."""

    key = choice(chains.keys())

    text = key[0]

    for i in range(1,len(key)):
        text = text + ' ' + key[i]

    while key in chains and len(text) <= 200:
        random_word = choice(chains[key])
        text = text + ' ' + random_word

        key_list = list(key)[1:]
        key_list.append(random_word)
        
        key = tuple(key_list)

    return text


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains_n_gram(input_text, n)

# Produce random text
random_text = make_text(chains, n)

print random_text

