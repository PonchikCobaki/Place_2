#n, m, k = map(int,input().split())
inp = open('input.txt',"r")
n, m, k = map(int,inp.readline().strip().split())
a = [str(0) for g in range(n)]
for i2 in range(n):
  a[i2] = inp.readline().strip()
t = 1
t1 = 0
k1 = 2
m2 = m - 1
s = ''
if k == 1:
  for i1 in range(n):
    if t1 == 1:
      break
    for j1 in range(m):
      if a[i1][j1] == '.':
        s = str(i1) + str(j1)
        #print(' '.join(s))
        with open('output.txt',"w") as out:
          out.write(' '.join(s))
        t1 += 1
        break
elif k > 1:
  for i in range(n):
    if t1 == 1:
      break
    #print('_____')
    #print('i | j')
    #print('¯¯¯¯¯')
    for j in range(m2):
      #print(i,'|',j)
      if a[i][j] == a[i][j+1] and a[i][j] == '.':
        t += 1
        #print(t,'t')

      if t == k and k <= 1+((n-1)-i):
        #print('#')
        t1 = 1
        t = 1

        for r in range(i+1, i+k):
          if t1 == 0:
            break
          for u in range(j-(k - k1), j+1):
            if t1 == 0:
              break
            #print(r, ':r', u, ':u')
            t1 = 0
            if  a[r][u+1] == a[r][u] and a[r][u] == '.':
              #print('Верно')
              t1 += 1

      if t1 == 1:
        #print(i, '', j-(k - k1))
        s = str(i) + str(j-(k - k1))
        #print(' '.join(s))
        with open('output.txt',"w") as out:
          out.write(' '.join(s))

        break

  if t1 != 1:
    #print(-1)
    with open('output.txt', "w") as out:
      out.write('-1')
else:
  #print('Дурачок?')
  with open('output.txt', "w") as out:
    out.write('Error!')