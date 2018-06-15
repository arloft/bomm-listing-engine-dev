# taking a file as input then scanning its text contents,
# searching for instances of a chosen set of characters,
# counting those instances, and returning the amount

# path to the text file we're searching
inputTextfile = ""
# text file contents, stored in a variable
rawFileConents = ""

# take the file's raw text and break it into an array (list),
# with each list item being 1 line of the file
def rawTextToArray(rawText):
    
