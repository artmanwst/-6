import re
import sys
import pickle
print("Введите название файла, для обучения модели или введите 0, если хотите обучать модель построчно.")
t=input()
k=[]
if t!='0':
    with open(t,'r',encoding='utf-8') as file:
        
        for i in file:
            i=i.rstrip('\n')
            z=re.split(r'[.?!]',i)
            if z[len(z)-1]=='':
                del z[len(z)-1]
            if len(z)!=0:
                k.append(z)
else:
    for i in sys.stdin:
        i=i.rstrip('\n')
        z=re.split(r'[.?!]',i)
        if z[len(z)-1]=='':
            del z[len(z)-1]
        if len(z)!=0:
            k.append(z)

spisok=[]
for j in k:
    for i in j:
        i=i.replace(':'," ")
        i=i.replace(', '," ")
        i=i.replace(" - "," ")
        i=i.replace("– ","")
        i=i.replace(" – "," ")
        i=i.replace("... "," ")
        i=i.replace('*',' ')
        i=i.replace('['," ")
        i=i.replace(']'," ")
        i=i.replace('('," ")
        i=i.replace(')'," ")
        i=i.lower()
        i=i.split()
        spisok.append(i)
co=0
print('Вы хотите создать новый словарь?(Ответьте "Новый"). Если хотите добавить элементы к уже обученной модели(Ответьте "Старый")')
fr=input()
if fr==("Новый"):
        v={}
elif fr==("Старый"):
    we=input('Введите расположение уже обученной модели:')
    try:
        print(we)
        with open(we,'rb') as file:
            sl=pickle.load(file)
            v=sl
            co+=1
    except:
        print("Такого файла нет, создаем новый словарь")
        v={}
for i in spisok:
    for j in range(0,len(i)-1): #все элементы кроме последнего
        for o in range(1,len(i)-j):#длина строки как префикса оценивается  длиной минус начало префикса
            p=(i[j:o+j])
                        
            if tuple(p) not in v:
                v[tuple(p)]={}
                v[tuple(p)][i[o+j]]=1
            else:
                if i[o+j] not in v[tuple(p)]:
                    v[tuple(p)][i[o+j]]=1
                else:
                    v[tuple(p)][i[o+j]]+=1   
print(v)

if co==1:
    with open(we,"wb") as file:
        pickle.dump(v,file)
else:
    print("Введите название файла, для сохранения модели в формате x.pkl, где x-название файла.")
    y=input()
    if "pkl" in y:
        y=y
    else:
        y=y+".pkl"
    with open(y,"wb") as file:
        pickle.dump(v,file)
    

