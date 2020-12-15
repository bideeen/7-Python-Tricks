# First form of list comprehension
x = [i for i in range(20)]

y = [j for j in x if j%2 == 0]

# Second form of list comprehension
z = [k for k in range(20) if k%2 == 0]


print(y)
print(z)