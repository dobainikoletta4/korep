num=int(input("Adj meg egy számot: "))
lista=[]
while num!=0:
    lista.append(num)
    num=int(input("Adj meg egy számot: "))
print(lista)

# Maximum: 6
# Minimum: 1

legkisebb= lista[0]
for szam in lista:
    if szam<legkisebb:
        legkisebb=szam
print("Minimum:", legkisebb)

