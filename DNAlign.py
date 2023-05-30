#Example alignment
#TAGACTGACCTCGTATCGTACCGTGCCTTCCCTGCGTCGGTACGCAACCTTGGCCTGATCCTTCGTTCTTTCCCGCTATATTAGAGGCAAATCGATATTATGCGCATGCCTTCAATAACCTTTAGTGCAAGATAAAAAAATGCTACGACG
#                                                                   CTTTCCCGCTATATTAGAGGCAAAT
#                                                                            TATATTAGAGGCAAATCGATATTAT
#                           TTCCCTGCGTCGGTACGCAACCTTG
#                 GTACCGTGCCTTCCCTGCGTCGGTA
#                                                           CCTTCGTTCTTTCCCGCTATATTAG
#
#                                                                            TATATTAG - 3x alignment

#Goal is to take splices and align them against each other and/or a canonical sequence, then display said alignment to show degree of consensus.
#Will eventually need to be able to work with errors and partial alignment (establish thresholds for mismatch, establish consensus).
#Data structure?
#Should call Splices Fragments?
#For optimization may needto use numpy and vectorize?

def lcs(a, b):
    # generate matrix of length of longest common subsequence for substrings of both words
    # Will this generate non-contiguous overlaps?
    lengths = [[0] * (len(b)+1) for _ in range(len(a)+1)] #creates list of lists, with the length being that of one string+1, and the number of lists being that of the other string+1
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
            
    # read a substring from the matrix
    result = ''
    index = 0
    j = len(b)
    for i in range(1, len(a)+1):
        if lengths[i][j] != lengths[i-1][j]:
            result += a[i-1]
            index = i


    return result, (index - j), index


#Seq = 'TAGACTGACC'
#SubSeq = 'CTG'

#print(lcs(Seq, SubSeq), "longest common subsequence, length+1, start position")


Seq = 'TAGACTGACCTCGTATCGTACCGTGCCTTCCCTGCGTCGGTACGCAACCTTGGCCTGATCCTTCGTTCTTTCCCGCTATATTAGAGGCAAATCGATATTATGCGCATGCCTTCAATAACCTTTAGTGCAAGATAAAAAAATGCTACGACG'
SubSeq = 'TCTTTCCCGCTATATTAGAGGCAAA'

print(lcs(Seq, SubSeq))
print(Seq[(91-25):91], "Seq")
print(SubSeq, "SubSeq")
#print(Seq[lcs(Seq, SubSeq)[2]:lcs(Seq, SubSeq)[1]]) #just returns list of lists, not SubSeq from Seq
SubSeqStart = lcs(Seq, SubSeq)[2]
SubSeqEnd = lcs(Seq, SubSeq)[1]
print(Seq[SubSeqEnd:SubSeqStart], "derived Seq")
print(Seq[lcs(Seq, SubSeq)[1]:lcs(Seq, SubSeq)[2]], "nested derived Seq")