class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        dictionary = {}

        # Build a dictionary
        for c in s1:
            if c in dictionary:
                dictionary[c] += 1
            elif c not in dictionary:
                dictionary[c] = 1
        
        # Loop through second string
        i = 0
        window_size = len(s1)

        while i <= len(s2) - window_size:
            j = i + (window_size - 1)
            d = dictionary.copy()

            while j >= i:
                current = s2[j]

                if not d.get(current):
                    i += 1
                    break

                d[current] -= 1

                if j == i:
                    return True
                else:
                    j -= 1

        return False