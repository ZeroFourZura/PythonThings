
def greeting(*args):
    """This function has an arbitrary amount of arguments"""
    for name in args:
        print("Hello, ", name)


#You can print documentation of a functions
print(greeting.__doc__)
greeting("John", "Bob", "Another Bob", "Billy", "Ben")  


#function with *args and **kwargs
def FunctionArgK(*args, **kwargs):
    for arg in args:
        print('arg: ', arg)
    for key in kwargs.keys():
        print('key: ', key, 'has a value: ', kwargs[key])

FunctionArgK(1, 2, 3, 4, a="10", b="11", c="12", d="a", e="b")

#Anonymous functions - these are functions which are called only once when created
# lambda arguments: expression

double = lambda i: i * i
print(double(10))
print(double(15))

#Other examples of lambda functions
func0 = lambda: print('No args')
func1 = lambda x, y: x * y
func2 = lambda x, y, z: x + y + z

func0()
print(func1(4, 2))
print(func2(1, 2, 3))

