import pytesseract as ocr
import numpy as np
import cv2
from itertools import combinations

from PIL import Image

def remove_quebra_linha(value):
    return ' '.join(value.splitlines())

def testar(roi, texto, imagem_path = None):
    resultado = False
    vetor_passar = roi

    combinacoes = combinations([0, 1, 2], 2)


    ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # tipando a leitura para os canais de ordem RGB
    if imagem_path is not None:
        imagem = Image.open(imagem_path).convert('RGB')
    else:
        #Preciso colocar a captura da imagem pela camera aqui dentro
        pass
    left = vetor_passar[0]
    top = vetor_passar[1]
    right = vetor_passar[2]
    bottom = vetor_passar[3]
    # chamada ao tesseract OCR por meio de seu wrapper

    #cropped = binimagem.crop((left, top, right, bottom))
    cropped = imagem.crop((left, top, right, bottom))
    #cropped.show()

    phrase = ocr.image_to_string(cropped, lang='por')
    phrase = remove_quebra_linha(phrase)
    if phrase.strip() == texto:
        resultado = True

    if resultado == False:
        for i in combinacoes:
            npimagem = np.asarray(cropped).astype(np.uint8)
            # diminuição dos ruidos antes da binarização
            #npimagem[:, :, 0] = 0 # zerando o canal R (RED)
            npimagem[:, :, i[0]] = 0
            npimagem[:, :, i[1]] = 0

            # atribuição em escala de cinza
            im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY)

            # aplicação da truncagem binária para a intensidade
            # pixels de intensidade de cor abaixo de 127 serão convertidos para 0 (PRETO)
            # pixels de intensidade de cor acima de 127 serão convertidos para 255 (BRANCO)
            # A atrubição do THRESH_OTSU incrementa uma análise inteligente dos nivels de truncagem
            ret, thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

            # reconvertendo o retorno do threshold em um objeto do tipo PIL.Image
            binimagem = Image.fromarray(thresh)

            phrase = ocr.image_to_string(binimagem, lang='por')
            phrase = remove_quebra_linha(phrase)

            if phrase.strip() == texto:
                resultado = True
    return resultado