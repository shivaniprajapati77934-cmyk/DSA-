#8. Matrix Rotation (90° Clockwise)
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

n = len(matrix)

for i in range(n):
    for j in range(n):
        print(matrix[n-j-1][i], end=" ")
    print()
#9. Binary Search
arr = [1,2,3,4,5,6,7,8,9]
target = 4

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2
    
    if arr[mid] == target:
        print("Index:", mid)
        break
    
    elif arr[mid] < target:
        low = mid + 1
    
    else:
        high = mid - 1
#10. Count Frequency of Each Integer in Array
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key in freq:
    print(key, "occurs", freq[key], "times")
#11. Spiral Matrix Traversal
matrix = [
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16],
[17,18,19,20]
]

top = 0
bottom = len(matrix)-1
left = 0
right = len(matrix[0])-1

while top <= bottom and left <= right:

    for i in range(left, right+1):
        print(matrix[top][i], end=" ")
    top += 1

    for i in range(top, bottom+1):
        print(matrix[i][right], end=" ")
    right -= 1

    if top <= bottom:
        for i in range(right, left-1, -1):
            print(matrix[bottom][i], end=" ")
        bottom -= 1

    if left <= right:
        for i in range(bottom, top-1, -1):
            print(matrix[i][left], end=" ")
        left += 1
#12. Second Largest and Second Smallest
arr = list(map(int, input("Enter elements: ").split()))

unique = list(set(arr))

if len(unique) < 2:
    print("Second Smallest: -1")
    print("Second Largest: -1")
else:
    unique.sort()
    
    print("Second Smallest:", unique[1])
    print("Second Largest:", unique[-2])
#13. Merge Overlapping Intervals
intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort()

merged = []

for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])

print(merged)
#14.Matrix Identity Check
A = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3],
     [4,4,4,4]]

B = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3],
     [4,4,4,4]]

if A == B:
    print("Matrices are identical")
else:
    print("Matrices are not identical")
#15. Reverse an Array
arr = [5,4,3,2,1]

print(arr[::-1])
#16. Kth Largest Element
nums = [3,2,1,5,6,4]
k = 2

nums.sort()

print(nums[-k])
#17.Missing Number
nums = [3,0,1]

n = len(nums)

total = n*(n+1)//2

print(total - sum(nums))
#18. Find Duplicate Number
arr = [1,3,4,2,2]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            print("Duplicate Number:",arr[i])

#19.Merge Two Sorted Arrays
def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(merge(nums1,3,nums2,3))

#20. Rotate Array
def rotate(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]
    return nums


nums = [1,2,3,4,5,6,7]
print(rotate(nums,3))

#21. Maximum Product Subarray
def maxProduct(nums):
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])

        result = max(result, max_prod)

    return result


nums = [2,3,-2,4]
print(maxProduct(nums))

#22. Count Pairs With Given Sum
def countPairs(arr, target):
    count = 0
    seen = {}

    for num in arr:
        complement = target - num

        if complement in seen:
            count += seen[complement]

        seen[num] = seen.get(num, 0) + 1

    return count


arr = [1,5,7,-1,5]
target = 6
print(countPairs(arr, target))

#23. Move Zeros to End
def moveZeroes(nums):
    j = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
            
    return nums


nums = [0,1,0,3,12]
print(moveZeroes(nums))

#24. Majority Element
def majorityElement(nums):
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1
            
    return candidate


nums = [3,2,3]
print(majorityElement(nums))

#25. Intersection of Two Arrays
def intersection(nums1, nums2):
    result = list(set(nums1) & set(nums2))
    return result


nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersection(nums1, nums2))