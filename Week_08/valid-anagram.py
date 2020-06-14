#!/usr/local/anaconda3/bin/python

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(s)==sorted(t) else False

if __name__ == "__main__":
    s = Solution()
    string1 = "anagram"
    string2 = "naagram"
    print(s.isAnagram(string1, string2))