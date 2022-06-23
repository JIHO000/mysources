# 6장 문자열 뒤집기
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

# 8장 배열 파티션
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

# 11장 보석과 돌
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)

# 11장 상위 K 빈도 요소
import collections


class Solution:
    def topKFrequent(self, nums, k):
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

# 12장 조합
import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))

# 14장 이진 트리 반전
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = \
                self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None

# 15장 배열의 K번째 큰 요소 
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]

# 18장 이진 검색
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1

# 19장 1비트의 개수
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

# 22장 과반수 엘리먼트
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]

