#Take input sequence (in base-2 binary or in ATCG?), cut into random sequences of X length.and

import random

nucDict = {
    "0": "A",
    "1": "T",
    "2": "C",
    "3": "G"
}

#outputs a converted list, not the string that it should.
def convDNA(y):
    list = [y[i:i+1] for i in range(0, len(y))]
    nuclist = [nucDict[list] for list in list]
  
    return(''.join(nuclist))

def randDNA(p):
    dnaTemp = ""
    for i in range(p):
        temp = str(random.randint(0, 3))
        dnaTemp += temp

    return(dnaTemp)

#grab random set of 25 bases from sequence
#def sliceDNA(y):
    #my_str = str(y)
    #my_list = [int(x) for x in my_str]
    #l = 2
    #basel = 25
    #
    #randStart = random.randint(0, (len(my_str) // 2))
    #my_duolist = [my_str[i:i+l] for i in range(0, len(my_str), l)]

    #my_sliced_duolist = [my_duolist[i] for i in range(randStart, randStart + basel)]
    #dna_slicedseq = my_sliced_duolist

    #return(dna_slicedseq)

#Convention: dnaXSeq = ternary, dnaXNuc = nucleotides.
def sliceDNA25(y):
    my_str = str(y)
    basel = 25 #number of bases to grab for slice
    randStart = random.randint(0, (len(my_str) // 2))
    my_list = [my_str[i:i+1] for i in range(0, len(my_str))]
    dnaSliceSeq = [my_list[i] for i in range(randStart, randStart + basel)]
  
    return(''.join(dnaSliceSeq)) #return(dnaSliceSeq) for a list

dnaSeq = randDNA(150)
dnaNuc = convDNA(dnaSeq)
dnaSeq_sliced = sliceDNA25(dnaSeq)
dnaNuc_sliced = convDNA(dnaSeq_sliced) #doesn't work if input is a list?

print("Original sequence is:", dnaSeq, "or in nucleotides:", dnaNuc)

print("Sliced sequence is:", dnaSeq_sliced, "or in nucleotides:", dnaNuc_sliced)

#should everything be lists, or nothing? Some standard might be good.
#NOLISTS