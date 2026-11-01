# num = 1
# while num<101:
#   print(num)
#   num +=1

# num2 = 100
# while num2>0 :
#   print(num2)
#   num2 -= 1 

# a = int(input("Enter number: "))
# i = 1
# while i<11:
#   print(f"{a}*{i} = {a*i}")
#   i += 1

# list = [1, 4, 9, 16, 25, 36, 49,64, 81, 100]

b = 1
list = []
while b<11:
  c = b**2
  list.append(c)
  b += 1

# print(list)

# tup = tuple(list)
# print(tup)

# x = 160
# found = False
# for el in tup:
#   if el == x:
#     found = True
#     break
#   else:
#     found = False

# if found :
#   print(f"{x} found")
# else:
#   print(f"{x} not found")



# for el in range(5):
#   print(el)
# for el in range(1, 5):
#   print(el)
# for el in range(1, 5, 2):
#   print(el)

# for el in range(1, 101):
#   print(el)

# for el in range(100,0, -1):
#   print(el)


# x = int(input("Enter Your Number: "))
# for el in range(1,11,1):
#   print(f"{x}*{el} = {x*el}")


for el in range(10):
  pass # for future code



# n = int(input("Enter upto which number: "))
# i = 0
# sum = 0
# while i < n+1:
#   sum += i
#   i += 1

# print(sum)

# m = int(input("Enter upto which number: "))
# i = 1
# mul = 1
# while i < m+1:
#   mul *= i
#   i += 1

# print(mul)

m = int(input("Enter upto which number: "))
mul = 1
for el in range(1, m+1):
  mul *= el


print(mul)


