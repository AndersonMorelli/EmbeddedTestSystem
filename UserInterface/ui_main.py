# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_sistema.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 680)
        MainWindow.setMinimumSize(QtCore.QSize(770, 680))
        MainWindow.setMaximumSize(QtCore.QSize(770, 680))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 770, 680))
        self.tabWidget.setMinimumSize(QtCore.QSize(770, 680))
        self.tabWidget.setMaximumSize(QtCore.QSize(770, 680))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalFrame = QtWidgets.QFrame(self.tab)
        self.verticalFrame.setGeometry(QtCore.QRect(0, 10, 760, 645))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame = QtWidgets.QFrame(self.verticalFrame)
        self.horizontalFrame.setEnabled(True)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(0, 40))
        self.horizontalFrame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushNovo = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushNovo.setMinimumSize(QtCore.QSize(100, 0))
        self.pushNovo.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushNovo.setObjectName("pushNovo")
        self.horizontalLayout_2.addWidget(self.pushNovo)
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalFrame)
        self.textBrowser.setMinimumSize(QtCore.QSize(515, 0))
        self.textBrowser.setMaximumSize(QtCore.QSize(515, 16777215))
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_2.addWidget(self.textBrowser)
        self.pushAbrir = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushAbrir.setMinimumSize(QtCore.QSize(100, 0))
        self.pushAbrir.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushAbrir.setObjectName("pushAbrir")
        self.horizontalLayout_2.addWidget(self.pushAbrir)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushAdicionarStep = QtWidgets.QPushButton(self.verticalFrame)
        self.pushAdicionarStep.setMinimumSize(QtCore.QSize(0, 40))
        self.pushAdicionarStep.setObjectName("pushAdicionarStep")
        self.verticalLayout_3.addWidget(self.pushAdicionarStep)
        self.pushRemoveStep = QtWidgets.QPushButton(self.verticalFrame)
        self.pushRemoveStep.setMinimumSize(QtCore.QSize(0, 40))
        self.pushRemoveStep.setObjectName("pushRemoveStep")
        self.verticalLayout_3.addWidget(self.pushRemoveStep)
        self.pushTimer = QtWidgets.QPushButton(self.verticalFrame)
        self.pushTimer.setMinimumSize(QtCore.QSize(0, 40))
        self.pushTimer.setObjectName("pushTimer")
        self.verticalLayout_3.addWidget(self.pushTimer)
        self.line_2 = QtWidgets.QFrame(self.verticalFrame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.pushSerial = QtWidgets.QPushButton(self.verticalFrame)
        self.pushSerial.setMinimumSize(QtCore.QSize(0, 40))
        self.pushSerial.setObjectName("pushSerial")
        self.verticalLayout_3.addWidget(self.pushSerial)
        self.pushDigitalOut = QtWidgets.QPushButton(self.verticalFrame)
        self.pushDigitalOut.setMinimumSize(QtCore.QSize(0, 40))
        self.pushDigitalOut.setObjectName("pushDigitalOut")
        self.verticalLayout_3.addWidget(self.pushDigitalOut)
        self.pushAnalogOut = QtWidgets.QPushButton(self.verticalFrame)
        self.pushAnalogOut.setMinimumSize(QtCore.QSize(0, 40))
        self.pushAnalogOut.setObjectName("pushAnalogOut")
        self.verticalLayout_3.addWidget(self.pushAnalogOut)
        self.line = QtWidgets.QFrame(self.verticalFrame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.pushDigitalInput = QtWidgets.QPushButton(self.verticalFrame)
        self.pushDigitalInput.setMinimumSize(QtCore.QSize(0, 40))
        self.pushDigitalInput.setObjectName("pushDigitalInput")
        self.verticalLayout_3.addWidget(self.pushDigitalInput)
        self.pushAnalogInput = QtWidgets.QPushButton(self.verticalFrame)
        self.pushAnalogInput.setMinimumSize(QtCore.QSize(0, 40))
        self.pushAnalogInput.setObjectName("pushAnalogInput")
        self.verticalLayout_3.addWidget(self.pushAnalogInput)
        self.pushPattern = QtWidgets.QPushButton(self.verticalFrame)
        self.pushPattern.setMinimumSize(QtCore.QSize(0, 40))
        self.pushPattern.setObjectName("pushPattern")
        self.verticalLayout_3.addWidget(self.pushPattern)
        self.pushOcr = QtWidgets.QPushButton(self.verticalFrame)
        self.pushOcr.setMinimumSize(QtCore.QSize(0, 40))
        self.pushOcr.setObjectName("pushOcr")
        self.verticalLayout_3.addWidget(self.pushOcr)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.listaTestcases = QtWidgets.QListWidget(self.verticalFrame)
        self.listaTestcases.setMinimumSize(QtCore.QSize(100, 0))
        self.listaTestcases.setMaximumSize(QtCore.QSize(100, 16777215))
        self.listaTestcases.setObjectName("listaTestcases")
        self.horizontalLayout_4.addWidget(self.listaTestcases)
        self.listaTeststeps = QtWidgets.QListWidget(self.verticalFrame)
        self.listaTeststeps.setObjectName("listaTeststeps")
        self.horizontalLayout_4.addWidget(self.listaTeststeps)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushAdicionar = QtWidgets.QPushButton(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushAdicionar.setFont(font)
        self.pushAdicionar.setObjectName("pushAdicionar")
        self.horizontalLayout_3.addWidget(self.pushAdicionar)
        self.pushRemover = QtWidgets.QPushButton(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushRemover.setFont(font)
        self.pushRemover.setObjectName("pushRemover")
        self.horizontalLayout_3.addWidget(self.pushRemover)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushAdicionar_2 = QtWidgets.QPushButton(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushAdicionar_2.setFont(font)
        self.pushAdicionar_2.setObjectName("pushAdicionar_2")
        self.verticalLayout.addWidget(self.pushAdicionar_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_executar = QtWidgets.QWidget()
        self.tab_executar.setObjectName("tab_executar")
        self.verticalFrame_2 = QtWidgets.QFrame(self.tab_executar)
        self.verticalFrame_2.setGeometry(QtCore.QRect(0, 10, 760, 517))
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalFrame_2 = QtWidgets.QFrame(self.verticalFrame_2)
        self.horizontalFrame_2.setEnabled(True)
        self.horizontalFrame_2.setMinimumSize(QtCore.QSize(0, 40))
        self.horizontalFrame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.horizontalFrame_2)
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_5.addWidget(self.textBrowser_2)
        self.pushAbrir_2 = QtWidgets.QPushButton(self.horizontalFrame_2)
        self.pushAbrir_2.setObjectName("pushAbrir_2")
        self.horizontalLayout_5.addWidget(self.pushAbrir_2)
        self.verticalLayout_2.addWidget(self.horizontalFrame_2)
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.verticalFrame_2)
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.verticalLayout_2.addWidget(self.treeWidget_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushIniciar_2 = QtWidgets.QPushButton(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushIniciar_2.setFont(font)
        self.pushIniciar_2.setObjectName("pushIniciar_2")
        self.horizontalLayout_6.addWidget(self.pushIniciar_2)
        self.pushParar_2 = QtWidgets.QPushButton(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushParar_2.setFont(font)
        self.pushParar_2.setObjectName("pushParar_2")
        self.horizontalLayout_6.addWidget(self.pushParar_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_executar, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.contador_testcases = 0
        self.pushNovo.clicked.connect(self.criar_arquivo)
        self.pushAbrir.clicked.connect(self.abrir_arquivo)
        self.pushAdicionar.clicked.connect(self.adicionar_testcase)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushNovo.setText(_translate("MainWindow", "Novo"))
        self.pushAbrir.setText(_translate("MainWindow", "Abrir"))
        self.pushAdicionarStep.setText(_translate("MainWindow", "Adicionar Step"))
        self.pushRemoveStep.setText(_translate("MainWindow", "Remover Step"))
        self.pushTimer.setText(_translate("MainWindow", "Timer"))
        self.pushSerial.setText(_translate("MainWindow", "Serial"))
        self.pushDigitalOut.setText(_translate("MainWindow", "Saída Digital"))
        self.pushAnalogOut.setText(_translate("MainWindow", "Saída Analógica"))
        self.pushDigitalInput.setText(_translate("MainWindow", "Entrada Digital"))
        self.pushAnalogInput.setText(_translate("MainWindow", "Entrada Analógica"))
        self.pushPattern.setText(_translate("MainWindow", "Padrão"))
        self.pushOcr.setText(_translate("MainWindow", "O.C.R."))
        self.pushAdicionar.setText(_translate("MainWindow", "Adicionar Testcase"))
        self.pushRemover.setText(_translate("MainWindow", "RemoverTestcase"))
        self.pushAdicionar_2.setText(_translate("MainWindow", "Salvar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.pushAbrir_2.setText(_translate("MainWindow", "Abrir"))
        self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "Testcase"))
        self.treeWidget_2.headerItem().setText(1, _translate("MainWindow", "Função"))
        self.treeWidget_2.headerItem().setText(2, _translate("MainWindow", "Resultado"))
        self.pushIniciar_2.setText(_translate("MainWindow", "Iniciar"))
        self.pushParar_2.setText(_translate("MainWindow", "Parar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_executar), _translate("MainWindow", "Tab 2"))



    def criar_arquivo(self):
        self.listaTestcases.clear()
        self.contador_testcases = 0


    def abrir_arquivo(self):
        self.listaTestcases.clear()
        arquivo_testcase = ['S','a',',','k']
        self.contador_testcases = len(arquivo_testcase)
        contador_testcase_atual = 1
        for testcase in arquivo_testcase:
            self.listaTestcases.addItem(str(contador_testcase_atual) + '. ' + testcase)
            contador_testcase_atual += 1


    def adicionar_testcase(self):
        text, okPressed = QInputDialog.getText(None,'titulo','label')
        if okPressed and text != '':
            self.contador_testcases += 1
            self.listaTestcases.addItem(str(self.contador_testcases) + '. ' + text)



    def remover_testcase(self):
        pass


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())
