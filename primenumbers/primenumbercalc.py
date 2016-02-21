#prime number calculator
import math
from time import sleep

end_range = raw_input("calculate prime numbers up until: ")

def isprime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0: 
            return False
    return n>1

num = int(end_range)
for n in range(3, num):
    if isprime(n):
        print n

sleep(10)
