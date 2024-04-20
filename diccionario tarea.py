#aispuro garcia alan yair

#1 
a={
    "A":1,
    "B":2,
    "C":3
}
b = 3
for i in a:
    a[i]=a[i]*b
print(a)


#2
a.pop("A")
print(a)


#3
c = [1,2,3,4,5,6,7]
c2 = [1,4,9,16,25,36,49]
cc = {}
for i in range(len(c)):
    cc[str(c[i])]=c2[i]
print(cc)


#4
d={
    "C":3,
    "B":2,
    "A":1
}
d1=sorted(d)
d2={}
for i in range(len(d1)):
    d2[d1[i]]=d[d1[i]]
print(d2)


#5
e = {
    'f':199,
    'e':0.2,
    'c':4,
    'a':1,
    'b':2,
    'd':16,
    'g':0.5
}
emin='f'
emax='f'
for i in e:
    if e[i]<e[emin]:
        emin=i
    if e[i]>e[emax]:
        emax=i
print(f"max = {e[emax]}, min = {e[emin]}")


#6
f = ["Seviche","Aguacate","Wacamola","Cilantro","Berenjena"]
ff = {}
for i in range(len(f)):
    ff[str(i)]=f[i]
print(ff)


#7
g = {
    'a':1,
    'b':2,
    'c':3,
    'd':1,
    'e':2
}
gg = {}
for i,j in g.items():
    if j not in gg.values():
        gg[i]=j
print(gg)


#8
def vacio(x):
    if len(x)==0:
        print('Vacio')
    else:
        print("No vacio")
h = {}
vacio(g)
vacio(h)


#9
k = [{'Matematicas': 90, 'ciencia': 92}, {'matematicas': 89, 'ciencia': 94}, {'Matematicas': 92, 'ciencia': 88}]
k1 = []
for i in k:
    for j in i:
        k1.append(i[j])
print(k1)


#10
k2 = []
for i in k:
    for j in i:
        if j == 'ciencia':
            k2.append(i[j])
print(k2)


#11
k3 = []
for i in k:
    for j in i:
        if j == 'Matematicas' or j == "matematicas":
            k3.append(i[j])
print(k3)


#12
def longitud(x):
    print(len(x))
longitud(g)
longitud(h)


#13
def prof(x):
    return 1 + (max(map(prof,x.values())) if x else 0)
l = {'a':{'a':{"a":{}}}}
print(f'profundidad = {prof(l)}')


#14
p = {'1':'fisica','2':'matematica','3':'arquitectura','4':'bioquimica','5':'quimica'}
p1 = [0,1,4]
p2 = 0
for i in p:
    if p2 in p1:
        print(p[i])
    p2+=1


#15
m = {1: 'rojo', 2: 'verde', 3: 'negro', 4: 'blanco', 5: 'negro'}
m1=[]
mm = []
for i in m:
    m1 = [i,m[i]]
    mm.append(m1)
print(mm)


#16
def filtpar(x):
    y = []
    z = []
    for i in x:
        y = x[i]
        z = [i for i in y if i%2!=0]
        x[i]=z
o1={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
o2={'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
o3={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
o4={'V': [], 'VI': [], 'VII': [2]}
filtpar(o1)
print(o1)
filtpar(o2)
print(o2)
filtpar(o3)
print(o3)
filtpar(o4)
print(o4)