# --- Day 4: High-Entropy Passphrases ---
#
# A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password.
#A passphrase consists of a series of words (lowercase letters) separated by spaces.
#
# To ensure security, a valid passphrase must contain no duplicate words.
#
# For example:
#
#     aa bb cc dd ee is valid.
#     aa bb cc dd aa is not valid - the word aa appears more than once.
#     aa bb cc dd aaa is valid - aa and aaa count as different words.
#
# The system's full passphrase list is available as your puzzle input. How many passphrases are valid?
#----------------------------------------------------------
# --- Part Two ---
#
# For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.
#
# For example:
#
#     abcde fghij is a valid passphrase.
#     abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
#     a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
#     iiii oiii ooii oooi oooo is valid.
#     oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
#
# Under this new system policy, how many passphrases are valid?

def Main():
    #counter for Part1 and Part2
    correctPhrasesPart1 = 0
    correctPhrasesPart2 = 0

    #openfile
    data = open("day4_passphrases.txt", "r")
    for line in data:
        if isWordIn(line):
            correctPhrasesPart1 +=1
        if isAnagrammIn(line):
            correctPhrasesPart2 +=1

    print("Answer to Part1: " + str(correctPhrasesPart1))
    print("Answer to Part2: " + str(correctPhrasesPart2))


def isWordIn(phrase):
    words = phrase.split()
    valid = True
    while words:
        test = words.pop()
        if test in words:
            valid = False

    return valid;

def isAnagrammIn(phrase):
    words = phrase.split()
    valid =True
    wordSortet = []

    #Create new list that sorts each word alphabetically
    for word in words:
        new = ''.join(sorted(word))
        wordSortet.append(new)

    #test if popped word is in the list
    while wordSortet:
        word = wordSortet.pop()
        if word in wordSortet:
            valid = False

    return valid;

if __name__ == '__main__':
    Main()
