
# Day 002 - Minimum Changes to Make K Semi-palindromes

## Problem Details

- **LeetCode Number:** 2911
- **Difficulty:** Hard
- **Topic:** Dynamic Programming, String, Number Theory
- **Language:** Python 3

## 1. Problem Statement

Given a string `s` and an integer `k`, divide the string into exactly `k` non-empty substrings.

Each substring must have a length of at least 2.

Your task is to find the minimum number of character changes required to make every substring a semi-palindrome.

Return the minimum number of changes.

## 2. What is a Semi-palindrome?

A semi-palindrome is a string that can be divided into groups using a repeating pattern.

To check whether a string is a semi-palindrome:

1. Choose a divisor `d` of the string length.
2. The divisor must be smaller than the string length.
3. Divide characters into groups based on positions separated by `d`.
4. Every group must be a palindrome.

### Example

String: `abcabc`

Length = 6

Possible divisors: 1, 2, 3.

For d = 3:

- Group 1: `aa`
- Group 2: `bb`
- Group 3: `cc`

All groups are palindromes.

Therefore, `abcabc` is a semi-palindrome.

## 3. Example 1

**Input:**
```python
s = "abcac"
k = 2
```

**Output:**
```python
1
```

**Explanation:**

Divide the string into:

- `ab`
- `cac`

The substring `cac` is already a semi-palindrome.

Change `ab` into `aa`.

Only one character change is required.

Answer = 1.

## 4. Example 2

**Input:**
```python
s = "abcdef"
k = 2
```

**Output:**
```python
2
```

**Explanation:**

Divide the string into:

- `abc`
- `def`

Each substring requires one character change to become a semi-palindrome.

Total changes = 2.

## 5. Example 3

**Input:**
```python
s = "aabbaa"
k = 3
```

**Output:**
```python
0
```

**Explanation:**

Divide the string into:

- `aa`
- `bb`
- `aa`

All three substrings are already semi-palindromes.

No changes are required.

Answer = 0.

## 6. Approach 1: Brute Force

### Idea

Try every possible way to divide the string into exactly k substrings.

For each substring:

1. Find all valid divisors of its length.
2. Check the character changes needed for each divisor.
3. Select the minimum changes.
4. Add the changes for all substrings.
5. Find the minimum total across all partitions.

### Complexity

Enumerating all possible partitions is exponential in the number of possible cuts.

This approach is useful for understanding the problem but is inefficient for large inputs.

## 7. Approach 2: Optimized Dynamic Programming

### Idea

Instead of repeatedly checking every partition, use:

- Divisor precomputation
- Memoization
- Dynamic Programming

### Step 1: Precompute Divisors

Find all valid divisors for every possible substring length.

A valid divisor must divide the length and must be smaller than the length.

### Step 2: Calculate Semi-palindrome Cost

For each substring, calculate the minimum number of character changes required.

For each valid divisor:

1. Compare the outer groups.
2. Count mismatching character pairs.
3. Move inward by the divisor.
4. Continue until all groups are checked.
5. Select the minimum cost.

### Step 3: Dynamic Programming

Let `best[j]` represent the minimum changes required to partition the first `j` characters into the number of pieces placed so far.

Try every valid previous partition position and add the cost of the next substring.

Repeat until exactly `k` substrings are formed.

Finally, include the last substring and return the minimum total cost.

## 8. Important Concepts

- **Divisors:** Find valid repeating patterns.
- **Palindrome:** Compare characters from opposite ends.
- **Memoization:** Cache previously calculated substring costs.
- **Dynamic Programming:** Find the minimum cost across different partitions.

## 9. Approach Comparison

| Factor | Brute Force | Optimized |
|---|---|---|
| Technique | Partition Enumeration | DP + Memoization |
| Time | Exponential | Polynomial |
| Performance | Slow | Efficient |
| Repeated Work | High | Reduced |

## 10. Key Learnings

- Understanding semi-palindromes.
- Finding valid divisors of a string length.
- Comparing repeating character groups.
- Using recursion with memoization.
- Applying dynamic programming to string partition problems.

## Important Takeaway

The main challenge is not simply checking whether a string is a palindrome.

It is finding the minimum changes required to make every partition a semi-palindrome while dividing the original string into exactly k parts.

---

**Status:** Solved

**Next Goal:** Practice more String and Dynamic Programming problems.
