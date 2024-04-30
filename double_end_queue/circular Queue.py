li = [1,2,3,4,5]
front = 0
rear=len(li)-1
def dequeue(lis,x):
    lis[x] = ''
    return lis
def enqueue(lis,rear,front):
    rear = (rear+1)%5
    if rear == front:
        print('Overflow')
        return lis
    else:
        lis[rear] = int(input('Enter Your Ele: '))
        return lis
for x in range(1,4):
    li = dequeue(li,x=front)
    front += 1
print(li)
for _ in range(0,4):
    li = enqueue(li,rear,front=front)
    rear = (rear+1)%5
print(li)