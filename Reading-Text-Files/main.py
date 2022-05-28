# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from itertools import count
from posixpath import split


def read_file_content(filename):
    # [assignment] Add your code here 
    with open('story.txt') as f:
        file = f.read()
    
    return file
read_file_content('story.txt')
print(read_file_content("./story.txt"))

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    split_text = text.split()
    count_words = {}
    for i in split_text:
            if i in count_words:
                count_words[i] += 1
            else:
                count_words[i] = 1
    
    return count_words
print(count_words())