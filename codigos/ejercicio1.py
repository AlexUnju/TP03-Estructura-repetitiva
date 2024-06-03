"""
nro = int(input('Ingrese nro:'))
dsor = 2
es_primo = True
while dsor < nro and es_primo:
    resto = nro % dsor
    if resto == 0:
        es_primo = False
    else:
        dsor += 1
print('Es primo:', es_primo)
"""
#nro    dsor       es_primo      resto            while dsor < nro and es_primo            if resto == 0          
#11      2         True          1                True and True = True                     False
#11      3         True          2                True and True = True                     False
#11      4         True          3                True and True = True                     False
#11      5         True          1                True and True = True                     False
#11      6         True          5                True and True = True                     False
#11      7         True          4                True and True = True                     False
#11      8         True          3                True and True = True                     False
#11      9         True          2                True and True = True                     False
#11      10        True          1                True and True = True                     False
#11      11                                       False and True = False
#print("Es primo:", es_primo)


"""
x = int(input('x:'))
y = 0
iter = x
while iter > 0:
    y += x
    iter -= 1
    print(y, iter)
"""
#x       y         iter        while iter>0         print
#3       0          3          True                 3,2
#3       3          2          True                 6,1
#3       6          1          True                 9,0
#3       9          0          False                

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

#nota      contador     suma       logico_max        nota_max          pos_nota_max        continuar
#6         0            0          True              6                 1                   s
#7         1            6          False             7                 2                   s
#7         2            13         False             7                                     s
#9         3            20         False             9                 3                   s
#4         4            29         False                               4                   n
#          5            33                                                                 
#print("Promedio", 6.6)
