def append_at_rear(i):
    li.append(i)
def pop_at_rear(i):
    li.remove(i)
def append_at_front(i):
    li.insert(0,i)
def pop_at_front(i):
    li.pop(0)
li=[]
insert_no=int(input("Enter your number: "))
print("1)Append_at_front\n2)Append_at_rear\n3)Pop_at_front\n4)pop_at_rear\n5)Are you Want to exit")
choice=int(input("Enter your choice: "))
# while True:
if choice==1:
    append_at_front(insert_no)
    print(li)
elif choice==2:
    append_at_rear(insert_no)
    print(li)
elif choice==3:
    try:
        pop_at_front(insert_no)
        print(li)
    except Exception:
        print('UnderFlow')
elif choice==4:
    try:
        pop_at_rear(insert_no)
    except Exception:
        print("UnderFlow")
# elif choice==5:
#     break
