import pytesseract as ocr
import numpy as np
import cv2
#import capturar_frame
from itertools import combinations

from PIL import Image




def remove_quebra_linha(value):
    return ' '.join(value.splitlines())

def testar(roi, texto, img, report_path):
    resultado = False
    vetor_passar = roi
    combinacoes = combinations([0, 1, 2], 2)
    ocr.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imagem = Image.fromarray(img)

    # tipando a leitura para os canais de ordem RGB
    #imagem = Image.open(imagem_path).convert('RGB')
    #else:
    #imagem = capturar_frame.capturar()

    left = vetor_passar[0]
    top = vetor_passar[1]
    right = vetor_passar[2]
    bottom = vetor_passar[3]

    cropped = imagem.crop((left, top, right, bottom))

    phrase = ocr.image_to_string(cropped, lang='por')
    print(phrase)
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

    cv2.imwrite(report_path + '.jpg', img)
    return resultado