# Generate a random DNA sequence

# Should store ATCG as 'ATCG' or as '1234' and just display as '1234'? Use base 2?

#Generate random number then convert to base 2? Or just use fake-base-2 binary? (Is it even fake?)

#Shifting to 0-3

# 0 = A, 1 = T, 2 = C, 3 = G

import random
#from 00SplitandConv import nucDict


nucDict = {
    "0": "A",
    "1": "T",
    "2": "C",
    "3": "G"
}

def randDNA(p):
    dnaTernTemp = ""
    for i in range(p):
        temp = str(random.randint(0, 3))
        dnaTernTemp += temp

    return(str(dnaTernTemp))

#
#def convDNA(y):
#    my_str = str(y)
#    my_list = [int(x) for x in my_str] #unused
#    l = 2
#    my_duolist = [my_str[i:i+l] for i in range(0, len(my_str), l)]
#    print(my_duolist)
#    my_nuclist = [nucDict[my_duolist] for my_duolist in my_duolist]
#    
#    return(my_nuclist)

def convDNA(y):
    my_str = str(y)
    my_list = [int(x) for x in my_str] #hilarious results if int(x)is instead str(x), unused line otherwise since it returns list of integers, not strings
    my_list_str = [my_str[i:i+1] for i in range(0, len(my_str))]
    #print(my_list_str)
    my_nuclist = [nucDict[my_list_str] for my_list_str in my_list_str]
    #print(my_nuclist)
    return(my_nuclist)

def convDNA2(y):
    #my_str = str(y)
    list = [y[i:i+1] for i in range(0, len(y))]
    nuclist = [nucDict[list] for list in list]
    return(nuclist)


print('How long a DNA sequence should we generate?')

n = int(input())
dnaTern = randDNA(n)
dnaSeqNuc = convDNA(dnaTern)
#test_list = ['3', '2', '2', '3', '0', '0', '2', '1', '3', '3', '1', '0', '3', '1', '3', '3', '1', '1', '2', '3', '1', '3', '1', '0', '0', '3', '3', '1', '0', '3', '3', '1', '2', '2', '3', '3', '0', '3', '2', '1', '0', '0', '0', '0', '0', '3', '1', '0', '1', '0', '1', '3', '2', '2', '3', '0', '1', '0', '0', '3', '3', '0', '3', '3', '1', '3', '0', '0', '0', '3', '1', '0', '0', '2', '1', '2', '3', '2', '3', '1', '2', '3', '2', '2', '1', '2', '1', '3', '3', '1', '3', '0', '3', '1', '3', '2', '2', '3', '1', '0', '1', '2', '2', '3', '1', '0', '1', '3', '2', '1', '1', '2', '1', '2', '3', '1', '3', '1', '1', '2', '0', '3', '1', '2', '0', '1', '1', '3', '2', '3', '2', '1', '0', '2', '1', '1', '0', '0', '0', '2', '0', '1', '2', '2', '3', '2', '1', '0', '0', '3']
#dnaSeqNucv2 = convDNA(test_list) #doesn't work because is alread list of strings
print("Sequence is: ", dnaTern, "or in nucleotides:", ''.join(dnaSeqNuc))
#print("List ingestion is: ", test_list, "or in nucleotides:", ''.join(dnaSeqNucv2)) #does not work
dnaSeqNuc2 = convDNA2(dnaTern)
print("Sequence via secondary conversion is: ", ''.join(dnaSeqNuc2))