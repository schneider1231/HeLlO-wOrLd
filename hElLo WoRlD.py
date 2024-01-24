'''
This code asks the user to input a sentence and saves it as a string e.g. "hello world"
Then changes each other character to uppercase and lower case to look like this "hElLo WoRLlD"
Then changes each other word to uppercase and lower case to look like this "hello WORLD"
'''

#Get input from user then replace single spaces with double spaces
string =input("Enter a sentence\n:").replace(" ","  ")

#Create empty string which will store the modified string
new_string =""

#Print the users string un modified
print(string.replace("  "," "))

#loops through the lenght of the string
for i in range(len(string)):
    #goes through the index of the string for even and odd
    if i % 2 == 1:
        new_string += string[i].upper() #uppercase the even indecies and saves it in a new string
    else:
        new_string += string[i].lower() #lowercase the odd indecies and saves it in a new string

#returns the space betweeen the words to normal
string = string.replace("  "," ")

#print string with alternating upper/lower case characters
print(f"\n{new_string.replace("  "," ")}")

#Create empty string which will store the modified string
new_str =""

#turns string into a list so the contents are mutable
words = string.split(" ")

#loop through the lenght of the list
for i in range(len(words)):
    #goes through the even and odds
    if i % 2 == 1:
        new_str += words[i].upper() + " "#uppercase the words at even indices and add a space
    else:
        new_str += words[i].lower() + " "#lowercase the words at odd indices and add a space

#prints the new string made from the list with each other word being upper and lower case
print(f"\n{new_str}")
