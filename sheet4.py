#26. Move # to Front of String
def moveHash(s):
    count = s.count('#')
    s = s.replace('#','')
    
    result = '#' * count + s
    return result


string = "Move#Hash#to#Front"
print(moveHash(string))

#27. Season According to Month
month = int(input("Enter month: "))

if month < 1 or month > 12:
    print("Invalid Month Entered")

elif month >= 3 and month <= 5:
    print("Season: Spring")

elif month >= 6 and month <= 8:
    print("Season: Summer")

elif month >= 9 and month <= 11:
    print("Season: Autumn")

else:
    print("Season: Winter")

#28. Counting Valleys
def countingValleys(steps, path):
    sea_level = 0
    valleys = 0
    
    for step in path:
        if step == 'U':
            sea_level += 1
        else:
            sea_level -= 1
            
        if sea_level == 0 and step == 'U':
            valleys += 1
            
    return valleys


steps = 8
path = "UDDDUDUU"
print(countingValleys(steps, path))

#29. Reduce Consecutive Characters
def compressString(s):
    result = ""
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1
            
    result += s[-1] + str(count)
    
    return result


s = "aabbbbeeeffggg"
print(compressString(s))

#30. Reverse a String
def reverseString(s):
    return s[::-1]


s = "Capgemini"
print(reverseString(s))

#31. Check Valid Anagram
def isAnagram(s, t):
    if sorted(s) == sorted(t):
        return True
    else:
        return False


print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))

#32. First Unique Character (Return Index)
def firstUniqChar(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i
    return -1


print(firstUniqChar("leetcode"))

#33. First Non-Repeated Character
def firstNonRepeated(s):
    for char in s:
        if s.count(char) == 1:
            return char


print(firstNonRepeated("swiss"))

#34. check whether a string is palindrome or not
s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#35. Longest Palindromic Substring
def longestPalindrome(s):
    res = ""
    
    for i in range(len(s)):
        # odd length
        l = r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
        
        # even length
        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
            
    return res


print(longestPalindrome("babad"))

#36. Longest Common Prefix
def longestCommonPrefix(strs):
    prefix = strs[0]
    
    for s in strs[1:]:
        while s.find(prefix) != 0:
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))

#37. String Rotation Check
def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    return goal in (s + s)


print(rotateString("abcde","cdeab"))

#38.Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
        
    return max_len


print(lengthOfLongestSubstring("abcabcbb"))