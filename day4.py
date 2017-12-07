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


def Main():
    correctPhrases = 0
    #openfile
    data = open("day4_passphrases.txt", "r")
    for line in data:
        if isPassphraseValid(line):
            correctPhrases +=1

    print(correctPhrases)

def isPassphraseValid(phrase):
    words = phrase.split()
    valid = True
    while words:
        test = words.pop()
        if test in words:
            valid = False

    return valid;

if __name__ == '__main__':
    Main()
