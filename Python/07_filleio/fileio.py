# f = open("07_filleio\demo.txt", "r")

# data = f.read()
# data = f.readline()
# print(data)
# print(type(data))

f = open("07_filleio\demo.txt", "w")

f.write("I want to learn python from tomorrow")
f.write("\nI want to learn python from tomorrow")


f.close()


with open("07_filleio\demo.txt", "r") as f:
  data = f.read()
  print(data)

# with open("07_filleio\demo.txt", "r") as f:
#   f.write("new data")



import os

os.remove("07_filleio\sample.txt")
