def read_file_content(filename):
    with open(filename) as file:
        return file.read() # read it as a whole string
print(read_file_content(r"...\hello.txt"))

def count_words():
    # calling the function and storing the output in `text`
    text = read_file_content(r"...\story.txt")
    output = {} # empty dictionary
    # a set doesn't allow duplicates
    unique = set(text.lower().split()) # convert to lowercase, then make all the words into a list
    for word in unique: # for every word
        output[word] = text.lower().split().count(word) # to make sure it's counting word by word, and not letter by letter
    return output # {"as": 10, "would": 20}
print(count_words())
