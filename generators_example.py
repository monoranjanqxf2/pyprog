# Defining a generator function
def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3

# Iterating through generator function
for item in simpleGeneratorFun():
    print(item)
# generator_object is a generator object 
generator_object = simpleGeneratorFun() 
# Iterating over the generator object using __next__ 
print(generator_object.__next__())
print(generator_object.__next__())
print(generator_object.__next__())