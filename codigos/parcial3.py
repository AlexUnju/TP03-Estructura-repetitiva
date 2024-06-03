reserva=1
reservaEstandar=0
precio=0;
continuar = "s"
logicoMax=True

while(True):
    precio=int(input("INgrese el precio rango 150 - 300"))
    if 150<=precio<=300:
        break
    else: 
        print("El precio debe estar en el rango de 150 a 300")

while(continuar == "s"):
    cantidadNoche= int(input("Ingrese la cantidad de Noches: "))
    if cantidadNoche > 0:
        tipo=str(input("Ingrese el tipo de hotel estandar ó lujo: ")).lower()
        if tipo == "estandar":
            precioTotal = precio*cantidadNoche
            reservaEstandar+=1

        elif tipo == "lujo":
            if 1<=cantidadNoche<5:
                recargo=precio*cantidadNoche
                precioTotal=precio*cantidadNoche+(recargo*0.20)
            else:
                precioTotal=precio*cantidadNoche
        else:
            print("Error, al ingresar el tipo de reserva")

        print(f"EL monto a pagar es de {precioTotal}")
    else:
        print("la cantidad de noches debe ser mayor que cero")
    
    if logicoMax:
        reservaMayorIngreso=precioTotal
        reservaMax=reserva
        logicoMax=False

    if precioTotal > reservaMayorIngreso:
        reservaMayorIngreso=precioTotal
        reservaMax=reserva
    reserva+=1
    continuar=str(input("¿Continuar? s/n"))



print(f"la cantidad de habitaciones reservadas es de {reservaEstandar}")
print(f"la reserva {reservaMax} generó el mayor gasto de { reservaMayorIngreso }")


