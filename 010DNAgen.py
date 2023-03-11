# Generate a random DNA sequence

# Should store ATCG as 'ATCG' or as '1234' and just display as '1234'? Use base 2?

#Generate random number then convert to base 2? Or just use fake-base-2 binary? (Is it even fake?)

# 00 = A, 01 = T, 10 = C, 11 = G

import random
#from 00SplitandConv import nucDict


nucDict = {
    "00": "A",
    "01": "T",
    "10": "C",
    "11": "G"
}

def randDNA(p):
    dnaBinTemp = ""
    p = p * 2
    for i in range(p):
        temp = str(random.randint(0, 1))
        dnaBinTemp += temp

    return(dnaBinTemp)

# List of ['XX', 'XX'] is generated for my_duolist, but is not ingestable from beginning - a single integer or string is expected.
def convDNA(y):
    my_str = str(y)
    my_list = [int(x) for x in my_str]
    l = 2
    my_duolist = [my_str[i:i+l] for i in range(0, len(my_str), l)]
    print(my_duolist)
    my_nuclist = [nucDict[my_duolist] for my_duolist in my_duolist]
    
    return(my_nuclist)

def convDNAv2(y):
    my_str = str(y)
    my_list = [int(x) for x in my_str]
    l = 2
    my_duolist = [my_str[i:i+l] for i in range(0, len(my_str), l)]
    print(my_duolist)
    my_nuclist = [nucDict[my_duolist] for my_duolist in my_duolist]
    
    return(my_nuclist)

print('How long a DNA sequence should we generate?')

n = int(input())
dnaBin = randDNA(n)
dnaSeqNuc = convDNA(dnaBin)
test_list = ['11', '01', '01', '11', '00', '00', '10', '01', '11', '11', '01', '00', '10', '01', '11', '11', '01', '01', '10', '11', '01', '11', '01', '00', '00', '11', '11', '10', '00', '11', '11', '01', '10', '10', '11', '11', '00', '11', '10', '01', '00', '00', '00', '00', '00', '11', '01', '00', '01', '00', '01', '11', '10', '10', '11', '00', '01', '00', '00', '11', '11', '00', '11', '11', '01', '11', '00', '00', '00', '11', '01', '00', '00', '10', '01', '10', '11', '10', '11', '01', '10', '11', '10', '10', '01', '10', '01', '11', '11', '01', '11', '00', '11', '01', '11', '10', '10', '11', '01', '00', '01', '10', '10', '11', '01', '00', '01', '11', '10', '01', '01', '10', '11', '10', '11', '01', '11', '01', '01', '10', '00', '11', '01', '10', '00', '01', '01', '11', '10', '11', '10', '01', '00', '10', '01', '01', '00', '00', '00', '01', '00', '01', '10', '10', '11', '10', '01', '00', '00', '11']
dnaSeqNucv2 = convDNAv2(test_list)
print("Sequence is: ", dnaBin, "or in nucleotides:", ''.join(dnaSeqNuc))
print("List ingestion is: ", test_list, "or in nucleotides:", ''.join(dnaSeqNucv2))





#dnaSeqLength = input()
#dnaSeq = random.randint(1,4)
#print(dnaSeq)



# Convert base 2 sequence to ATCG
