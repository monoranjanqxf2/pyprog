a = [25,15,8,6,7,3,4]
max=max(a)
for i in a:
    if i>=max:
        max=i
max2=min(a)
for i in a:
    if i>=max2 and i<max:
        max2=i
print(f"second max is {max2}")

