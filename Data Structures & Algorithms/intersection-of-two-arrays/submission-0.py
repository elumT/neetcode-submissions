class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        snums1 = set(nums1)
        res = set()
        for n in nums2:
            if n in snums1:
                res.add(n)

        return list(res)