name = input("Please enter a name: ")
alpha = name
while name != "DONE":
    if name < alpha:
       alpha = name
    name = input("Please enter another name, enter DONE to stop: ")
print(alpha + " is the name that comes first alphabetically")
