def areAnagrams(wordOne, wordTwo):
    # Convert both strings to lowercase
    wordOne.lower()
    wordTwo.lower()

    # Check if wordOne & wordTwo have the same lengths
    if len(wordOne) != len(wordTwo):
        return False # Words with differing lengths can't be anagrams
    
    # We are going to store the number of each letter in the words in dictionaries
    count1 = {}
    count2 = {}

    # Count characters in the first string & store them in 'count1'
    for character in wordOne:
        if character in count1:
            count1[character] += 1
        else:
            count1[character] = 1
       
    for character in wordTwo:
        if character in count2:
            count2[character] += 1
        else:
            count2[character] = 1

    # Now we compare the two dictionaries
    # If they are the same, the strings are anagrams
    return count1 == count2

print(areAnagrams("listen","silent")) # This returns True
print(areAnagrams("dog","cat")) # This returns False



