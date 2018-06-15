# script to live-calculate the character count of a string
# when creating the leading part of a product SKU for Amazon (21 max)


def filter_long_words(string):
    string = raw_input("SKU: ")
    maxCount = raw_input(21)

typedCount = 0
for letter in string:
    typedCount = typedCount + 1
print("typed length is: ", typedCount)
return typedCount

filter_long_words(string)
if count > maxCount:
    print(len(string))