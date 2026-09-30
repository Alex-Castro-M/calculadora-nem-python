print("Calculadora NEM")

objetivo = float(input("Dime el promedio NEM que aspiras tener: "))
curso = int(input("Dime en qué curso estás actualmente (ej: 1, 2, 3, 4): "))

NEMnes = 0.0
NEM = 0.0

if curso == 1:
    pro1 = float(input("Dime tu promedio de 1ero medio: "))
    NEMnes = ((objetivo * 4) - pro1) / 3
    print("Necesitas este promedio desde 2do a 4to medio para lograr tu objetivo: ", round(NEMnes, 1))

elif curso == 2:
    pro1 = float(input("Dime tu promedio de 1ero medio: "))
    pro2 = float(input("Dime tu promedio de 2do medio: "))
    NEMnes = ((objetivo * 4) - (pro1 + pro2)) / 2
    print("Necesitas este promedio desde 3ro a 4to medio para lograr tu objetivo: ", round(NEMnes, 1))

elif curso == 3:
    pro1 = float(input("Dime tu promedio de 1ero medio: "))
    pro2 = float(input("Dime tu promedio de 2do medio: "))
    pro3 = float(input("Dime tu promedio de 3ro medio: "))
    NEMnes = ((objetivo * 4) - (pro1 + pro2 + pro3))
    print("Necesitas este promedio de 4to medio para lograr tu objetivo: ", round(NEMnes, 1))

elif curso == 4:
    pro1 = float(input("Dime tu promedio de 1ero medio: "))
    pro2 = float(input("Dime tu promedio de 2do medio: "))
    pro3 = float(input("Dime tu promedio de 3ro medio: "))
    pro4 = float(input("Dime tu promedio de 4to medio: "))
    NEM = (pro1 + pro2 + pro3 + pro4) / 4
    print("Tu promedio NEM es de: ", round(NEM, 1))

    if NEM >= objetivo:
        print("¡Felicidades, lo conseguiste!")
    else:
        print("Lo siento, no lo alcanzaste")

else:
    print("Curso inválido, no existe. El curso es de 1 a 4")

if curso in [1, 2, 3]:
    if NEMnes > 7.0:
        print("Perdón, es físicamente imposible su objetivo")
        print("Tendría que sacar nota: ", round(NEMnes, 1), ", lo cual es físicamente imposible ;-;")
