# Given a string s, find the length of the longest substring without duplicate characters.


def sub(s):
    visited = []
    seq_len = 1
    n = len(s)
    if n==1:
        return seq_len
    else:
        visited.append(+s[0])
        i=1
        while i<n:


 # s = "abcabcbb"

