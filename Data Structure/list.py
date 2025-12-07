# Creating a list of numbers from 1 to 10
nums = []
for i in range(1,11):
    nums.append(i)

# Extracting the first five elements
extracted = nums[0:5]

# Reversing the extracted list
extracted_rev = extracted[::-1]

# Displaying
print("Original List:", nums)
print("Extracted List:", extracted)
print("Reversed Extracted List:", extracted_rev)

