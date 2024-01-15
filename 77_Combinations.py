class Solution:
    def backtrack(self,result,temp,nums,start,k):
        # Return if length of temp list = k after appending to result
        if len(temp) == k:
            result.append(temp.copy())
            return

        # if start exceeds length of nums, return
        if start == len(nums):
            return
        
        # Append number if not in temp
        temp.append(nums[start])
        self.backtrack(result,temp,nums,start+1,k)
        # Remove last element if temp == k
        temp.pop()
        self.backtrack(result,temp,nums,start+1,k)

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = []
        for i in range(1,n+1):
            nums.append(i)

        result = []
        # backtrack(resultset,tempset,originalarray,start,constraint)
        self.backtrack(result,[],nums,0,k)
        
        return result
