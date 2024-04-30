li=[]
n=21
import sys
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n and((i%3==0 and j%5==0) or (i%5==0 and j%3==0)):
            if i%3==0:
                s=i//3
                li.append(('5'*3)*s)
            elif i%5==0:
                s1=i//5
                li.append(('3'*5)*s1)
            elif j%3==0:
                s2=j//3
                li.append(('5'*3)*s2)
            elif j%5==0:
                s3=j//5
                li.append(('3'*5)*s3)
        if len(li)==2:
            break
        
if li:
    print(li)
else:
    print(-1)

'''
1,20
2,19
3,18
4,17
5,16
6,15
'''