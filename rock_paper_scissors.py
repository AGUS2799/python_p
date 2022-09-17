from random import randint

def rock_paper_scissors():
    player = None
    player_points = 0
    pc_points = 0
    choice = ["piedra","papel","tijera"]
    pc = choice[randint(0,2)]
    player = input("Tu eleccion: ").lower()

    print("\n****Bienvenido al juego de Piedra, Papel, o tijera****\n"
            "--Para salir escriba end--\n")

    while player != "end":
        if player_points == 3:
            print("Sos god pa, segui asi")
            break
        if pc_points == 3:
            print("Sos muy malo, te gane")
            break

        player = input("Tu eleccion: ").lower()
        if player == "papel" or player == "tijera" or player == "piedra":
            if player == pc:
                print(f"La PC eligio: {pc}\n")
                print("Empate\n")
                print(f"puntos del cpu: {pc_points}\n"
                f"puntos del jugador: {player_points}")

            elif player == "piedra" and pc == "papel":
                print(f"La PC eligio: {pc}\n")
                print("Gano la PC\n")
                pc_points += 1
                print(f"puntos del cpu: {pc_points}\n"
                f"puntos del jugador: {player_points}")

            elif player == "piedra" and pc == "tijera":
                print(f"La PC eligio: {pc}\n")
                print("Ganaste!!\n")
                player_points += 1
                print(f"puntos del cpu: {pc_points}\n"
                f"puntos del jugador: {player_points}")

            elif player == "papel" and pc == "piedra":
                print(f"La PC eligio: {pc}\n")
                print("Ganaste!!\n")
                player_points += 1
                print(f"puntos del cpu: {pc_points}\n"
                f"puntos del jugador: {player_points}")

            elif player == "papel" and pc == "tijera":
                print(f"La PC eligio: {pc}\n")
                print("Gano la PC\n")
                pc_points += 1
                print(f"puntos del cpu: {pc_points}\n"
                f"puntos del jugador: {player_points}")

            elif player == "tijera" and pc  == "piedra":
                print(f"La PC eligio: {pc}\n")
                print("Gano la PC\n")
                pc_points += 1
                print(f"puntos del cpu: {pc_points}\n"
                f"puntos del jugador: {player_points}")

            elif player == "tijera" and pc == "papel":
                print(f"La PC eligio: {pc}\n")
                print("Ganaste!!\n")
                player_points += 1
                print(f"puntos del cpu: {pc_points}\n"
                f"puntos del jugador: {player_points}")
                
        elif player == "end":
            print("Hasta la proxima cabezón!")
        
        else:
            print("Debes elegir entre piedra, papel o tijera")

rock_paper_scissors() 


