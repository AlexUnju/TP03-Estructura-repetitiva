"""2. En un supermercado se ingresa repetidamente el precio de un producto y el número de unidades a comprar por
cliente (un cliente solo puede comprar un tipo de producto). Validar que el precio del producto y el número de
unidades no debe ser negativo ni cero. A partir de 5 unidades se realiza un descuento del 10% sobre el total de
la compra. Los clientes se identifican por un número de orden consecutivo automático. Muestre el importe de
dinero que debe pagar el cliente. El proceso finaliza al terminar la jornada laboral. Mostrar el número de
orden del cliente que pagó el máximo importe y el total recaudado por el supermercado.
"""
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
         


        
