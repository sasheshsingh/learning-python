## Variable Scope = Where a variable is visible & accessible.

## Scope Resolution = LEGB -> Local, Enclosed, Global, Build-In

def func1():
    a = 1
    print(a)


def func2():
    b = 2 
    print(b)


func1()

func2()

def func1():
    a = 1
    print(a)


def func2():
    a = 2 
    print(a)


func1()

func2()


def func1():
    x = 1 

    def func2():
        print(x)


    func2()

func1()


x = 3


def func1():
    print(x)

def func2():
    print(x)

func1()
func2()


from math import e

def func1():
    print(e)


e = 2

func1()