
# Exercise: Numbers of Specific Type Lister in a Range
user_range_start = int(input("Enter the number from which you want to start"))
user_range_end = int(input("\nEnter the number up to which you want it to function"))

def even_numbers_lister(start, end):
  even_numbers = []
  for i in range(start, end + 1):
    if i % 2 == 0:
      even_numbers.append(i)
  print(f"\nEven numbers from {start} to {end} are: \n\t{even_numbers}")

def isPrime(num):
  if num <= 1:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

def prime_numbers_lister(start, end):
  prime_numbers = []
  for j in range(start, end + 1):
    if isPrime(j):
      prime_numbers.append(j)
  print(f"Prime numbers from {start} to {end} are: \n\t{prime_numbers}")


even_numbers_lister(user_range_start, user_range_end)
prime_numbers_lister(user_range_start, user_range_end)
