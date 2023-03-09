#Take input sequence (in base-2 binary or in ATCG?), cut into random sequences of X length.and
#Iterate: Do X times

import random

nucDict = {
    "00": "A",
    "01": "T",
    "10": "C",
    "11": "G"
}

def convDNA(y):
    my_str = str(y)
    my_list = [int(x) for x in my_str]
    l = 2
    my_duolist = [my_str[i:i+l] for i in range(0, len(my_str), l)]
    my_nuclist = [nucDict[my_duolist] for my_duolist in my_duolist]
    
    return(my_nuclist)

#grab random set of 25 bases from sequence
#Could grab directly from base2 but that would allow for possibility of a frameshift
def sliceDNA(y):
    my_str = str(y)
    my_list = [int(x) for x in my_str]
    l = 2
    basel = 25
    #
    randStart = random.randint(0, (len(my_str) // 2))
    my_duolist = [my_str[i:i+l] for i in range(0, len(my_str), l)]
    #my_sliced_duolist = [my_duolist[i:i+1] for i in range((random.randint(0, (len(my_str) // 2 - 25))), (len(my_str) // 2))]
    #Random value taken for start point, then range until basel/25 later
    my_sliced_duolist = [my_duolist[i:i+1] for i in range(randStart, randStart + basel)]
    dna_slicedseq = my_sliced_duolist

    return(dna_slicedseq)

#150 bp sequence, issue with leading 0s "SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers"
dnaBin = 110101110000100111110100100111110101101101110100001111100011110110101111001110010000000000110100010001111010110001000011110011110111000000110100001001101110110110111010011001111101110011011110101101000110101101000111100101101110110111010110001101100001011110111001001001010000000100011010111001000011


dna_nuc = convDNA(dnaBin)
dna_sliced = sliceDNA(dnaBin)
#dna_sliced_nuc = convDNA(dna_sliced) 

print("Original sequence is:", dnaBin, "or in nucleotides:", ''.join(dna_nuc))
print("Sliced sequence is:", dna_sliced)
#print("Sliced sequence is:", dna_sliced, "or in nucleotides:", ''.join(dna_sliced_nuc))