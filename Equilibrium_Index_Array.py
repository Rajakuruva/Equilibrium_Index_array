# Find the Equilibrium Index in an Array

def equilibrium_index_array(array):
    if len(array)==0:
        return -1
    res = []                                         # O(1)
    t_sum = sum(array)
    l_sum = 0
    for idx in range(len(array)):
        r_sum = t_sum - l_sum - array[idx]
        if r_sum == l_sum:
            res.append(idx)
        l_sum += array[idx]

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


# Time Complexity: O(n)
# Space Complexity: O(1)

