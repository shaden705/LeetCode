def sub_is_Palindrome(s:str, start_index:int, last) -> bool:
    sub = s[start_index:last + 1]
    return sub == sub[::-1]
def longestPalindrome(s: str) -> str:
    if len(s) == 0:
        return s
    if s == s[::-1]:
        return s
    last = len(s) - 1 
    res = ""
    first = 0
    if len(s) == 2 and s[0] != s[1]:
        return s[0]
    if len(s) == 3 and s[first] != s[last]:
        if s[first + 1] == s[last]:
            res = s[first + 1] + s[last]
        elif s[last - 1] == s[first]:
            res = s[first] + s[last - 1]
    else:
        for i in range(len(s)):
            for j in range(i):
                if s[j] == s[i] and sub_is_Palindrome(s,j,i):
                    if len(res) >= len(s[j:i + 1]):
                        continue
                    else:
                        res = s[j:i+ 1]
    if len(res) == 0:
        res = s[first]
    return  res
print(longestPalindrome("shaden"))        