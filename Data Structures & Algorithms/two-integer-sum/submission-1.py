class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        seen[nums[0]] = 0
        for i in range(1, len(nums)):
            print(seen.get(nums[i]))
            difference = target - nums[i] 
            print(f"difference: {difference}")
            if difference in seen:
                return [seen.get(difference), i]
            seen[nums[i]] = i

        return []
