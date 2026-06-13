class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        longest_prefix = strs[0]
        array_length = len(strs)

        for i in range(1, array_length):
            current_string = strs[i]
            j = 0

            while j < min(len(longest_prefix), len(current_string)):
                if longest_prefix[j] != current_string[j]:
                    break
                j += 1
            longest_prefix = longest_prefix[:j]

        return longest_prefix