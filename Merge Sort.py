
def sort(arr):
    if(len(arr)>1):
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        sort(L)
        sort(R)
        i=j=k=0
        while (i<len(L) and j<len(R)):
            if(L[i]<R[j]):
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
   
# 64, 34, 25, 12, 22, 11, 90, 
a = [1,4,3,6,5]
sort(a)
print(a)
