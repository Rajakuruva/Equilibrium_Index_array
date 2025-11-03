#  Problem 3: Find the Equilibrium Index in an Array

###  Problem Statement
Given an array of integers, find all the **equilibrium indices** in the array.  
An **equilibrium index** is a position `i` such that the sum of all elements **to the left of `i`** is equal to the sum of all elements **to the right of `i`**.

If there are no such indices, return `-1`.

---

###  Example 1

**Input:**
array = [1, 7, 3, 6, 5, 6]


**Output:**
[3]

---

**Explanation:**
- Left side of index `3`: 1 + 7 + 3 = 11  
- Right side of index `3`: 5 + 6 = 11  
Hence, index `3` is an equilibrium index.

---

### Example 2

**Input:**
array = [1, -1, 1, -1, 1, -1, 1]


**Output:**
[0, 2, 4, 6]

**Explanation:**
There are multiple points where left and right sums are equal.

---

## Approach 1 — Brute Force (O(n²))

```python
def equilibrium_index_array(array):
    if len(array) == 0:
        return -1
    
    res = []
    total_sum = sum(array)
    left_sum = 0
    for idx in range(len(array)):
        right_sum = total_sum - left_sum - array[idx]
        if right_sum == left_sum:
            res.append(idx)
        left_sum+=array[idx]
    
    return res if res else -1

array_data_1 = [1, 7, 3, 6, 5, 6]
array_data_2 = [2, 3, -1, 8, 4]
array_data_3 = [1, -1, 1, -1, 1, -1, 1]
array_data_4 = [1, 2, 3]
array_data_5 = []

print("Case1: Equilibrium Index in an array: ", equilibrium_index_array(array_data_1))
print("Case2: Equilibrium Index in an array: ", equilibrium_index_array(array_data_2))
print("Case3: Equilibrium Index in an array: ", equilibrium_index_array(array_data_3))
print("Case4: Equilibrium Index in an array: ", equilibrium_index_array(array_data_4))
print("Case5: Equilibrium Index in an array: ", equilibrium_index_array(array_data_5))

```

---

###  Time & Space Complexity
- **Time Complexity:** O(n) — each element is visited once.
- **Space Complexity:** O(1) — Only a few extra variables used.

---

### Output Example

---

```
Case1: Equilibrium Index in an array:  [3]
Case2: Equilibrium Index in an array:  [3]
Case3: Equilibrium Index in an array:  [0, 1, 2, 3, 4, 5, 6]
Case4: Equilibrium Index in an array:  -1
Case5: Equilibrium Index in an array:  -1
```
