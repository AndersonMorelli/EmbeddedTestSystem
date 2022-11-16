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
import RPi.GPIO as gpio
pin_saida = 16
pin_concedido = 20
pin_negado = 21



gpio.setmode(gpio.BCM)

gpio.setup(pin_concedido, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(pin_negado, gpio.IN, pull_up_down=gpio.PUD_DOWN)
'''
gpio.setup(16, gpio.OUT) # Usei 18 pois meu setmode é BCM, se estive usando BOARD seria 12
gpio.output(16, gpio.HIGH)
gpio.output(16, gpio.LOW)
'''



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        MainWindow.setMinimumSize(QtCore.QSize(480, 320))
        MainWindow.setMaximumSize(QtCore.QSize(480, 320))
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("background-image: url(:/CadeadoFechado/CadeadoFechado.png);")


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.label_principal = QtWidgets.QLabel(self.centralwidget)
        self.label_principal.setEnabled(True)
        self.label_principal.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.label_principal.setMinimumSize(QtCore.QSize(480, 320))
        self.label_principal.setMaximumSize(QtCore.QSize(480, 320))
        self.label_principal.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; color:#ffffff;\">CONTROLE</span></p><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; color:#ffffff;\">DE</span></p><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; color:#ffffff;\">ACESSO</span></p></body></html>")
        self.label_principal.setAlignment(QtCore.Qt.AlignCenter)
        self.label_principal.setObjectName("label_principal")
        self.label_principal.setHidden(False)
        self.acesso_negado = QtWidgets.QLabel(self.centralwidget)
        self.acesso_negado.setEnabled(True)
        self.acesso_negado.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.acesso_negado.setMinimumSize(QtCore.QSize(480, 320))
        self.acesso_negado.setMaximumSize(QtCore.QSize(480, 320))
        self.acesso_negado.setAutoFillBackground(False)
        self.acesso_negado.setStyleSheet("background-image : url(./Cadeado/CadeadoFechado2.png);")
        self.acesso_negado.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; color:#ff0000;\">ACESSO NEGADO</span></p></body></html>")
        self.acesso_negado.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.acesso_negado.setObjectName("acesso_negado")
        self.acesso_negado.setHidden(False)
        self.acesso_concedido = QtWidgets.QLabel(self.centralwidget)
        self.acesso_concedido.setEnabled(True)
        self.acesso_concedido.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.acesso_concedido.setMinimumSize(QtCore.QSize(480, 320))
        self.acesso_concedido.setMaximumSize(QtCore.QSize(480, 320))
        self.acesso_concedido.setAutoFillBackground(False)
        self.acesso_concedido.setStyleSheet("background-image : url(./Cadeado/cadeado_fechado.jpg);")
        self.acesso_concedido.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; color:#55ff00;\">ACESSO CONCEDIDO</span></p></body></html>")
        self.acesso_concedido.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.acesso_concedido.setObjectName("acesso_concedido")
        self.acesso_concedido.setHidden(False)
        self.acesso_concedido.raise_()
        self.acesso_negado.raise_()
        self.label_principal.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.varrerGPIO)
        self.timer.start()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


    def varrerGPIO(self):
        if keyboard.is_pressed("a") or gpio.input(pin_negado) == 1:
            self.acesso_negado.raise_()
        elif keyboard.is_pressed("b") or gpio.input(pin_concedido) == 1:
            self.acesso_concedido.raise_()
        else:
            self.label_principal.raise_()

        gpio.cleanup()
        exit()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.showFullScreen()
#MainWindow.show()
sys.exit(app.exec())
