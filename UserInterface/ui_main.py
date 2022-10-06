# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_sistema.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QInputDialog, QFileDialog
from Model import testcase
import xml.etree.cElementTree as ET
from enum import Enum

from xml.dom import minidom

class TiposTeste(Enum):
    TIMER = 'TIMER'
    SERIAL = 'SERIAL'
    DOUT = 'DOUT'
    DIN = 'DIN'



class Ui_MainWindow(object):

    def prettify(elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = ElementTree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

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
        #self.pushAdicionarStep = QtWidgets.QPushButton(self.verticalFrame)
        #self.pushAdicionarStep.setMinimumSize(QtCore.QSize(0, 40))
        #self.pushAdicionarStep.setObjectName("pushAdicionarStep")
        #self.verticalLayout_3.addWidget(self.pushAdicionarStep)
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
        #self.pushAnalogOut = QtWidgets.QPushButton(self.verticalFrame)
        #self.pushAnalogOut.setMinimumSize(QtCore.QSize(0, 40))
        #self.pushAnalogOut.setObjectName("pushAnalogOut")
        #self.verticalLayout_3.addWidget(self.pushAnalogOut)

        self.pushDigitalInput = QtWidgets.QPushButton(self.verticalFrame)
        self.pushDigitalInput.setMinimumSize(QtCore.QSize(0, 40))
        self.pushDigitalInput.setObjectName("pushDigitalInput")
        self.verticalLayout_3.addWidget(self.pushDigitalInput)
        self.line = QtWidgets.QFrame(self.verticalFrame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        #self.pushAnalogInput = QtWidgets.QPushButton(self.verticalFrame)
        #self.pushAnalogInput.setMinimumSize(QtCore.QSize(0, 40))
        #self.pushAnalogInput.setObjectName("pushAnalogInput")
        #self.verticalLayout_3.addWidget(self.pushAnalogInput)
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
        self.pushRemoverTestcase = QtWidgets.QPushButton(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushRemoverTestcase.setFont(font)
        self.pushRemoverTestcase.setObjectName("pushRemoverTestcase")
        self.horizontalLayout_3.addWidget(self.pushRemoverTestcase)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushSalvar = QtWidgets.QPushButton(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushSalvar.setFont(font)
        self.pushSalvar.setObjectName("pushSalvar")
        self.verticalLayout.addWidget(self.pushSalvar)
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
        #self.pushAdicionarStep.clicked.connect(self.adicionar_step)
        self.pushSalvar.clicked.connect(self.salvar)
        self.pushRemoverTestcase.clicked.connect(self.remover_testcase)
        self.listaTestcases.clicked.connect(self.get_testcase_name)
        self.pushSerial.clicked.connect(self.enviar_serial)
        self.pushRemoveStep.clicked.connect(self.remover_teststep)
        self.pushTimer.clicked.connect(self.timer)
        self.pushDigitalOut.clicked.connect(self.saida_digital)
        self.pushDigitalInput.clicked.connect(self.entrada_digital)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushNovo.setText(_translate("MainWindow", "Novo"))
        self.pushAbrir.setText(_translate("MainWindow", "Abrir"))
        #self.pushAdicionarStep.setText(_translate("MainWindow", "Adicionar Step"))
        self.pushRemoveStep.setText(_translate("MainWindow", "Remover Step"))
        self.pushTimer.setText(_translate("MainWindow", "Timer"))
        self.pushSerial.setText(_translate("MainWindow", "Serial"))
        self.pushDigitalOut.setText(_translate("MainWindow", "Saída Digital"))
        #self.pushAnalogOut.setText(_translate("MainWindow", "Saída Analógica"))
        self.pushDigitalInput.setText(_translate("MainWindow", "Entrada Digital"))
        #self.pushAnalogInput.setText(_translate("MainWindow", "Entrada Analógica"))
        self.pushPattern.setText(_translate("MainWindow", "Padrão"))
        self.pushOcr.setText(_translate("MainWindow", "O.C.R."))
        self.pushAdicionar.setText(_translate("MainWindow", "Adicionar Testcase"))
        self.pushRemoverTestcase.setText(_translate("MainWindow", "RemoverTestcase"))
        self.pushSalvar.setText(_translate("MainWindow", "Salvar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.pushAbrir_2.setText(_translate("MainWindow", "Abrir"))
        self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "Testcase"))
        self.treeWidget_2.headerItem().setText(1, _translate("MainWindow", "Função"))
        self.treeWidget_2.headerItem().setText(2, _translate("MainWindow", "Resultado"))
        self.pushIniciar_2.setText(_translate("MainWindow", "Iniciar"))
        self.pushParar_2.setText(_translate("MainWindow", "Parar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_executar), _translate("MainWindow", "Tab 2"))

    def atualizar_lista_testcases(self):
        self.listaTestcases.clear()
        self.contador_testcases = 1
        for tc in self.listaTC:
            self.listaTestcases.addItem(str(self.contador_testcases) + '. ' + tc.nome)
            self.contador_testcases += 1
    def atualizar_lista_teststeps(self):
        self.listaTeststeps.clear()
        for ts in self.listaTC[self.index_current_testcase].test_steps:
            self.listaTeststeps.addItem(str(ts.acao + ts.parametro))


    ##########Parei aqui, falta fazer os steps
    def carregar_test_steps(self):
        self.listaTeststeps.clear()
        for tc in self.listaTC:
            if tc.nome == self.current_testcase:
                for ts in tc.test_steps:
                    self.listaTeststeps.addItem(str(ts.acao + ts.parametro))
                self.tamanho_testcase = len(tc.test_steps)

    def enviar_serial(self):
        serialInformation, okPressed = QInputDialog.getText(None,'titulo','label')
        if okPressed and serialInformation != '':
            self.listaTC[self.index_current_testcase].adicionar_teststep('Enviar serial: ',serialInformation, TiposTeste.SERIAL)
        self.atualizar_lista_teststeps()
    def timer(self):
        timer_value, okPressed = QInputDialog.getText(None,'titulo','label')
        if okPressed and timer_value != '':
            self.listaTC[self.index_current_testcase].adicionar_teststep('Wait(ms): ',timer_value, TiposTeste.TIMER)
        self.atualizar_lista_teststeps()
    def saida_digital(self):
        porta, okPorta = QInputDialog.getText(None,'titulo','Digite a porta digital')
        status, okStatus = QInputDialog.getText(None, 'titulo', 'Digite o status desejado (0-1)')
        if okPorta and porta.isdigit() and okStatus and (status == '1' or status =='0') :
            self.listaTC[self.index_current_testcase].adicionar_teststep('Saída Digital: ',str(porta+':'+status), TiposTeste.DOUT)
        self.atualizar_lista_teststeps()
    def entrada_digital(self):
        porta, okPorta = QInputDialog.getText(None,'titulo','Digite a porta digital')
        status, okStatus = QInputDialog.getText(None, 'titulo', 'Digite o status desejado (0-1)')
        if okPorta and porta.isdigit() and okStatus and (status == '1' or status =='0') :
            self.listaTC[self.index_current_testcase].adicionar_teststep('Entrada digital: ',str(porta+':'+status),TiposTeste.DIN)
        self.atualizar_lista_teststeps()

    def get_testcase_name(self):
        current_testcase = self.listaTestcases.currentItem()
        self.index_current_testcase = self.listaTestcases.currentRow()
        if current_testcase is not None:
            self.current_testcase = current_testcase.text().split('. ')[1]
            self.carregar_test_steps()

    def criar_arquivo(self):
        self.listaTestcases.clear()
        self.listaTC = []

    def abrir_arquivo(self):
        self.listaTestcases.clear()
        fname = QFileDialog.getOpenFileName(None, 'Open file', '.\\', "XML files (*.xml)")
        tree = ET.parse(fname[0])
        root = tree.getroot()
        if root is not None:
            self.listaTC = []
            self.index_current_testcase = 0
            for tc in root:
                self.listaTC.append(testcase.Testcase(tc.attrib.get('name')))
                for ts in tc:
                    if str(ts.attrib.get('name')) == str(TiposTeste.DOUT.value):
                        self.listaTC[self.index_current_testcase].adicionar_teststep('Saída Digital: ', ts.get('porta') + ':' + ts.text, TiposTeste.DOUT.value)
                    elif str(ts.attrib.get('name')) == str(TiposTeste.DIN.value):
                        self.listaTC[self.index_current_testcase].adicionar_teststep('Entrada digital: ', ts.get('porta') + ':' + ts.text, TiposTeste.DIN.value)
                    elif str(ts.attrib.get('name')) == str(TiposTeste.SERIAL.value):
                        self.listaTC[self.index_current_testcase].adicionar_teststep('Enviar serial: ', ts.text, TiposTeste.SERIAL.value)
                    elif str(ts.attrib.get('name')) == str(TiposTeste.TIMER.value):
                        self.listaTC[self.index_current_testcase].adicionar_teststep('Wait(ms): ', ts.text, TiposTeste.TIMER.value)
                self.index_current_testcase += 1
            self.atualizar_lista_testcases()

    def adicionar_testcase(self):
        testcase_name, okPressed = QInputDialog.getText(None,'titulo','label')
        if okPressed and testcase_name != '':
            self.listaTC.append(testcase.Testcase(testcase_name))
            self.index_current_testcase = (self.listaTC.index(self.listaTC[-1]))
        self.atualizar_lista_testcases()

    def remover_testcase(self):
        self.listaTeststeps.clear()
        for tc in self.listaTC:
            if tc.nome == self.current_testcase:
                self.listaTC.pop(self.listaTC.index(tc))
                self.atualizar_lista_testcases()

    def remover_teststep(self):
        print("flango")
        self.listaTC[self.index_current_testcase].remover_teststep()
        self.atualizar_lista_teststeps()

    def salvar(self):
        root = ET.Element("teste")
        contador_cases = 1
        for testcase in self.listaTC:
            doc = ET.SubElement(root, "TC" + str(contador_cases), name=testcase.nome)
            contador_cases+=1
            contador_steps = 1
            for teststep in testcase.test_steps:
                if teststep.tipo  == TiposTeste.TIMER.value:
                    ET.SubElement(doc, "step_" + str(contador_steps), name="TIMER").text = str(teststep.parametro)
                elif teststep.tipo == TiposTeste.SERIAL.value:
                    ET.SubElement(doc, "step_" + str(contador_steps), name="SERIAL").text = str(teststep.parametro)
                elif teststep.tipo == TiposTeste.DOUT.value:
                    ET.SubElement(doc, "step_" + str(contador_steps), name="DOUT", porta = teststep.parametro.split(':')[0]).text = teststep.parametro.split(':')[1]
                elif teststep.tipo == TiposTeste.DIN.value:
                    ET.SubElement(doc, "step_" + str(contador_steps), name="DIN", porta = teststep.parametro.split(':')[0]).text = teststep.parametro.split(':')[1]
                tree = ET.ElementTree(root)
                contador_steps+=1
                print(teststep.acao)
                print(teststep.parametro)
        fname = QFileDialog.getSaveFileName(None, 'Save File')
        tree.write(fname[0])


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())
