class Solution(object):
    def containsDuplicate(self, nums):
        seen = set() #duplicate numbers cannot be present

        for n in nums:
            if n in seen:
                return True
            seen.add(n)    

        return False  
