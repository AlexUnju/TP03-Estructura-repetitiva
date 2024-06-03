"""nro = int(input('Ingrese nro:'))
dsor = 2
es_primo = True
while dsor < nro and es_primo:
    resto = nro % dsor
    if resto == 0:
        es_primo = False
    else:
        dsor += 1
print('Es primo:', es_primo)  """


"""x = int(input('x:'))
y = 0
iter = x
while iter > 0:
    y += x
    iter -= 1
    print(y, iter)"""
"""
contador = 0
suma = 0
logico_max = True
continuar = 's'
while (continuar == 's'):
    nota = float(input('Ingrese nota:'))
    suma += nota
    contador += 1
    if logico_max:
        logico_max = False
        nota_max = nota
        pos_nota_max = contador
    else:
        if nota > nota_max:
            nota_max = nota
            pos_nota_max = contador
    continuar = input('Continuar (s/n):')
    promedio = suma/contador
    print('Promedio: ', promedio)
    print('Nota máxima: ', nota_max)
    print('Posición Máximo: ', pos_nota_max)
"""

    

#a) 10

nro = int(input('nro: '))
flag=not nro != 0 and nro <=10
suma=10
for i in range(1,nro,3):
    if flag:
        suma += i
    else:
        suma+= nro
    flag=not flag
print(suma)


