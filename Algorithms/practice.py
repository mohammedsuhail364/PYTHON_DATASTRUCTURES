count=0
nums=[2,11,10,1,3]
k=10
while sum(nums)>=k:
    count+=1
    if len(nums)>0:
        nums.remove(min(nums))
    

if len(nums)>0:
    print(count)
else:
    print(0)