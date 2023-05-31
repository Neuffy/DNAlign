#Example alignment
#TAGACTGACCTCGTATCGTACCGTGCCTTCCCTGCGTCGGTACGCAACCTTGGCCTGATCCTTCGTTCTTTCCCGCTATATTAGAGGCAAATCGATATTATGCGCATGCCTTCAATAACCTTTAGTGCAAGATAAAAAAATGCTACGACG
#                                                                   CTTTCCCGCTATATTAGAGGCAAAT
#                                                                            TATATTAGAGGCAAATCGATATTAT
#                           TTCCCTGCGTCGGTACGCAACCTTG
#                 GTACCGTGCCTTCCCTGCGTCGGTA
#                                                           CCTTCGTTCTTTCCCGCTATATTAG
#
#                                                                            TATATTAG - 3x alignment

#Goal is to take fragments and align them against each other and/or a canonical sequence, then display said alignment to show degree of consensus.
#Will eventually need to be able to work with errors and partial alignment (establish thresholds for mismatch, establish consensus).

#Will also eventually need to search sequence and complimentary sequence (ATCG-> vs 
#                                                                       <-TAGC so CGAT)

def lcs(a, b):
    # generate matrix of length of longest common subsequence for substrings of both words
    # Will this generate non-contiguous overlaps? No. Lacks any gap pentalty at all. Needs longest common substring, or implement Needleman-Wunsch (4 Russians Method may be necessary in end) or FOGSAA.
    lengths = [[0] * (len(b)+1) for _ in range(len(a)+1)] #creates list of lists, with the length being that of one string+1, and the number of lists being that of the other string+1. There are other approaches that avoid having to initialize this ... matrix?
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1]) #max is what allows non-contiguous matching?
            
    # read a substring from the matrix
    result = ''
    index = 0
    j = len(b)
    for i in range(1, len(a)+1):
        if lengths[i][j] != lengths[i-1][j]:
            result += a[i-1]
            index = i


    return result, (index - j), index, lengths

#longest common substring, Not working yet
def lcss(a, b):

    gappenalty = 1
    lengths = [[0] * (len(b)+1) for _ in range(len(a)+1)] #creates list of lists, with the length being that of one string+1, and the number of lists being that of the other string+1
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            #needs another if or elif, is applying too many gappenalties
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(0, (max(lengths[i+1][j], lengths[i][j+1]) - gappenalty)) #Attempting to implement gappenalty
            
    # read a substring from the matrix
    # reads continuously, no accounting for gaps
    result = ''
    index = 0
    j = len(b)
    for i in range(1, len(a)+1):
        if lengths[i][j] != lengths[i-1][j]: #and lengths[i][j] > 0 and lengths[i-1][j] > 0:
            result += a[i-1]
            index = i


    return result, (index - j), index, lengths

#Needleman-Wunsch, not working yet
def nmw(a, b):
    #scoring
    #Match = 1, Mismatch = -1, Gap = -2

    lengths = [[0] * (len(b)+1) for _ in range(len(a)+1)] #creates list of lists, with the length being that of one string+1, and the number of lists being that of the other string+1
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1]) #max is what allows non-contiguous matching?
            
    # read a substring from the matrix
    result = ''
    index = 0
    j = len(b)
    for i in range(1, len(a)+1):
        if lengths[i][j] != lengths[i-1][j]:
            result += a[i-1]
            index = i


    return result, (index - j), index, lengths

#DNA sequences
#Seq = 'TAGACTGACCTCGTATCGTACCGTGCCTTCCCTGCGTCGGTACGCAACCTTGGCCTGATCCTTCGTTCTTTCCCGCTATATTAGAGGCAAATCGATATTATGCGCATGCCTTCAATAACCTTTAGTGCAAGATAAAAAAATGCTACGACG'
#SubSeq = 'TCTTTCCCGCTATATTAGAGGCAAA'

#ABC sequences
Seq = 'ABCDEFG'
SubSeq = 'DEG'


#print(Seq[(91-25):91], "Seq")
print(Seq, "- Seq")
print(SubSeq, "- SubSeq")
#print(Seq[lcs(Seq, SubSeq)[1]:lcs(Seq, SubSeq)[2]], "- LCS index output of SubSeq")

print(lcs(Seq, SubSeq)[0:3], "- LCS output")
for s in lcs(Seq, SubSeq)[3]:
    print(*s)
print(lcss(Seq, SubSeq)[0:3], "- LCSS output")
for s in lcss(Seq, SubSeq)[3]:
    print(*s)
print(nmw(Seq, SubSeq)[0:3], "- NMW output")
for s in nmw(Seq, SubSeq)[3]:
    print(*s)