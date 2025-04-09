# Define the two sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}


SD = a.symmetric_difference(b)


u = a.union(b)
i = a.intersection(b)


U_I_diff = u - i


print(SD)
print(U_I_diff)