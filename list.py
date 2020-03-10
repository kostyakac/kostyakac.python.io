lst = [int(i) for i in input().split()]
x = int(input())
c=0
if x not in lst:
  print('Отсутствует')
else:
  for i in range(0,len(lst)):
     if lst[i] == x:
       c=c+1;
print(c)