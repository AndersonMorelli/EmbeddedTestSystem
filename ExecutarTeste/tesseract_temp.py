import pytesseract as ocr
import numpy as np
import cv2

from PIL import Image
ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# tipando a leitura para os canais de ordem RGB
imagem = Image.open('teste.jpg').convert('RGB')

# convertendo em um array editável de numpy[x, y, CANALS]
npimagem = np.asarray(imagem).astype(np.uint8)  

# diminuição dos ruidos antes da binarização
npimagem[:, :, 0] = 0 # zerando o canal R (RED)
npimagem[:, :, 2] = 0 # zerando o canal B (BLUE)

# atribuição em escala de cinza
im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY) 

# aplicação da truncagem binária para a intensidade
# pixels de intensidade de cor abaixo de 127 serão convertidos para 0 (PRETO)
# pixels de intensidade de cor acima de 127 serão convertidos para 255 (BRANCO)
# A atrubição do THRESH_OTSU incrementa uma análise inteligente dos nivels de truncagem
ret, thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 

# reconvertendo o retorno do threshold em um objeto do tipo PIL.Image
binimagem = Image.fromarray(thresh)
#cv2.imshow('aaa',thresh)
left = 30
top = 265
right = 450
bottom = 340
# chamada ao tesseract OCR por meio de seu wrapper
#phrase = ocr.image_to_string(binimagem, lang='por')
#cropped = im2[250:340,20:500]
cropped = imagem.crop((left, top, right, bottom))
cropped.show()
phrase = ocr.image_to_string(cropped, lang='por')

# impressão do resultado
print("Frase: " + phrase) 
