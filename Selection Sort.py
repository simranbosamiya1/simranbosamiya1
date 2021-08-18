
def sort(l):
    
    for j in range(0,len(l)-1):
        minimum = j
        for i in range(j, len(l)):
            if(l[i]<l[minimum]):
                minimum = i
        l[j], l[minimum] = l[minimum], l[j]
        # l.remove(minimum)
        # l = l[:j] + [minimum] + l[j:]
        
    return l
    
    
print(sort([1,4,3,6,5]))
