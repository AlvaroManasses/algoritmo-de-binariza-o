
# Projeto de Binarização de Imagens

Este projeto contém um script em Python (`binarization.py`) que permite transformar uma imagem colorida para escala de cinza e, em seguida, realizar a binarização (conversão para preto e branco) com base em um limiar definido. O código foi desenvolvido para ser executado no Google Colab, facilitando o upload e a visualização de imagens processadas diretamente no ambiente.

## Funcionalidades

- Conversão de imagens coloridas para tons de cinza.
- Binarização das imagens (preto e branco) usando um limiar ajustável.
- Visualização das imagens processadas.
- Download da imagem binarizada para o computador.

## Pré-requisitos

Antes de executar o script, certifique-se de que o ambiente Google Colab está configurado, pois ele oferece suporte para o upload e visualização de imagens.

## Instalação

1. Clone este repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/usuario/projeto-binarizacao-imagens.git
   ```

2. Abra o arquivo `binarization.py` no Google Colab para execução.

## Uso

### 1. Carregar a Imagem

O script solicita o upload da imagem no Google Colab. A imagem a ser binarizada (por exemplo, "lena-exemplo.png") pode ser selecionada a partir do seu computador.

### 2. Executar o Código

No Google Colab, execute as células do código em sequência. O código realiza as seguintes operações:

- **Upload da Imagem**: O código solicita o upload da imagem desejada para o Colab.
- **Conversão para Escala de Cinza**: A imagem carregada é convertida para tons de cinza.
- **Binarização**: Com o valor do limiar (definido em 127, mas ajustável), a imagem é transformada para preto e branco.
- **Visualização**: O script exibe a imagem original em escala de cinza e a imagem binarizada.
- **Download da Imagem Binarizada**: O script salva a imagem binarizada no ambiente Colab e permite baixá-la.

### 3. Ajuste de Parâmetros

- **Limiar de Binarização**: Caso deseje ajustar o limiar para a binarização, modifique o valor de `127` para o valor desejado na linha:
  ```python
  _, imagem_binarizada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)
  ```

## Exemplo de Uso

```python
# Código simplificado para binarização de imagem
import cv2
from google.colab import files
from matplotlib import pyplot as plt

uploaded = files.upload()  # Upload da imagem
imagem_colorida = cv2.imread("lena-exemplo.png")
imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)
_, imagem_binarizada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

plt.imshow(imagem_binarizada, cmap='gray')  # Exibir imagem binarizada
cv2.imwrite("lena-binarizada.png", imagem_binarizada)  # Salvar imagem
files.download("lena-binarizada.png")  # Baixar imagem
```


