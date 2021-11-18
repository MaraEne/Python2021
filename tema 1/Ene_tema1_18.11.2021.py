l = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

lsecond = l[::]
print(lsecond)
lsecond.sort()
print(lsecond)

lsecond.sort(reverse = True)
print(lsecond)

lsecond.sort()
my_sliced_list = lsecond[1::2]
print(my_sliced_list)

my_sliced_list = lsecond[::2]
print(my_sliced_list)


for i in range(1,len(lsecond)):
    if l[i]%3==0:
        print(l[i])
