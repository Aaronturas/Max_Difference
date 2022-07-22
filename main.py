#function max_difference that takes in an integer list and returns the maximum difference between the elements in the list such that the element values are increasing.
def max_difference(nums):
  maxDiff = -1
  minNum = nums[0]
  
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if j > i:#if next element is greater than i then find the difference
        minNum = min(minNum, nums[i])
    maxDiff = max(maxDiff, nums[i] - minNum)#finds the current max difference in i
 
  if maxDiff != 0:
    return maxDiff
  else:
    return -1

# Test Cases
nums = [7, 1, 5, 4]
print("Input: ", nums)
print("Output: ", max_difference(nums))

nums = [9, 4, 3, 2]
print("\nInput: ", nums)
print("Output: ", max_difference(nums))

nums = [1, 5, 2, 10]
print("\nInput: ", nums)
print("Output: ", max_difference(nums))