#rsa encryption program

import math
from time import sleep
from random import randint

number = raw_input("Enter number: ")
def isprime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0: 
            return False
    return n>1
def randprime():
    a = randint(1000,1500)
    for x in range(a, 2000):
        if isprime(x):
            return x
rand1 = randprime()
rand2 = randprime()
p = rand1
#print p, "p"
q = rand2
#print q, "q"

n = p*q
k = (p-1)*(q-1)

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
e = largest_prime_factor(k+1)
#print e, "e"
d = (k+1)/e
#print d, "d"

B = int(number)
C = (B**e)% n
print C
print "encrypted number is", C
print "public key is", e, n
print "private key is", d, n
print C**d % n

sleep(10)
