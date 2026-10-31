import cv2

# 1. Carrega o classificador com tratamento de erro para compatibilidade da versão 5
try:
    classificador_rosto = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
except AttributeError:
    classificador_rosto = cv2.cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# 2. Inicializa a webcam
webcam = cv2.VideoCapture(0)

print("Programa iniciado. Pressione 'q' para fechar.")

while True:
    sucesso, frame = webcam.read()
    if not sucesso:
        print("Erro ao acessar a webcam.")
        break

    # Converte para tons de cinza
    imagem_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta os rostos
    rostos_detectados = classificador_rosto.detectMultiScale(
        imagem_cinza, 
        scaleFactor=1.1, 
        minNeighbors=6,  
        minSize=(40, 40)  
    )

    # 3. Conta quantos rostos foram encontrados
    total_pessoas = len(rostos_detectados)

    # Desenha o retângulo em cada rosto
    for (x, y, largura, altura) in rostos_detectados:
        cv2.rectangle(frame, (x, y), (x + largura, y + altura), (0, 255, 0), 2)
        cv2.putText(frame, "Pessoa", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # 4. Cria uma barra preta no topo para dar destaque ao contador
    cv2.rectangle(frame, (0, 0), (320, 50), (0, 0, 0), -1)

    # 5. Escreve o texto com a contagem na tela
    texto_contador = f"Pessoas na sala: {total_pessoas}"
    cv2.putText(frame, texto_contador, (15, 32), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    # Mostra o resultado na janela
    cv2.imshow("Contador de Presenca em Tempo Real", frame)

    # Fecha o programa ao apertar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
