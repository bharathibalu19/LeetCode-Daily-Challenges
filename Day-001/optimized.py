class Solution:
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7

        prefix = 0
        count = 0
        odd = 0
        even = 1

        for num in arr:
            prefix += num

            if prefix % 2 == 0:
                count += odd
                even += 1
            else:
                count += even
                odd += 1

            count %= MOD

        return count
      
# Time: O(n) | Space: O(1)
