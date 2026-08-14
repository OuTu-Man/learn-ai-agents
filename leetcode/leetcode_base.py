from typing import List
from collections import Counter

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # https://leetcode.cn/problems/two-sum/
        for num in nums:
            n = target - num
            if n == num:
                if nums.count(num) > 1:
                    indexes = [i for i, x in enumerate(nums) if x == num]
                    return [indexes[0], indexes[1]]
            elif n in nums:
                return [nums.index(num), nums.index(n)]
            else:
                continue
        return []

    def strStr(self, haystack: str, needle: str) -> int:
        # https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=programming-skills
        return haystack.find(needle)

    def mergeAlternately(self, word1: str, word2: str) -> str:
        # https://leetcode.cn/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=programming-skills
        ret = ""
        len_word1 = len(word1)
        len_word2 = len(word2)
        for i in range(0, min(len_word1, len_word2)):
            ret += word1[i] + word2[i]
        if len_word1 > len_word2:
            ret += word1[len_word2:]
        elif len_word2 > len_word1:
            ret += word2[len_word1:]
        return ret

    def findTheDifference(self, s: str, t: str) -> str:
        # https://leetcode.cn/problems/find-the-difference/description/?envType=study-plan-v2&envId=programming-skills
        return list(Counter(t) - Counter(s))[0]

    def isAnagram(self, s: str, t: str) -> bool:
        # https://leetcode.cn/problems/valid-anagram/?envType=study-plan-v2&envId=programming-skills
        return Counter(s) == Counter(t)

    def repeatedSubstringPattern(self, s: str) -> bool:
        # https://leetcode.cn/problems/repeated-substring-pattern/?envType=study-plan-v2&envId=programming-skills
        return s in (s+s)[1:-1]

    def moveZeroes(self, nums: List[int]) -> None:
        # https://leetcode.cn/problems/move-zeroes/?envType=study-plan-v2&envId=programming-skills
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for r in range(len(nums)):
            print(f"1: {nums} - l: {l} - r: {r}")
            if nums[r] == 0:
                continue
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            print(f"2: {nums} - l: {l} - r: {r}")

    def plusOne(self, digits: List[int]) -> List[int]:
        # https://leetcode.cn/problems/plus-one/?envType=study-plan-v2&envId=programming-skills
        d = int("".join(str(x) for x in digits)) + 1
        return [int(x) for x in str(d)]

    def arraySign(self, nums: List[int]) -> int:
        # https://leetcode.cn/problems/sign-of-the-product-of-an-array/?envType=study-plan-v2&envId=programming-skills
        product = 1
        for num in nums:
            if num == 0:
                return 0
            product *=  num
        if product > 0:
            return 1
        else:
            return -1
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # https://leetcode.cn/problems/can-make-arithmetic-progression-from-sequence/?envType=study-plan-v2&envId=programming-skills
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != d:
                return False
        return True

    def isMonotonic(self, nums: List[int]) -> bool:
        # https://leetcode.cn/problems/monotonic-array/?envType=study-plan-v2&envId=programming-skills
        n = len(nums)
        inc, dec = True, True
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                inc = False
            if nums[i] > nums[i - 1]:
                dec = False
            if not inc and not dec:
                return False
        return True

    def lengthOfLastWord(self, s: str) -> int:
        # https://leetcode.cn/problems/length-of-last-word/?envType=study-plan-v2&envId=programming-skills
        return len(s.strip().split()[-1])

    def average(self, salary: List[int]) -> float:
        # https://leetcode.cn/problems/average-salary-excluding-the-minimum-and-maximum-salary/submissions/742147673/?envType=study-plan-v2&envId=programming-skills
        salary.sort()
        salary.pop(0)
        salary.pop(-1)
        n = len(salary)
        s = 0
        return sum(salary) / n

s = Solution()
nums = [1,1,2,3]
print(s.lengthOfLastWord("Hello World"))
