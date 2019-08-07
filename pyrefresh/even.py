nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

def even_nums(nums):
    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
    return evens

print(even_nums(nums))
