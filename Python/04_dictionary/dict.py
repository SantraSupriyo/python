dict = {
  "name" : "Supriyo",
  "cgpa" : 9.6,
  "marks" : [66,78,90]
  # "key" : value
}

# print(dict["cgpa"])

# nested dictionary

student = {
  "name" : "supriyo",
  "score" :
  {
    "chem": 98,
    "phy" : 98,
    "math": 76
  }
}
# print(student)
# print(student["score"]["math"])

# print(dict.keys())
# print(dict.values())
# print(dict.items())
# print(dict.get("marks"))


dict.update({"city" : "delhi"})
print(dict)