def LongestVowelSubsequence(s):
   vowels = "aeiou"
   count = 1
   max_len = 0
   for c in s:
      if c == vowels[count-1]
          count += 1
          if count > 5:
               count = 5
       if count == 5:
           max_len = len(s)
    if count < 5:
        return 0
    return max_len
