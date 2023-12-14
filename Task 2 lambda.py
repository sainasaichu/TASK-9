nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("original list of integers:")
print(nums)

print("\neven numbers from the said list:")
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
print("\nodd numbers from the said list:")
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums)
