# Função para calcular a distância entre dois pontos no plano cartesiano
def calcular_distancia(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Recebendo as coordenadas dos pontos
x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))
x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))

# Calculando a distância entre os pontos
distancia = calcular_distancia(x1, y1, x2, y2)

# Verificando a distância e imprimindo o resultado
if distancia >= 10:
    print("longe")
else:
    print("perto")