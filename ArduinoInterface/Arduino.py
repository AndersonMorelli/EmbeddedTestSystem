import pyfirmata

sinal_entrada = 1
acesso_negado = 2
acesso_concedido = 3

porta_arduino = 'COM3' #Configuramos a porta como a porta COM4. Esta configuração deve ser alterada caso sua placa não se configure nesta porta.
placa = pyfirmata.Arduino(porta_arduino) #Criamos a variável board que realizará os comandos a partir daqui

placa.digital[sinal_entrada].mode = pyfirmata.INPUT
placa.digital[acesso_negado].mode = pyfirmata.OUTPUT
placa.digital[acesso_concedido].mode = pyfirmata.OUTPUT
it = pyfirmata.util.Iterator(placa)
it.start()
placa.digital[3].read()

while True:
    if placa.digital[0].read() == None:
        pass
    else:
        print("board.analog[0].read()")
        placa.digital[13].write(1)#Utilizamos a variável board e seu método .Digital para dizer ao pino 13 que ele deve acender
        placa.digital[13].write(0)#Utilizamos a variável board e seu método .Digital para dizer ao pino 13 que ele deve apagar