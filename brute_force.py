class Solution:
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        count = 0

        for i in range(len(arr)):
            total = 0
            for j in range(i, len(arr)):
                total += arr[j]

                if total % 2 == 1:
                    count += 1

        return count % MOD


# Time: O(n²) | Space: O(1)