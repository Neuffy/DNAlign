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

#mylist = [5, 9, 13, 15, 16]
#n = 14
#i=0
#mylist[i:i] = [n]
#print(mylist)

a = [5, 15, 13, 8, 16]
b = a
print("a =", a)
print("b =", b)
t = [4, 2]
r = [4]
a[1:3] = t
b[1:3] = r
print("a =", a)
print("b =", b)

f = [5, 15, 13, 8, 16]
print("f =", f)
z = [4, 2]
f[1:3] = z
print("f =", f)

# slice 1 to 3 (15 and 13) has been replaced by contents of t