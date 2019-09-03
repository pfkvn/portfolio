# print("Hello World.")
import time

startTime = time.time()

primes = [] 
for possiblePrime in range (2, 20000):
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break

    if isPrime:
        primes.append(possiblePrime)

elapsedTime = time.time() - startTime
 
print(len(primes))
print(elapsedTime, "seconds")