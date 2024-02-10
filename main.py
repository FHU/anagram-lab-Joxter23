#REMOVE PASS AND FIX THIS FUNCTION
def anagram(word1, word2):
    word1 = word1.replace(' ', '')
    word2 = word2.replace(' ', '')

    word1 = word1.lower()
    word2 = word2.lower()

    word1 = sorted(word1)
    word2 = sorted(word2)

    if len(word1) == 0 or len(word2) == 0:
        return False
    elif word1 == word2:
        return True
    else:
        return False

if __name__ == '__main__':
    word1 = input()
    word2 = input()

    print(anagram(word1, word2))

#comment
    