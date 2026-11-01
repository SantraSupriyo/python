# list = [1,2,3,4,5,6,7,8,9,10]

# def length(list):
#   count = 0
#   for el in list:
#     count += 1
#   return count

# length_of_list = length(list)
# print(f"Length of the list is: {length_of_list}")

# list = [1,2,3,4,5,6,7,8,9,10]

def print_list(list):
  print(*list) # printing in one line

# print_list(list)


def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

#  print(factorial(5))

def USD_to_INR(USD):
  INR = USD * 82.74
  return INR

# print(USD_to_INR(100))

def addition(n):
  sum = 0
  for i in range(1, n+1):
    sum += i
  return sum

addition_of_n = addition(10)
# print(f"Addition of first 10 natural numbers is: {addition_of_n}")



def print_list_recursive(my_list, index=0):
    if index >= len(my_list):
        return
    print(my_list[index])
    print_list_recursive(my_list, index + 1)


numbers = [10, 20, 30, 40, 50]
print_list_recursive(numbers)

