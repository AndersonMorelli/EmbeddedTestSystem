import xml.etree.cElementTree as ET
from enum import Enum
import time
import pyfirmata
from ImageProcessing import capturar_frame
from ImageProcessing import tesseract_temp
from ImageProcessing import pattern

try:
    placa = pyfirmata.Arduino("COM5")
except:
    print('Arduino não conectado.')
    arduino_conectado = False
else:
    arduino_conectado = True
fpath = '../aTeste/'
templates_path = fpath+'templates/'
report_path = fpath+'report/'

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
        contador_tc += 1
        print("Testcase " + str(contador_tc) + ': ' + tc.attrib.get('name'))
        contador_ts = 0
        for ts in tc:
            contador_ts += 1
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
                roi = [int(ts.attrib.get('left')), int(ts.attrib.get('top')), int(ts.attrib.get('right')), int(ts.attrib.get('botton'))]
                imagem = capturar_frame.capturar()
                template = capturar_frame.carregar(str(templates_path + ts.attrib.get('template')))
                resultado = pattern.testar(roi, template, imagem, report_path+'TC'+str(contador_tc)+'STEP'+str(contador_ts))
                if resultado == False:
                    resultado_teste = 'FAIL ||| '
                    complemento = ' Template não encontrado verificar imagem: ' + 'TC'+str(contador_tc)+'STEP'+str(contador_ts)+'.jpg'

            elif str(ts.attrib.get('name')) == str(TiposTeste.OCR.value):
                roi = [int(ts.attrib.get('left')), int(ts.attrib.get('top')), int(ts.attrib.get('right')), int(ts.attrib.get('botton'))]
                imagem = capturar_frame.capturar()
                resultado = tesseract_temp.testar(roi, str(ts.attrib.get('texto')), imagem,report_path+'TC'+str(contador_tc)+'STEP'+str(contador_ts))
                if resultado == False:
                    resultado_teste = 'FAIL ||| '
                    complemento = ' Texto não encontrado verificar imagem: ' + 'TC'+str(contador_tc)+'STEP'+str(contador_ts)+'.jpg'

            #Exibe o resultado do teststep
            print(resultado_teste + "Step " + str(contador_ts) + ': ' + ts.attrib.get('name') + complemento)

