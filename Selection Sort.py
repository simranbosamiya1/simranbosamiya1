

def sort(l):
    minimum = l[0]
    
    for j in range(0,len(l)-1):
        minimum = l[j]
        for i in range(j, len(l)):
            if(l[i]<minimum):
                minimum = l[i]
        l.remove(minimum)
        l = l[:j] + [minimum] + l[j:]
        
    return l
    
print(sort([1,4,5,3,2]))
