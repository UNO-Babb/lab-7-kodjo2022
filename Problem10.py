#Problem10.py
#Project Euler problem 10

from NumberTests import isPrime
from NumberTests import isPrimeSum
def main():
  print("Sum of primes below 10:", isPrimeSum(10))
  print("Sum of primes below 2 million:", isPrimeSum(2000000))

if __name__ == '__main__':
    main()



      
