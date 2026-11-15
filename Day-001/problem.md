
# Day 001 - Number of Sub-arrays With Odd Sum

## Problem Details

- **LeetCode Number:** 1524
- **Difficulty:** Medium
- **Topic:** Prefix Sum, Array
- **Language:** Python 3

## 1. Problem Statement

You are given an integer array `arr`.

Your task is to count how many continuous subarrays have an **odd sum**.

Return the total count modulo `10^9 + 7` because the answer can be very large.

### What is a Subarray?

A subarray is a continuous part of an array.

For example:

`arr = [1, 3, 5]`

All possible subarrays are:

- [1]
- [1, 3]
- [1, 3, 5]
- [3]
- [3, 5]
- [5]

## 2. Example 1

**Input:**
```python
arr = [1, 3, 5]
```

**All Possible Subarrays and Their Sums:**

| Subarray | Sum | Type |
|---|---:|---|
| [1] | 1 | Odd |
| [1, 3] | 4 | Even |
| [1, 3, 5] | 9 | Odd |
| [3] | 3 | Odd |
| [3, 5] | 8 | Even |
| [5] | 5 | Odd |

**Output:**
```python
4
```

**Explanation:**

There are 4 subarrays with odd sums:

- [1] → 1
- [1, 3, 5] → 9
- [3] → 3
- [5] → 5

Therefore, the answer is 4.

## 3. Example 2

**Input:**
```python
arr = [2, 4, 6]
```

**Output:**
```python
0
```

**Explanation:**

Every possible subarray has an even sum.

Therefore, there are no subarrays with odd sums.

## 4. Approach 1: Brute Force

### Idea

- Start from each index.
- Calculate the sum of every possible continuous subarray.
- Check whether the sum is odd.
- If it is odd, increase the count.

### Algorithm

1. Initialize count = 0.
2. Use an outer loop to select the starting index.
3. Use an inner loop to select the ending index.
4. Calculate the subarray sum.
5. If sum % 2 == 1, increment count.
6. Return count modulo 10^9 + 7.

### Complexity Analysis

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)

## 5. Approach 2: Optimized (Prefix Sum)

### Idea

Instead of calculating every subarray sum, use the parity of prefix sums.

A prefix sum is the sum of all elements from the beginning of the array up to the current index.

**Important Mathematical Observation:**

- Odd + Even = Odd
- Even + Odd = Odd
- Odd + Odd = Even
- Even + Even = Even

A subarray sum is odd when its two prefix sums have different parity.

### Key Logic

Maintain two counters:

- `even = 1` → Initially, the empty prefix has an even sum.
- `odd = 0` → Initially, there are no odd prefix sums.

For every element:

1. Add the current number to the prefix sum.
2. If the prefix sum is even:
   - Add the number of previous odd prefix sums to the answer.
   - Increase the even counter.
3. Otherwise:
   - Add the number of previous even prefix sums to the answer.
   - Increase the odd counter.
4. Apply modulo to the answer.

### Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## 6. Dry Run of Optimized Approach

Input:
```python
arr = [1, 3, 5]
```

| Number | Prefix Sum | Parity | Odd Count | Even Count | Answer |
|---|---:|---|---:|---:|---:|
| Initial | 0 | Even | 0 | 1 | 0 |
| 1 | 1 | Odd | 1 | 1 | 1 |
| 3 | 4 | Even | 1 | 2 | 2 |
| 5 | 9 | Odd | 2 | 2 | 4 |

Final Answer:
```python
4
```

## 7. Comparison of Both Approaches

| Factor | Brute Force | Optimized |
|---|---|---|
| Technique | Nested Loops | Prefix Sum |
| Time | O(n²) | O(n) |
| Space | O(1) | O(1) |
| Performance | Slower | Faster |

## 8. Key Learnings

- Understand how to generate all possible subarrays.
- Learn the concept of prefix sums.
- Understand odd and even parity.
- Use previous prefix sums to count valid subarrays.
- Optimize an O(n²) solution into O(n).

## 9. Important Takeaway

**Remember:**

If the current prefix sum is even, add the previous odd prefix count.

If the current prefix sum is odd, add the previous even prefix count.

This allows us to count all odd-sum subarrays in a single traversal.

---

**Status:** Solved

**Next Goal:** Practice more Prefix Sum problems.
