count = 0

with open("07_filleio\practice7\practice2.txt","r") as f:
  data = f.read()
  print(data)

  # num = ""
  # for i in range(len(data)):
  #   if data[i] == ",":
  #     print(num)
  #     num = ""
  #   else:
  #     num += data[i]


  num = data.split(",")
  for value in num:
    if(int(value) % 2 == 0):
      count += 1
     
  print(count)