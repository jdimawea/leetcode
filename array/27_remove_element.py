def removeElement(val, nums):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    print(nums)
    print(k)

myArray = [0, 0, 1, 2, 3, 3, 3, 4, 5, 3, 6, 3, 2, 8, 2]
val = 2

removeElement(val, myArray)