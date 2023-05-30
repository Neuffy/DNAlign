#testing lists, list comprehension

import random

nucDict = {
    "00": "A",
    "01": "T",
    "10": "C",
    "11": "G"
}

nucDictt = {
    "0": "A",
    "1": "T",
    "2": "C",
    "3": "G"
}

def randDNA(p):
    dnaBinTemp = ""
    p = p * 2
    for i in range(p):
        temp = str(random.randint(0, 1))
        dnaBinTemp += temp

    return(dnaBinTemp)

print(randDNA(10))

def randDNAt(p):
    dnaTernTemp = ""
    for i in range(p):
        temp = str(random.randint(0, 3))
        dnaTernTemp += temp

    return(dnaTernTemp)

print(randDNAt(10))


print(randDNAt(10))

#def convDNA(y):

my_str = str(11010101110101)
print(my_str)
    
my_list = [int(x) for x in my_str]
print(my_list)

l = 2

my_duolist = [my_str[i:i+l] for i in range(0, len(my_str), l)]

print(my_duolist)

my_nuclist = [nucDict[my_duolist] for my_duolist in my_duolist]
    
print(my_nuclist)

#ternary version of convDNA:

my_strt = str(231200312)
print(my_strt)
    
my_listt = [int(x) for x in my_strt]
print(my_listt)

lt = 1

#this line is essential for converting from integer into string?
#having a ternary operator for range resulted in keyerrors:
#my_duolistt = [my_strt[i:i+l] for i in range(0, len(my_str), lt)]
my_duolistt = [my_strt[i:i+lt] for i in range(0, len(my_strt))]


print(my_duolistt)

my_nuclistt = [nucDictt[my_duolistt] for my_duolistt in my_duolistt]
    
print(my_nuclistt)



