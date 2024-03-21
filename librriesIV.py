import sys

if len(sys.argv) < 2:#Important to use the (len)gth of the arguments inputted or else you will get type error "not supported between instances of 'str' and 'int'"
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])
