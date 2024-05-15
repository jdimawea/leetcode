def removeDuplicates(nums):

    left = 1

    for right in range(1, len(nums)): # Right starts at 1 and ends at the length of nums
        if nums[right] != nums[right - 1]: # If element does not match the element before
            nums[left] = nums[right] # nums[left] = to nums[right]
            left += 1 # increment left by one to move the pointer
    
    print(nums, left) # Returns left which outputs the length of unique numbers
    return left

myArray = [0, 0, 0, 1, 1, 1, 1, 2, 3, 4, 4, 5]
removeDuplicates(myArray)
