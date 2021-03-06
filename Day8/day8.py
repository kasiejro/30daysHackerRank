# Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
# You will then be given an unknown number of names to query your phone book for.
# For each queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
# if an entry for  is not found, print  instead.

#INPUT: The first line contains an integer, n , Not founddenoting the number of entries in the phone book.
# Each of the n subsequent lines describes an entry in the form of 2 space-separated values on a single line.
# The first value is a friend's name, and the second value is an 8-digit phone number.
# After the  lines of phone book entries, there are an unknown number of lines of queries.
# Each line (query) contains a name to look up, and you must continue reading lines until there is no more input.

n = int(raw_input("Enter the size of the phonebook: "))

print "Fill the phone book"
phonebook = {}

def lookup(query, phonebook):
    if phonebook.has_key(query):
        print "%s=%s" %(query,phonebook.get(query))
    else:
        print "Not found"


for i in range(0,n):
    name, phone = (raw_input("Enter name and the number to phonebook: ")).split()

    while(True):
        if len(phone) != 8:
            print "You entered a wrong phone number"
            phone = raw_input("Reenter the phone number: ")
            continue
        else:
            break

    phonebook[name.lower()] = phone

print "The phonebook is full."

while True:
    query = (raw_input("What friend are you looking for? ")).lower()
    lookup(query, phonebook)
    if not query:
        break
