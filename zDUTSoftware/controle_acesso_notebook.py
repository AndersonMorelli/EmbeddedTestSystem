# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UiFiles\ControleAcesso.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
import sys

import keyboard
import pyfirmata

in_concedido = 0
in_negado = 5
out_rele = 13

try:
    arduino = pyfirmata.Arduino("COM5")
except:
    print('Arduino não conectado.')
    arduino_conectado = False
else:
    arduino_conectado = True

if arduino_conectado:
    arduino.digital[out_rele].mode = pyfirmata.OUTPUT

    it = pyfirmata.util.Iterator(arduino)
    it.start()
    arduino.analog[in_concedido].enable_reporting()
    arduino.analog[in_negado].enable_reporting()
    rele = arduino.get_pin('d:13:o')



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #resolution = [480, 320]
        resolution = [1600, 900]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(resolution[0], resolution[1])
        MainWindow.setMinimumSize(QtCore.QSize(resolution[0], resolution[1]))
        MainWindow.setMaximumSize(QtCore.QSize(resolution[0], resolution[1]))
        MainWindow.setAutoFillBackground(True)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.label_principal = QtWidgets.QLabel(self.centralwidget)
        self.label_principal.setEnabled(True)
        self.label_principal.setGeometry(QtCore.QRect(0, 0, resolution[0], resolution[1]))
        self.label_principal.setMinimumSize(QtCore.QSize(resolution[0], resolution[1]))
        self.label_principal.setMaximumSize(QtCore.QSize(resolution[0], resolution[1]))
        self.label_principal.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:120pt; font-weight:700; color:#ffffff;\">CONTROLE</span></p><p align=\"center\"><span style=\" font-size:120pt; font-weight:700; color:#ffffff;\">DE</span></p><p align=\"center\"><span style=\" font-size:120pt; font-weight:700; color:#ffffff;\">ACESSO</span></p></body></html>")
        self.label_principal.setAlignment(QtCore.Qt.AlignCenter)
        self.label_principal.setObjectName("label_principal")
        self.label_principal.setHidden(False)
        self.acesso_negado = QtWidgets.QLabel(self.centralwidget)
        self.acesso_negado.setEnabled(True)
        self.acesso_negado.setGeometry(QtCore.QRect(0, 0, resolution[0], resolution[1]))
        self.acesso_negado.setMinimumSize(QtCore.QSize(resolution[0], resolution[1]))
        self.acesso_negado.setMaximumSize(QtCore.QSize(resolution[0], resolution[1]))
        self.acesso_negado.setAutoFillBackground(False)
        self.acesso_negado.setStyleSheet("background-image : url(./Cadeado/fechado_note.png);")
        self.acesso_negado.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:90pt; font-weight:700; color:#ff0000;\">ACESSO NEGADO</span></p></body></html>")
        self.acesso_negado.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.acesso_negado.setObjectName("acesso_negado")
        self.acesso_negado.setHidden(False)
        self.acesso_concedido = QtWidgets.QLabel(self.centralwidget)
        self.acesso_concedido.setEnabled(True)
        self.acesso_concedido.setGeometry(QtCore.QRect(0, 0, resolution[0], resolution[1]))
        self.acesso_concedido.setMinimumSize(QtCore.QSize(resolution[0], resolution[1]))
        self.acesso_concedido.setMaximumSize(QtCore.QSize(resolution[0], resolution[1]))
        self.acesso_concedido.setAutoFillBackground(False)
        self.acesso_concedido.setStyleSheet("background-image : url(./Cadeado/aberto_note.png);")
        self.acesso_concedido.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:90pt; font-weight:700; color:#55ff00;\">ACESSO CONCEDIDO</span></p></body></html>")
        self.acesso_concedido.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.acesso_concedido.setObjectName("acesso_concedido")
        self.acesso_concedido.setHidden(False)
        self.acesso_concedido.raise_()
        self.acesso_negado.raise_()
        self.label_principal.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.timer = QtCore.QTimer()
        self.fps = 50
        self.timer.setInterval(1000/self.fps)
        self.timer.timeout.connect(self.varrerGPIO)
        self.timer.start()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


    def varrerGPIO(self):
        if arduino_conectado:
            concedido = arduino.analog[in_concedido].read()
            negado = arduino.analog[in_negado].read()
            if keyboard.is_pressed("a") or negado == 0:
                self.acesso_negado.raise_()
                rele.write(0)
            elif keyboard.is_pressed("b") or concedido == 0:
                self.acesso_concedido.raise_()
                rele.write(1)
            else:
                self.label_principal.raise_()
                rele.write(0)

        else:
            if keyboard.is_pressed("a"):
                self.acesso_negado.raise_()
            elif keyboard.is_pressed("b"):
                self.acesso_concedido.raise_()
            else:
                self.label_principal.raise_()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.showFullScreen()
#MainWindow.show()
sys.exit(app.exec())
