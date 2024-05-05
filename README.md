# TP03-Estructura-repetitiva
## Casos de Estudio
Analice, diseñe y codifique los siguientes enunciados en Python
### 1. Realice la prueba de escritorio o traza del algoritmo de Euclides utilizando el debugger de VSC.
#### Resolución:
```python
#EJECUTAR EL CODIGO CON EL DEBUGGER DE PYTHON:
a = int(55) #2366, 55
b = int(89) #273, 89

while b != 0:
    r = a % b
    a = b
    b = r
print('mcd:', a)
```
##
### 2. En un supermercado se ingresa repetidamente el precio de un producto y el número de unidades a comprar por cliente (un cliente solo puede comprar un tipo de producto). 
Validar que el precio del producto y el número de
unidades no debe ser negativo ni cero. A partir de 5 unidades se realiza un descuento del 10% sobre el total de
la compra. Los clientes se identifican por un número de orden consecutivo automático. Muestre el importe de
dinero que debe pagar el cliente. El proceso finaliza al terminar la jornada laboral. Mostrar el número de
orden del cliente que pagó el máximo importe y el total recaudado por el supermercado.

#### Resolución:
```python
recaudacion = 0;
ejecucion="S";
orden=0
logico_max=True

while ejecucion == "S":

    while True:
        precioProducto=int(input("Ingrese el precio del producto: "));
        cantidadProducto=int(input("Ingrese la cantidad de producto: "));

        if not precioProducto <=0 and not cantidadProducto<=0:
            break

    orden+=1
    precioTotal=precioProducto*cantidadProducto;
    
    if cantidadProducto > 5:
            descuento=(precioTotal)*(10/100);
            precioTotal-=descuento
            print(f"El cliente del orden {orden} es de {precioTotal} pesos (se aplicó descuento)");
    else:
        print(f"EL cliente del orden {orden} es de {precioTotal} pesos (no se aplicó descuento)");
        

    recaudacion = recaudacion + precioTotal;

    if logico_max:
     logico_max = False
     importe_max = precioTotal
     pos_importe_max = orden
    else:
        if precioTotal > importe_max:
            importe_max = precioTotal
            pos_importe_max = orden
    ejecucion = input('Continuar (s/n):');

print(f'El cliente {pos_importe_max} pagó el máximo importe ${importe_max}')
print(f'El total recaudado por el supermercado es ${precioTotal}')
```

##
## Ejercicios
### 1. Analizar y ejecutar los siguientes algoritmos en Python, luego realizar la prueba de escritorio: manual y automático utilizando el debugger del VSC.
##
| nro: 11 |
|------|
```python
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
```

| x: 3 |
|------|
```python
x = int(input('x:'))
y = 0
iter = x
while iter > 0:
    y += x
    iter -= 1
    print(y, iter)
```
| notas: 6, 7, 7, 9, 4 |
|------|
```python
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
```
##
### 2. Analizar y ejecutar los siguientes códigos en Python, luego debe cambiar la sentencia repetitiva for por la sentencia while
```python
tabla = int(input('Ingrese número:'))
print(f"Tabla de multiplicar del {tabla}")
for i in range(1, 10):
  print(f"{tabla} x {i} = {i*tabla}")
```
#### Resolución:
```python
while i < tabla:
  print(f"{tabla} x {i} = {i*tabla}")
  i+=1
```
Convertir en una versión while
```python
vi = int(input('vi:'))
vf = int(input('vf:'))
for ddo in range (vi, vf):
  divisores = 0
  print('')
  print(ddo,': ', end='')
  for dsor in range (2,ddo):
    if ddo % dsor == 0:
      print(dsor, ',', end='')
      divisores += 1
  if divisores == 0:
    print('es un número primo!', end='')
print('\n')
```
#### Resolución:
```python

```


##
### 3. Escribir un algoritmo que calcule y muestre todos los divisores de un número entero.
##
### 4. Escribir un algoritmo que calcule y muestre la división entera de dos números enteros ddo y dsor mediante restas sucesivas.
## 
### 5. Muestre todos los números primos que hay en un intervalo [inicial, final]
##
### 6. Leer números enteros, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
##
### 7. Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad). 
Por ejemplo si ingresa: 18, Debe mostrar: 1 año, 2 años, 3 años, …, 18 años
##
### 8. Realizar el código de un programa que solicite al usuario un número entero positivo (debe validar que cumpla ésta condición) y muestre por pantalla todos los números impares desde 1 hasta ese número. 
Resuelto lo anterior, comente las líneas de código y agregue otras que muestre los impares en forma decreciente desde el número ingresado hasta 1.
##
### 9. Escribir un programa que solicite ingresar la cantidad de alumnos de un curso y cada nota de los mismos. 
Finalmente deberá mostrar cuántos tienen notas mayores o iguales a 7 y cuántos menores a 7. También calcule y muestre el promedio de todos los valores ingresados.
## 
### 10. Una fábrica necesita un programa para calcular el salario y mostrar el detalle de sus empleados, los mismos tienen un sueldo básico común y se adiciona un 10% por cada aumento de categoría, un 5% por cada año de antigüedad. 
A todos los empleados se les descuenta un 11% por aportes jubilatorios y un 4% por obra social ambos del sueldo básico, y finalmente un aumento fijo de $200 en concepto de salario familiar por cada hijo menor de 18 años.
##
### 11. Diseñe un algoritmo que permita calcular las mediciones de temperaturas de una caldera, las mismas solo pueden ser mayores a 20 grados, si se ingresan valores inferiores a estos se debe volver a pedir el valor. Al final del proceso mostrar el promedio de todos los valores ingresados.
##
### 12. Pida al usuario una cantidad N de puntos a representar en el plano cartesiano. 
Lea el par de valores que representan las coordenadas (x,y), para cada punto indique en qué cuadrante se encuentra. Muestre al final la cantidad de puntos ingresados para cada cuadrante. La figura muestra un caso ejemplo, con el ingreso de valores (x,y) para 3 puntos.
##
### 13. Mediante un menú de opciones el usuario debe poder seleccionar una opción (1, 2 ó 3). 
Si elige una opción
incorrecta, se debe informar del error. Volver a mostrar las tres opciones luego de ejecutada cada opción,
permitiendo volver a elegir. Si elige las opciones 1 muestre un texto de Bienvenida, 2 mostrar el mayor de
cinco valores numéricos ingresados. Si elige la opción 3, el programa finalizará.
##
### 14. Hacer un algoritmo que sea Idem Caso de Estudio 2 pero un cliente puede comparar más de un tipo de producto.


