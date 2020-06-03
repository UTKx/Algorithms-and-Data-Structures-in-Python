def anagram(str1, str2):

    # ignoring spaces and capitalization
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    # edge case
    if len(str1) != len(str2):
        return False
    
    # counting frequency of each letter in both dict
    count = {}
    for letter in str1: 
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
        
    for letter in str2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
        
    # checking count of each letter to 0
    for i in count:
        if count[i] == 0:
            return True
    # else not an anagram
    return False

# print(anagram('Fourth of July', 'Joyful Fourth'))
print(anagram('aaa', 'bbb'))
print(anagram('Fog', 'gof'))