print("=== RUN LAB ===")
distancia = float(input("Distancia percorrida: (km):"))
tempo_minutos = float(input("Tempo total: (minutos): "))

if distancia > 0 and tempo_minutos > 0:
    print("Os dados são validos")
    ritmo = tempo_minutos/distancia
    tempo_horas = tempo_minutos/60
    velocidade_media = distancia/tempo_horas
    print("=== relátorio da corrida===")
    print (f"Distância:{distancia}km")
    print(f"Tempo: {tempo_minutos} minutos")
    print (f"Ritmo Médio: {ritmo:.2f} min/km")
    print(f"Velocidade Média: {velocidade_media:.2f} km/h")  
else:
    print("Os dados são inválidos")

if ritmo < 5:
    print("Ritmo Rápido")
elif ritmo < 6 :
    print("Ritmo Moderado")
else:
    print("Ritmo Tranquilo")

dificuldade = input("Digite a dificuldade da corrida (Fácil, Médio, Dificil): ")

