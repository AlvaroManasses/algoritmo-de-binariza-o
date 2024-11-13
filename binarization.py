# USAR EM AMBIENTE GOOGLE COLAB
# Importação das bibliotecas necessárias
import cv2
import numpy as np
from google.colab import files
from matplotlib import pyplot as plt

# Passo 1: Fazer o upload da imagem
uploaded = files.upload()

# Passo 2: Carregar a imagem colorida
imagem_colorida = cv2.imread("lena-exemplo.png")

# Passo 3: Converter a imagem para escala de cinza
imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

# Passo 4: Binarizar a imagem usando um limiar (threshold)
# Definindo o limiar como 127 (ajustável)
_, imagem_binarizada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

# Passo 5: Exibir a imagem original e a binarizada no Colab
plt.figure(figsize=(10,5))

# Exibe a imagem em tons de cinza
plt.subplot(1, 2, 1)
plt.imshow(imagem_cinza, cmap='gray')
plt.title('Imagem em Escala de Cinza')
plt.axis('off')

# Exibe a imagem binarizada
plt.subplot(1, 2, 2)
plt.imshow(imagem_binarizada, cmap='gray')
plt.title('Imagem Binarizada')
plt.axis('off')

plt.show()

# Passo 6: Salvar a imagem binarizada
cv2.imwrite("lena-binarizada.png", imagem_binarizada)

# Baixar a imagem binarizada para o computador
files.download("lena-binarizada.png")
