# li=[6,4,2,1,5]
# li1=[]
# count=0
# for y in range(len(li)):
#     for x in range(y,len(li)):
#         if li[y]>li[x]:
#             count+=1
#     li1.append(count)
#     count=0
# print(li1)
# li=[2,1,5,6,4]
# for i in range(len(li)):
#     if max(li)==li[0]:
#         print(1)
#     else:
#         pass
prices=list(map(int,input().split()))
org=prices
dup=sorted(prices)
ind=1
partitions=[]
while len(org)>0:
    if sorted(org[:ind])==dup[:ind]:
        partitions.append(org[:ind])
        org=org[ind:]
        dup=dup[ind:]
        ind=1
    else:
        ind+=1
print(partitions)
print(len(partitions))
