def insertion_sort(nums):
    for i in range(1,len(nums)):
        j = i - 1
        v = nums[i]
        while j >= 0 and nums[j] > v:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = v
    return nums




print(insertion_sort([4,2,6,5,1,3]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """

