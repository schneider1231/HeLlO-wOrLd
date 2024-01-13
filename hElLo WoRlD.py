string =input("Enter a sentence\n:").replace(" ","  ")#add an extra space betweeen the words so each other character will be upper and lower 
new_string =""

print(string.replace("  "," "))

for i in range(len(string)):#loops through the lenght of the string
    if i % 2 == 1:#goes through the index of the string for even and odd
        new_string += string[i].upper()#uppercase the even indecies and saves it in a new string
    else:
        new_string += string[i].lower()#lowercase the odd indecies and saves it in a new string

string = string.replace("  "," ")#returns the space betweeen the words to normal

print(f"\n{new_string.replace("  "," ")}")#print string with alternating upper/lower case characters

new_str =""

words = string.split(" ")#turns string into a list so the contents are mutable

for i in range(len(words)):#loop through the lenght of the list
    if i % 2 == 1:#goes through the even and odds
        new_str += words[i].upper() + " "#uppper case the even count in the list then saves it into a new string and adds a space " " at the end 
    else:
        new_str += words[i].lower() + " "#lower case the odd count in the list then saves it into a new string and adds a space " " at the end 

print(f"\n{new_str}")#prints the new string made from the list with each other word being upper and lower case
