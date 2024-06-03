cantSimple=0
cantCertificado=0
pesoTotal=0
precioS=50
precioC=200
encomienda=1


    
while(encomienda > 0):
    tipo=str(input("Ingrese el tipo: S o C: ")).upper()
    peso=int(input("Ingrese el peso en kg[rango 0-10]: "))

    if tipo == "S" or "C":
        if 1<peso<=10:
            if tipo == "S":
                if 1<=peso<2:
                     recargo= precioS*peso
                     precioTotal= precioS*peso+(recargo*0.10)
                     cantSimple+=1
                elif 2<=peso<5:
                     recargo= precioS*peso
                     precioTotal=precioS*peso+(recargo*0.20)
                     cantSimple+=1
                else:
                     recargo=precioS*peso
                     precioTotal=precioS*peso+(recargo*0.50)
                     cantSimple+=1
            elif tipo == "C":
                if 1<=peso<2:
                    recargo= precioC*peso
                    precioTotal= precioC*peso+(recargo*0.10)
                    cantCertificado+=1
                elif 2<=peso<5:
                    recargo= precioC*peso
                    precioTotal=precioC*peso+(recargo*0.20)
                    cantCertificado+=1
                else:
                    recargo=precioC*peso
                    precioTotal=precioC*peso+(recargo*0.50)
                    cantCertificado+=1
        else:
            print("el peso no puede ser mayor que 10kg")
    else:
        print("error al ingresar el tipo de encomienda, vuelve a ingresar S o C")
        
    print(f"El precio total de la encomienda es {precioTotal}")
    pesoTotal+=peso;
    

    
    encomienda=int(input("Ingrese el número de encomienda para continuar: "))
4

print(f"El peso total es de {pesoTotal}")
print(f"la cantidad de encomiendas simples es de: {cantSimple} y la de certificadas es de: {cantCertificado}")

    



    
