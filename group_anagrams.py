# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

from collections import defaultdict 

def groupAnagrams(strs):
    sortWords = []
    for word in strs:
        sortWords.append((''.join(sorted(word)), word))

    anagrams = defaultdict(list)

    for sort, word in sortWords:
        anagrams[sort].append(word)

    return list(anagrams.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
