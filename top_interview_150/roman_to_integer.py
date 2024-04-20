class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_number = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        x = 0

        #for loop
        for i in range(len(s)):
            # grabs the value from dict
            if i < len(s) - 1 and roman_to_number[s[i]] < roman_to_number[s[i + 1]]:
                x -= roman_to_number[s[i]]
            else:
                x += roman_to_number[s[i]]
        return x
    
