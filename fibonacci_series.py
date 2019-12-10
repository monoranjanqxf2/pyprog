def fibonacci_series(number):
    a,b=0,1
    while number > 0:
        yield a
        a,b=b,a+b
        number = number - 1

gen=fibonacci_series(10)
for i in gen:
    print(i)
