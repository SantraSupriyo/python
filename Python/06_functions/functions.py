# sum of two numbers using function
# def sum (a, b):
#   return a + b


# a  = sum(2,3)
# print(a)

# Factorial of a number using recursion
def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)

factorial_of_5 = factorial(5)
# print(factorial_of_5)

# print numbers from n to 1 using recursion
def show(n):
  if n == 0:
    return
  else:
    print(n)
    show(n-1)

b = int(input("Enter a number: "))
show(b)
