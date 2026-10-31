
Contador de Presença em Tempo Real

Um script simples em Python que utiliza a biblioteca OpenCV para capturar o vídeo da webcam, detectar rostos humanos em tempo real usando o algoritmo de Haar Cascade e exibir a contagem total de pessoas na tela.

🚀 Funcionalidades

• Detecção Facial em Tempo Real: Identifica rostos através da webcam com redimensionamento (scaleFactor=1.1) e filtro de falsos positivos (minNeighbors=6).
• Contagem Automática: Exibe um contador no topo da tela com o número atual de pessoas detectadas no enquadramento.
• Marcação Visual: Desenha retângulos verdes ao redor de cada rosto identificado e uma barra de destaque superior.
• Compatibilidade: Tratamento de erro automático para diferentes versões da biblioteca cv2.CascadeClassifier.

📋 Pré-requisitos

Certifique-se de ter o Python instalado em seu computador. Você precisará da biblioteca opencv-python.

Instalação da Dependência

Execute o comando abaixo no seu terminal para instalar o OpenCV:
bash
pip install opencv-python
Use code with caution.

💻 Como Executar

1. Salve o código principal em um arquivo, por exemplo, contador.py.
2. Conecte uma webcam ao seu computador.
3. No terminal, execute o script:
bash
python contador.py
Use code with caution.
4. Uma janela chamada "Contador de Presenca em Tempo Real" será aberta.
5. Para encerrar o programa e fechar a janela, clique na janela do vídeo e pressione a tecla q do seu teclado.

⚠️ Observações

• O arquivo de modelo Haar Cascade utilizado (haarcascade_frontalface_default.xml) já vem embutido por padrão nos pacotes oficiais do OpenCV.
• Certifique-se de que a sua webcam não esteja sendo usada por outro aplicativo no momento da execução.
Se precisar, posso te ajudar a:
• Salvar os dados da contagem em um arquivo de texto ou planilha.
• Adicionar um alerta sonoro ou envio de aviso quando o número de pessoas ultrapassar um limite.
• Adaptar o código para ler um arquivo de vídeo gravado em vez da webcam.
O que gostaria de ajustar no projeto?
