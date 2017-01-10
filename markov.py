from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    open_file = open(file_path)

    return open_file.read()


def make_chains(text_string):
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

    i == len(words) - 1

    key = (words[-1], words[0])

    if key in chains:
        chains[key].append(words[1])
    else:
        chains[key] = [words[1]]

    i == len(words) - 2

    key = (words[i], words[-1])

    if key in chains:
        chains[key].append(words[0])
    else:
        chains[key] = [words[0]]


    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text

print chains