from Controller import Controller
import socket

HOST = '127.0.0.1'  # Endereco IP do servidor
PORT = 12011        # Porta utilizada no servidor

if __name__ == "__main__":
	C = Controller(0,HOST,PORT)
