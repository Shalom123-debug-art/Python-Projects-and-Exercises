
# Compound Interest Calculator 
def compound_interest_calculator(principal, rate, time, number_of_times):
  amount = round(principal * pow((1 + rate / number_of_times), (number_of_times * time)), 2)
  compound_interest = round((amount - principal), 2)
  
  print(f"The compound interest earned and the total amount will be {compound_interest}birr and {amount}birr, respectively.")
  
compound_interest_calculator(1000, 0.02, 2, 5)



# Prime Checker, Factors Finder, and Prime Numbers Finder in a Range
def is_prime(num, verbose):
  if num <= 1: 
    if verbose:
      print(f"{num} is neither prime nor composite")
    return False
  for i in range(2, num): 
    if (num % i == 0): 
      if verbose:
        print(f"{num} is composite")
      return False
  if verbose:
    print(f"{num} is prime")
  return True 

print(is_prime(12, True))


def find_factors(num):
  my_factors = [1]
  if is_prime(num, False):
    my_factors.append(num)
    print(f"The factors of {num} are: {my_factors}")
    return 
  
  for j in range(2, num + 1):
    if num % j == 0: 
      my_factors.append(j)
  print(f"The factors of {num} are: {my_factors}")

find_factors(179)


def prime_numbers_finder_in_a_range(start, end):
  my_primes = []
  for i in range(start, end + 1):
    if is_prime(i, False):
      my_primes.append(i)
  print(f"The primes between {start} and {end} are: {my_primes}")

prime_numbers_finder_in_a_range(50, 2000)



# Digital Root Calculator and Numbers with the Same D.R Finder
def find_sum_of_digits(num):
  characters = list(str(num))
  sum_of_characters = 0
  for i in range(0, len(characters)):
    sum_of_characters += int(characters[i])
  return sum_of_characters

print(find_sum_of_digits(5034))


def digital_root_calculator(num): 
  while num > 9:
    num = find_sum_of_digits(num)
  return num
  
print(digital_root_calculator(67879))
  

def find_numbers_with_digital_roots_of(num, start, end):
  digital_roots = []
  for i in range(start, end + 1):
    if digital_root_calculator(i) == num:
      digital_roots.append(i)
  print(f"Numbers from {start} to {end} with a digital root of {num} are: {digital_roots}. ")

find_numbers_with_digital_roots_of(5, 1, 200)



# Kaprekar Routine Cycle Detector
def difference_of_digits(num, verbose):
  digits = str(num).zfill(4)
  asc = sorted(list(digits))
  des = sorted(list(digits), reverse=True)
  diff = int("".join(des)) - int("".join(asc))
  if verbose:
    print(f"{"".join(des)} - {"".join(asc)} = {diff}")
  return diff
  
print(difference_of_digits(6456, False))

def kaprekar_routine(num):
  if not len(str(num)) == 4:
    print("Please type a 4-digit number")
    return 
  steps = 0
  while (not num == 6174) and (not len(str(num)) == 1):
    num = difference_of_digits(num, True)
    steps += 1
  if (num == 6174):
    print(f"Reached 6174 in {steps} steps")
  
kaprekar_routine(9900)



# Simple Calculator
def addition(a, b):
  print(a + b) 
  
def subtraction(a, b):
  print(a - b) 

def multiplication(a, b):
  print(a * b) 

def division(a, b):
  print(round((a / b), 3))
  

division(5, 3)

# Check Whether a Number is Even or Odd
def check_even_odd(num):
  if (num % 2 == 0):
    print("even")
  else:
    print("odd")
    
check_even_odd(0)


def check_even_odd_using_the_long_way(num): 
  if (num % 2 == 0):
    return "even"
  else:
    return "odd"
    
print(check_even_odd_using_the_long_way(9))

# Checking the data type of variables
x = "Shalom"
print(type(x))
# String Concatenation
num1 = "5"
num2 = "67"
print(num1 + num2)

# Receiving inputs from users
"""
Last year, we used "c in >>" to receive inputs when working on c++.
"""
name = input("What's your name?")
print(type(name))

age = int(input("How old are you?"))
print(type(age))
