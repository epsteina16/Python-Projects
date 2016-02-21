# mersenne prime calculator
number = raw_input("enter a prime number to find if it has a mersenne prime: ")
def isprime(x):
    n = abs(int(number))
    for y in range(3, int(n**0.5)+1, 2):
        if n % y == 0:
            return False
    return True
def findprime(x):
    if isprime(number) == True:
        n = 2 ** int(number) - 1
        if isprime(n):
            print n," is a mersenne prime"
        else:
            print "does not have a mersenne prime"
    else:
        print "not a prime"
findprime(number)
