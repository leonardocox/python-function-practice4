# Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(x, a, b):
    return x in range(a, b + 1)


print(num_within(5, 4, 20))
print(num_within(34534923325, 4, 20))
