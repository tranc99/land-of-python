shoplist = ["apple", "mango", "carrot", "banana"]

print("I have ", len(shoplist), " items to purchase.")

for item in shoplist:
    print(item, end=' ')

print("\nI also have to buy rice")
shoplist.append("rice")

def printlist(the_list):
    for item in the_list:
        print("\n", item)

printlist(shoplist)

print("\nI will sort my list now")
shoplist.sort()

print("sorted shopping list: ")

printlist(shoplist)
