ab = {
    "Swaroop": "swaroop@swaroopch.com",
    "Larry": "larry@wall.org",
    "Matsumoto": "matz@ruby-land.org",
    "Spammer": "spammer@hotmail.com"
}

print("Swaroop's address is ", ab["Swaroop"])
print("Matsumoto's address is", ab["Matsumoto"])

del(ab["Spammer"])

print("\nThere are {} contacts in the address-book\n".format(len(ab)))

for name, address in ab.items():
    print("Contact {} at {} ".format(name, address))

ab["Guido"] = "guido@python-land.org"

if "Guido" in ab:
    print("\nGuido's address is: ", ab["Guido"])
    print("\nThere are now {} contacts in the address book".format(len(ab)))
