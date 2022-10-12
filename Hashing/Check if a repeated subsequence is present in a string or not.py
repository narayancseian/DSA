# Recursive function to check if `s[low…high]` is a palindrome or not
def isPalindrome(s):
 
    (low, high) = (0, len(s) - 1)
 
    while low < high:
        if s[low] != s[high]:
            return False
        low = low + 1
        high = high - 1
 
    return True
 
 
# Function to checks if repeated subsequence is present in a string
def hasRepeatedSubsequence(s):
 
    # base case
    if not s or not len(s):
        return False
 
    # dictionary to store the frequency of each distinct character of a given string
    freq = {}
 
    # update dictionary with frequency
    for c in s:
        # if the frequency of any character becomes 3, we have found a
        # repeated subsequence
        freq[c] = freq.get(c, 0) + 1
        if freq.get(c) >= 3:
            return True
 
    # consider all repeated elements (frequency 2 or more)
    # and discard all non-repeating elements (frequency 1)
    repeated = [c for c in s if freq.get(c) >= 2]
 
    # return false if it is a palindrome
    return not isPalindrome(repeated)
 
 
if __name__ == '__main__':
 
    s = 'XYBYAXB'        # 'XB' is repeated subsequence
 
    if hasRepeatedSubsequence(s):
        print('Repeated subsequence is present')
    else:
        print('No repeated subsequence is present')
 
