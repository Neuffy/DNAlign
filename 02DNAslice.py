#Take input sequence (in base-2 binary or in ATCG?), cut into random sequences of X length.and

import random

nucDict = {
    "00": "A",
    "01": "T",
    "10": "C",
    "11": "G"
}

#Cannot ingest a list?
def convDNA(y):
    my_str = str(y)
    my_list = [int(x) for x in my_str]
    l = 2
    my_duolist = [my_str[i:i+l] for i in range(0, len(my_str), l)]
    my_nuclist = [nucDict[my_duolist] for my_duolist in my_duolist]
    print("Duolist is:", my_duolist)    
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
    #my_sliced_duolist = [my_duolist[i:i+1] for i in range(randStart, randStart + basel)]
    #Problem was [i:i+1] - This produces a nested list.
    # [i] grabs one thing an does not make it a list. // Square brackets selects the item at the index
    # [i:i] produces a set of empty nested lists.
    # [i:i+1] grabs one thing and makes it a list.
    # [i:i+2] grabs two things and makes it a list.
    
    #s[i:j] = t --> slice of s from i to j is replaced by the contents of the iterable t
    #s.append(x) --> appends x to the end of the sequence (same as s[len(s):len(s)] = [x])
    #s.insert(i, x) --> inserts x into s at the index given by i (same as s[i:i] = [x])
    #s[i:i] = [x] behaves like insert and s[len(s):len(s)] = [x] behaves like append.
    
    #Let's examine s[i:j] = [t],

    #1. If i == j, then it will behave like insert and inserts t's content to s in index j

    #2. If i == j == len(s), then it will behave like append and appends t's content to s.

    #3. If i != j then slice of s from i to j is replaced by the contents of the iterable t.


    my_sliced_duolist = [my_duolist[i] for i in range(randStart, randStart + basel)]
    dna_slicedseq = my_sliced_duolist

    return(dna_slicedseq)

#150 bp sequence, issue with leading 0s "SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers"
dnaBin = 110101110000100111110100100111110101101101110100001111100011110110101111001110010000000000110100010001111010110001000011110011110111000000110100001001101110110110111010011001111101110011011110101101000110101101000111100101101110110111010110001101100001011110111001001001010000000100011010111001000011


dna_nuc = convDNA(dnaBin)
dna_sliced = sliceDNA(dnaBin)
dna_sliced_nuc = convDNA(dna_sliced) 

print("Original sequence is:", dnaBin, "or in nucleotides:", ''.join(dna_nuc))

print("Sliced sequence is:", dna_sliced)
print("Sliced sequence is:", dna_sliced, "or in nucleotides:", ''.join(dna_sliced_nuc))