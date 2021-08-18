

def sort(l):
    for i in range(0, len(l)):
        x = l[i]
        j = i - 1
        while(j>=0 and l[j]>x):
            l[j+1] = l[j]
            j = j - 1
        l[j+1] = x
    return l
    
print(sort([1,4,5,3,2]))
