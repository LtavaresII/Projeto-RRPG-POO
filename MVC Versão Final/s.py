# -*- coding: utf-8 -*-


import time
import sys
from tinydb import TinyDB, Query
import tkinter as tk
from tkinter import *
from RRPGModel import ErroSenhaUsuarioIncorreto, ErroAtualizarFicha, ErroUsuarioIncorreto, ErroComandoInvalido, ErroOpcaoNaoValida, ErroCriacaoUsuario, ErroCriarFicha, ErroCriacaodeSala, Usuario, Ficha, Sala, RolagemdeDados, MyEncoder
from RRPGView import LoginGUI, TelaSalaGUI, SalaGUI, FichaGUI
import socket
import json
import pickle
from threading import Thread

HOST = '127.0.0.1'  # Endereco IP
PORT = 12011        # Porta

class ServerWork(Thread):

	def __init__(self,conn):
		Thread.__init__(self)
		self._conn = conn
		
	def mandar_mensagem(self,conn):
		msg = 'gerar'
		conn.send(msg.encode())

	def run(self):
		with self._conn as conn:
			
			dados = conn.recv(2048)
			opc = dados.decode()
			
				#Tela Inicial.....................................................................
			
			if opc == "cadastrar":
				usuario = conn.recv(2048)
				
				U = json.loads(usuario.decode(),object_hook = MyEncoder.decode)
				resposta = Usuario.Cadastrar(U)
					
				if resposta == True:
					conn.send(b'True')
				else:
					conn.send(b'False')
					raise ErroCriacaoUsuario()
						
			elif opc == "logar":
				usuario = conn.recv(2048)
				
				L = json.loads(usuario.decode(),object_hook = MyEncoder.decode)
				email = L._Email
				senha = L._Senha
				
				resposta = Usuario.Logar(email, senha)
				if resposta is True:
					conn.send(b'True')
				else:
					conn.send(b'False')
					raise ErroCriacaoUsuario()
			
				#Tela das Salas...................................................................
			
			elif opc == "criar sala":
				telasala = conn.recv(2048)
				
				S = json.loads(telasala.decode(),object_hook = MyEncoder.decode)
				
				resposta = Sala.Criar(S)
				if resposta is True:
					conn.send(b'True')
				else:
					conn.send(b'False')
					raise ErroCriacaodeSala()
					
			elif opc == "abrir sala":
				telasala = conn.recv(2048)
				nome = self._conn.recv(2048)
				print(nome)
				
				L = Sala.Abrir(nome)
				
				conn.send(str.encode(json.dumps(L, cls=produto.MyEncoder)))
				
				#self._conn.sendall(L)
				
				#Sala........................................................................
				
			elif opc =="adicionar usuario":
				sala = conn.recv(2048)
				
				AS = json.loads(sala.decode(),object_hook = MyEncoder.decode)
				sala = AS._Sala
				usuario = AS._Usuario
				resposta = Sala.Atualizar_Usuario(sala,usuario)
				if resposta is True:
					conn.send(b'True')
				else:
					conn.send(b'False')
					raise ErroUsuarioIncorreto()
				
				#Chat.............................................................................
						
			elif opc == "enviar":
				sala = conn.recv(2048)
				sala.decode()	
				conn.send("ola".encode())
				msg = conn.recv(2048)
				with open(sala,"a") as arq:
					arq.write(msg.decode())
					arq.write('\n')
			
				print(msg.decode())
				
				#Fichas...........................................................................
				
			elif opc == "salvar ficha":
				ficha = conn.recv(2048)
				
				F = json.loads(ficha.decode(),object_hook = MyEncoder.decode)
				
				resposta = Ficha.Criar(F)
				if resposta is True:
					conn.send(b'True')
				else:
					conn.send(b'False')
					raise ErroCriarFicha()
					
			elif opc == "atualizar ficha":
				ficha = conn.recv(2048)
				
				AF = json.loads(ficha.decode(),object_hook = MyEncoder.decode)
				nome = AF._Nome
				raca = AF._Raca
				classe = AF._Classe
				nivel = AF._Nivel
				vida = AF._Vida
				ca = AF._CA
				deslc = AF._Deslocamento
				antec = AF._Antecedente
				forc = AF._Forca
				dex = AF._Destreza
				cons = AF._Constituicao
				intl = AF._Inteligencia
				sab = AF._Sabedoria
				car = AF._Carisma
				equip = AF._Equipamento
				info = AF._InformacaoPersonagem
				ataq = AF._Ataques
				peri = AF._Pericias
				test = AF._Testes
				
				resposta = Ficha.Atualizar(nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car, equip, info, ataq, peri, test)
				if resposta is True:
					conn.send(b'True')
				else:
					conn.send(b'False')
					raise ErroAtualizarFicha()
				
class Server:
	def __init__(self, host, port):
		self._host = host
		self._port = port
		
	def iniciar(self):
		try:
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
				s.bind((self._host, self._port))
				s.listen()
				while True:
					conn, addr = s.accept()
					T = ServerWork(conn)
					T.start()
					
		except Exception as err:
			print('Erro na conexao...{0}'.format(err))
			
if __name__ == "__main__":
    S = Server(HOST,PORT)
    S.iniciar()
