import pickle
import random
print('Введите название файла, в котором содержится модель.')
t=input()
print("Введите префикс")
l=input().split()
print('Введите кол-во требуемых постфиксов')
d=int(input())
l=tuple(l)
if "pkl" in t:
    t=t
else:
    t+='.pkl'
with open(t,'rb') as file:
    s=pickle.load(file)
    y=sorted(s[l].items(),reverse=True)
    print(y[0][0],end=" ")
    for i in range(d-1):
        w=random.choice(y)
        print(w[0],end=" ")
