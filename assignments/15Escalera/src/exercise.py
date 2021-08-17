import math
def main():
    #escribe tu código abajo de esta línea
    h = float(input("Altura de la casa: "))
    angulo = int(input("Angulo en grados: "))

    angulo_radianes = math.radians(angulo)
    largo = round(h/math.sin(angulo_radianes))
    print("Largo de la escalera: "+str(largo))

if __name__ == '__main__':
    main()
