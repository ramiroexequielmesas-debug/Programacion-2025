import random
guessIA: int=(random.randint(1,3))
guessUS:int=int(input("seleccione su jugada, 1(piedra), 2(papel), 3(tijera)"))
rond: int=0
wIA: int=0
wUS: int=0

while rond<5 or wIA<3 or wUS<3:
    if guessIA==guessUS:
        rond+=1
        print("empate")
        guessIA: int=(random.randint(1,3))
        guessUS:int=int(input("seleccione su jugada, 1(piedra), 2(papel), 3(tijera)"))
   
    if guessIA==1 and guessUS==2:
        rond+=1
        print("¡Ganaste!")
        wUS+=1
        guessIA: int=(random.randint(1,3))
        guessUS:int=int(input("seleccione su jugada, 1(piedra), 2(papel), 3(tijera)"))
    elif guessIA==2 and guessUS==1:
        rond+=1
        print("¡perdiste!")
        wIA+=1
        guessIA: int=(random.randint(1,3))
        guessUS:int=int(input("seleccione su jugada, 1(piedra), 2(papel), 3(tijera)"))
   
    if guessIA==1 and guessUS==3:
        rond+=1
        print("¡Perdiste!")
        wIA+=1
        guessIA: int=(random.randint(1,3))
        guessUS:int=int(input("seleccione su jugada, 1(piedra), 2(papel), 3(tijera)"))
    elif guessIA==2 and guessUS==3:
        rond+=1
        print("¡Ganaste!")
        wUS+=1
        guessIA: int=(random.randint(1,3))
        guessUS:int=int(input("seleccione su jugada, 1(piedra), 2(papel), 3(tijera)"))
    
    if guessIA==3 and guessUS==1:
        rond+=1
        print("¡Ganaste!")
        wUS+=1
        guessIA: int=(random.randint(1,3))
        guessUS:int=int(input("seleccione su jugada, 1(piedra), 2(papel), 3(tijera)"))
    elif guessIA==3 and guessUS==2:
         rond+=1
         print("¡Perdiste!")
         wIA+=1
         guessIA: int=(random.randint(1,3))
         guessUS:int=int(input("seleccione su jugada, 1(piedra), 2(papel), 3(tijera)"))
