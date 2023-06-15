# Problem #1768
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = j = 0
        result = ""
        while (i < len(word1) and j < len(word2)):
            # Add the first 2 letters
            result += word1[i]
            result += word2[j]
            # Increase the index
            i += 1
            j += 1
            while i < len(word1):
                # Alternate over to the next letter
                result += word1[i]
                i += 1
            while j < len(word2):
                result += word2[j]
                j += 1
        return result
    

        # Set range
        # range = 0
        # if (len(word2) > len(word1)):
        #     range = len(word2)
        # else: 
        #     range = len(word1)
            
        # for x in range(range):
        #     if not()
            
        # Go through each index, check if it is a space
        # mergedString = ""
        # for x in word1:
        #     print(index)
            # print(x)
            # if not(x.isspace()):
                
                
                
            
theSolution = Solution().mergeAlternately("a   b   c", "  p   q   r")
print(theSolution)