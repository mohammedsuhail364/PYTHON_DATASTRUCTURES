even=False
odd=False
li=[]
low=1
high=10
k=1

for i in range(low,high+1):
    even=False
    odd=False
    if i%k==0:
        l=i
        while i>0:
            s=i%10
            if s%2==0:
                even=True
            else:
                odd=True
            i//=10
        if odd and even :
            li.append(l)
print(li)