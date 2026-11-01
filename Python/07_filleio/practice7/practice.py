# with open("practice.txt","w") as f:
#   f.write("Hi everyone\nwe are learning File I\O\n")
#   f.write("using Java\nI like programming in Java")

# with open("07_filleio\practice7\practice.txt","r") as f:
#   data = f.read()


# new_data = data.replace("Java","Python")
# print(new_data)

# with open("07_filleio\practice7\practice.txt","w") as f:
#   f.write(new_data)


# def check_word_in_file(word):
#     word = "learning"
#     with open("07_filleio\practice7\practice.txt", "r") as f:
#         data = f.read()
#         if word in data:
#             print(f"{word} is present in the file")
#         else:
#             print(f"{word} is not present in the file")


# check_word_in_file("learning")

# word = "learning"
# with open("07_filleio\practice7\practice.txt","r") as f:
#   data = f.read()
#   if word in data:
#     print(f"{word} is present in the file")
#   else:
#     print(f"{word} is not present in the file")


def chech_for_line():
  word = "learning"
  data = True
  line_no = 0
  with open("07_filleio\practice7\practice.txt","r") as f:
    while data:
      data = f.readline()
      if word in data:
        print(line_no)
        return
      line_no += 1
  return -1

chech_for_line()

