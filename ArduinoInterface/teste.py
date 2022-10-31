import xml.etree.cElementTree as ET
from enum import Enum
import time
import pyfirmata
import cv2
import numpy as np
from matplotlib import pyplot as plt
cam_port = 0



porta_arduino = 'COM3' #Configuramos a porta como a porta COM4. Esta configuração deve ser alterada caso sua placa não se configure nesta porta.
placa = pyfirmata.Arduino(porta_arduino) #Criamos a variável board que realizará os comandos a partir daqui

from PyQt5.QtWidgets import QFileDialog
fname = 'filename1.xml'
#fname = QFileDialog.getOpenFileName(None, 'Open file', '.\\', "XML files (*.xml)")
#tree = ET.parse(fname[0])
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
    for tc in root:
        print(tc.attrib.get('name'))
        for ts in tc:
            if str(ts.attrib.get('name')) == str(TiposTeste.TIMER.value):
                print(ts.attrib.get('name') + ' --- ' + ts.text)
                time.sleep(int(ts.text)/1000)
            elif str(ts.attrib.get('name')) == str(TiposTeste.DOUT.value):
                print(ts.attrib.get('name') + ' --- ' +'Porta: ' + ts.attrib.get('porta') + ' Valor: '+ ts.text)
                placa.digital[int(ts.attrib.get('porta'))].write(int(ts.text))
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
                    for pt in zip(*loc[::-1]):
                        if len(loc[0] == 1) and (pt[0] >= roi_upper_left_x and pt[1] >= roi_upper_left_y and pt[0]+w <= roi_lower_right_x and pt[1]+h <= roi_lower_right_y):
                            cv2.rectangle(imagem, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                            status = True
                        else:
                            status = False
                    cv2.rectangle(imagem, (roi_upper_left_x, roi_upper_left_y), (roi_lower_right_x, roi_lower_right_y),(255, 0, 0), 2)
                    cv2.imwrite('res.png', imagem)

            elif str(ts.attrib.get('name')) == str(TiposTeste.OCR.value):
                pass
