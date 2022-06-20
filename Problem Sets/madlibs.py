                          # Madlibs 

# Goal: Print some faces and shapes! 


"""
Background: 
    If you’ve never heard of Mad Libs, 
    they are basically stories with a fill in the blank structure. 
    The reader is to provide some nouns, adjectives, and adverbs in order to 
    fill the blanks often to a hilarious effect! For more info on how 
    Mad Libs work, go to this link: https://en.wikipedia.org/wiki/Mad_Libs


Your Mission: 
    Create a python program called madlibs.py that asks the user for various 
    strings and creates an Mad Lib story like the output structure below dictates.


Output Structure: 
    Enter a name: [name]
    Enter an adjective: [adjective 1]
    Enter another adjective: [adjective 2]
    Enter an adverb: [adverb]
    Enter a food: [food 1]
    Enter another food: [food 2]
    Enter a noun: [noun]
    Enter a place: [place]
    Enter a verb: [verb]
    [name] was planning a dream vacation to [place].
    [name] was especially looking forward to trying the local
    cuisine, including [adjective 1] [food 1] and [adjective 2] [food 2].

    [name] will have to practice the language [adverb] to
    make it easier to [verb] with people.

    [name] has a long list of sights to see, including the
    [noun] museum and the [adjective 1] river.


Example Run (in terminal): 
    ~/workspace/ $ python adlibs.py
    Enter a name: Tom Brady
    Enter an adjective: stinky
    Enter another adjective: blue
    Enter an adverb: fervently
    Enter a food: soup
    Enter another food: bananas
    Enter a noun: snot
    Enter a place: Harvard
    Enter a verb: fight
    Tom Brady was planning a dream vacation to Harvard.
    Tom Brady was especially looking forward to trying the local
    cuisine, including stinky soup and blue bananas.

    Tom Brady will have to practice the language fervently to
    make it easier to fight with people.

    Tom Brady has a long list of sights to see, including the
    snot museum and the stinky river.
"""

# Code goes below 

# Get user input for each field 
name = input("Enter a name: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adverb = input("Enter an adverb: ")
food1 = input("Enter a food: ")
food2 = input("Enter another food: ")
noun = input("enter a noun: ")
place = input("Enter a place: ")
verb = input("Enter a verb: ")

# print sentences 
print(f"{name} was planning a dream vacation to {place}.")
print(f"{name} was especially looking forward to trying the local cuisine, including {adjective1} {food1} and {adjective2} {food2}.")
print(f"{name} will have to practice the language {adverb} to make it easier to {verb} with people.")
print(f"{name} has a long list of sights to see, including the {noun} museum and the {adjective1} river.")
