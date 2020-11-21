noofchar=256
def maxdistinctchar(str,n):  #in this function we are returning maximum distinct char from a given string of size n.
    count=[0]*noofchar
    for i in range(n):
        count[ord(str[i])] +=1
    maxdist=0
    for i in range(noofchar):
        if(count[i]!=0):
            maxdist+=1
    return maxdist
def substring_with_maxdistinctchar(str):  #function for counting substring_with_maxdistinctchar
    n=len(str)                  
    maxd=maxdistinctchar(str,n)   #returns the maxdistinctchar
    minlen=n                      #initializes minlen as n 
    for i in range(n):
        for j in range(n):
            substring=str[i:j]          
            substringlen=len(substring)
            subdistchar=maxdistinctchar(substring,substringlen) #each and every substring is sent and maxdistinctchar is returned back
    if (substringlen <minlen and maxd==subdistchar):            #here we are checking whether the substringlen is min and max distinct char is equal to subdistchar
        minlen=substringlen
    return minlen

str=input()
leng=substring_with_maxdistinctchar(str)
print(leng-1)