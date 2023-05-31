my_str = '01011101000110'

my_list = [int(x) for x in str(my_str)]

n = 2
my_duolist = [my_str[i:i+n] for i in range(0, len(my_str), n)]

nucDict = {
    "00": "A",
    "01": "T",
    "10": "C",
    "11": "G"
}

my_nuclist = [nucDict[my_duolist] for my_duolist in my_duolist]




print(my_str)
print(my_list)
print(my_duolist)
print(my_nuclist)
