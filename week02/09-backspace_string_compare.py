# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:

# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.


def removeBsp(word):
    i = 0
    newWord = list(word)
    while i < len(newWord):
        if newWord[i] == '#':
            if newWord[i-1] != '#' and i != 0:
                del newWord[i-1: i+1]
                i -= 1
                continue
            elif i == 0:
                del newWord[i]
                continue
        i += 1

    return ''.join(newWord)


def backspaceCompare(S, T):
    return removeBsp(S) == removeBsp(T)


print(backspaceCompare("ab#c", "ad#c"))
