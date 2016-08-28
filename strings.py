name = "Tendai"

if name.startswith("Ten"):
    print("Yes, the string starts with 'Ten'")

if 'a' in name:
    print("Yes, it contains the string 'a'")

if name.find("enda") != -1:
    print("Yes it contains the string 'enda'")

delimiter = '_*_'
mylist = ["Brazil", "Russia", "India", "China"]
print(delimiter.join(mylist))
