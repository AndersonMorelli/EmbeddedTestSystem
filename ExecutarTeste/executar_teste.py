import xml.etree.cElementTree as ET
from enum import Enum
import time
import pyfirmata
import cv2
import numpy as np
from ImageProcessing import tesseract_temp

cam_port = 0
#ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

try:
    placa = pyfirmata.Arduino("COM5")
except:
    print('Arduino não conectado.')
    arduino_conectado = False
else:
    arduino_conectado = True


fname = 'tesseract.xml'
tree = ET.parse(fname)
class TiposTeste(Enum):
    TIMER = 'TIMER'
    SERIAL = 'SERIAL'
    DOUT = 'DOUT'
    DIN = 'DIN'
    PATTERN = 'PATTERN'
    OCR = 'OCR'

lista_portas = []

root = tree.getroot()
if arduino_conectado:
    if root is not None:
        for tc in root:
            for ts in tc:
                if str(ts.attrib.get('name')) == str(TiposTeste.DOUT.value):
                    if str(ts.attrib.get('name')) not in lista_portas:
                        placa.digital[int(ts.attrib.get('porta'))].mode = pyfirmata.OUTPUT
                if str(ts.attrib.get('name')) == str(TiposTeste.DIN.value):
                    if str(ts.attrib.get('name')) not in lista_portas:
                        placa.digital[int(ts.attrib.get('porta'))].mode = pyfirmata.INPUT
    it = pyfirmata.util.Iterator(placa)
    it.start()

if root is not None:
    contador_tc = 0
    for tc in root:
        print("Testcase " + str(contador_tc) + ': ' + tc.attrib.get('name'))
        contador_ts = 0
        for ts in tc:
            complemento=''
            resultado_teste = 'PASS ||| '
            if str(ts.attrib.get('name')) == str(TiposTeste.TIMER.value):
                #print(ts.attrib.get('name') + ' --- ' + ts.text)
                complemento = ' ' + ts.text + 'ms'
                time.sleep(int(ts.text)/1000)
            elif str(ts.attrib.get('name')) == str(TiposTeste.DOUT.value):
                #print(ts.attrib.get('name') + ' --- ' +'Porta: ' + ts.attrib.get('porta') + ' Valor: '+ ts.text)
                if arduino_conectado:
                    placa.digital[int(ts.attrib.get('porta'))].write(int(ts.text))
                    complemento = ' Porta: ' + ts.attrib.get('porta') + ' Valor: ' + ts.text
            elif str(ts.attrib.get('name')) == str(TiposTeste.SERIAL.value):
                pass
            elif str(ts.attrib.get('name')) == str(TiposTeste.DIN.value):
                pass
            elif str(ts.attrib.get('name')) == str(TiposTeste.PATTERN.value):
                template = cv2.imread(ts.attrib.get('file_name'),0)
                w, h = template.shape[::-1]

                roi_upper_left_x = str(ts.attrib.get('roi_upper_left')).split(';')[0]
                roi_upper_left_y = str(ts.attrib.get('roi_upper_left')).split(';')[1]
                roi_lower_right_x = str(ts.attrib.get('roi_lower_right')).split(';')[0]
                roi_lower_right_y = str(ts.attrib.get('roi_lower_right')).split(';')[1]
                frame = cv2.VideoCapture(cam_port)
                result, imagem = frame.read()
                if result:
                    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
                    res = cv2.matchTemplate(imagem_cinza, template, cv2.TM_CCOEFF_NORMED)
                    threshold = 0.8
                    loc = np.where(res >= threshold)
                    #####PRECISO VER COMO ESTÁ ESSA PARTE NO CODIGO QUE FIZ POR FORA#
                    for pt in zip(*loc[::-1]):
                        if len(loc[0] == 1) and (pt[0] >= roi_upper_left_x and pt[1] >= roi_upper_left_y and pt[0]+w <= roi_lower_right_x and pt[1]+h <= roi_lower_right_y):
                            cv2.rectangle(imagem, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                            status = True
                        else:
                            status = False
                    cv2.rectangle(imagem, (roi_upper_left_x, roi_upper_left_y), (roi_lower_right_x, roi_lower_right_y),(255, 0, 0), 2)
                    cv2.imwrite('res.png', imagem)
                    ##################################################################
                else:
                    complemento = 'Problema com a câmera'

            elif str(ts.attrib.get('name')) == str(TiposTeste.OCR.value):
                roi = [int(ts.attrib.get('left')), int(ts.attrib.get('top')), int(ts.attrib.get('right')), int(ts.attrib.get('botton'))]
                resultado = tesseract_temp.testar(roi, str(ts.attrib.get('texto')), str(ts.attrib.get('filename')))
                if resultado == False:
                    resultado_teste = 'FAIL ||| '
                    complemento = ' Texto não encontrado'


            #Exibe o resultado do teststep
            print(resultado_teste + "Step " + str(contador_ts) + ': ' + ts.attrib.get('name') + complemento)

