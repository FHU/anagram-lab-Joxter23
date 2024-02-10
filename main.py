#REMOVE PASS AND FIX THIS FUNCTION
def anagram(word1, word2):
    word1 = word1.strip()
    word2 = word2.strip()

    word1 = word1.lower()
    word2 = word2.lower()

    word1 = sorted(word1)
    word2 = sorted(word2)

    if word1 == word2:
        return True
    else:
        return False

if __name__ == '__main__':
    word1 = input()
    word2 = input()

    print(anagram(word1, word2))

#comment
    