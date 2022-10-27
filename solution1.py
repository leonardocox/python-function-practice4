# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    return max([a, b, c])


print(max_num(154, 15, 453344))

# or max of any number by using


def max_num_arb(*args):
    return max(args)


print(max_num_arb(3, 4, 3343, 33, 234333, 12))
