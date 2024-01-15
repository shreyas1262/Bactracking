class Solution:

    def backtrack(self,result,temp,nums,start):
            # Here start represents the level in the tree
            if start == len(nums):
                result.append(temp.copy())
                return
            
            temp.append(nums[start])
            self.backtrack(result,temp,nums,start+1)
            temp.pop()
            self.backtrack(result,temp,nums,start+1)

    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        # backtrack(resultset,tempset,originalarray,startposition)
        self.backtrack(result,[],nums,0)

        return result

        

            
