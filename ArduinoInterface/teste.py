import xml.etree.cElementTree as ET
from enum import Enum
import time
import pyfirmata
import cv2
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
                golden = cv2.imread(ts.attrib.get('file_name'),0)
                roi_upper_left_x = str(ts.attrib.get('roi_upper_left')).split(';')[0]
                roi_upper_left_y = str(ts.attrib.get('roi_upper_left')).split(';')[1]
                roi_lower_right_x = str(ts.attrib.get('roi_lower_right')).split(';')[0]
                roi_lower_right_y = str(ts.attrib.get('roi_lower_right')).split(';')[1]
                roi_right_lower = 'teste'
                frame = cv2.VideoCapture(cam_port)
                result, image = frame.read()
                if result:
                    #primeiro procurar pela gondem na imagem inteira permitindo somente um resultado positivo e depois verificar se essa uma ocorrência está dentro do roi
                    #exemplo (substituir pelos rois)
                    cropped_image = result[80:280, 150:330]

                pass
            elif str(ts.attrib.get('name')) == str(TiposTeste.OCR.value):
                pass
