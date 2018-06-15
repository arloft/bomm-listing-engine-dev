# set the text for your greeting in this variable
myText = "i love burritos!"
findThisWord = "burrito"


# this function will take your greeting, put it into the sentence,
# count the length of your greeting's text (number of characters),
# then tell you how many times the text you chose appears in your greeting.

def sayHello(sayWhat, theBlurb):
    print(sayWhat)
    # this line is a function assigned to a variable, the function takes the greeting,
    # adds text to form a sentence, then counts the length (number of characters) of the greeting.
    builtMessage = buildFullMessage(sayWhat)
    print(builtMessage)
    if sayWhat.count(theBlurb) > 1:
        print("The text '" + theBlurb + "' appears in my greeting " + str(sayWhat.count(theBlurb)) + " times.")
    elif sayWhat.count(theBlurb) == 1:
        print("The text '" + theBlurb + "' appears in my greeting " + str(sayWhat.count(theBlurb)) + " time.")
    else:
        print("The text '" + theBlurb + "' does not appear in my greeting. Sad!")


def buildFullMessage(theString):
    fullMessage = str.capitalize("my greeting is " + str(len(theString)) + " characters long, Neat!")
    return (fullMessage)


# this function is 'called', and starts off the process,
# using just the two pieces of text we gave it at the top
sayHello(myText, findThisWord)
