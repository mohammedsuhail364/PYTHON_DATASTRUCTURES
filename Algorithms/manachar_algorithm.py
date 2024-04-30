s = 'momracecar'
li = []
li1 = [0]
li.append('#')
for i in range(len(s)):
    li.append(s[i])
    li.append('#')
for x in range(1, len(li) - 2):
    i = 1
    count = 0
    while x - i >= 0 and x + i < len(li) and li[x - i] == li[x + i]:
        count += 1 
        i += 1
    li1.append(count)
max1 = max(li1)
s= li1.index(max1)
for i in range(s-max1,s+max1):
    if li[i]=='#':
        pass
    else:
        print(li[i],end='')