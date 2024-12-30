def bubble_sort(nums):
    for i in range(len(nums)-1,-1,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums




print(bubble_sort([4,2,6,5,1,3]))

 
 
"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """