#w3schools while exercises
i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
    if i == 3:
       break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
       continue
    print(i)

i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
   print(i)
   i += 1
else:
   print("i is no longer less than 6")

#w3schools lists exercises

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

fruits = ["apple", "banana", "cherry"]
fruits.removes("banana")

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(len(fruits))

#w3schools tuples exercises

fruits = ("apple", "banana", "cherry")
print(fruits[0])

fruits = ("apple", "banana", "cherry")
print(len(fruits))

fruits = ("apple", "banana", "cherry")
print(fruits[-1])

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#w3schools sets exercises

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
   print("Yes, apple is a fruit")

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#w3schools dictionaries exercises
car = {
   "brand" : "Ford",
   "model" : "Mustang",
   "year" : 1964
}

print(car.get("model"))

car = {
   "brand" : "Ford",
   "model" : "Mustang",
   "year" : 1964
}
car["year"] = 2020

car = {
   "brand" : "Ford",
   "model" : "Mustang",
   "year" : "1964"
}

car["color"] = "red"

car = {
   "brand" : "Ford",
   "model" : "Mustang",
   "year" : "1964"
}

car.pop("model")

car = {
   "brand" : "Ford",
   "model" : "Mustang",
   "year" : "1964"
}

car.clear()

#w3schools for loops exercises

fruits = ["apple", "banana", "cherry"]
for x in fruits:
   print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
   if x == "banana":
      continue
   print(x)

for x in range(6):
   print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
   if x == "banana":
      break
   print(x)
#######