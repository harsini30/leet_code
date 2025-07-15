class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = set()

        for n in range(len(nums)):
            if nums[n] in seen:
                return True
            seen.add(nums[n])
            
            if len(seen) > k:
                seen.remove(nums[n - k])  # Keep the sliding window size ≤ k

        return False
