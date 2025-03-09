#Problem10.py
#Project Euler problem 10

from NumberTests import isPrime
from NumberTests import nthPrime

def main():
    result = nthPrime(10001)
    print("The 10001st prime number is:", result)

if __name__ == '__main__':
    main()