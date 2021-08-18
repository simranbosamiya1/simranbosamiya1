
def sort(l):
    
    swap = True
    while(swap):
        swap = False
        for i in range(0,len(l)-1):
            if(l[i+1]<l[i]):
                l[i+1], l[i] = l[i], l[i+1]
                swap = True
    return l
    
    
print(sort([1,4,3,6,5]))
