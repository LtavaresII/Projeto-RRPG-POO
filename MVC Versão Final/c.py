# -*- coding: utf-8 -*-

import time
import sys
from tinydb import TinyDB, Query
import tkinter as tk
from tkinter import *
import socket
import json
import threading
from threading import Thread
import pickle
import select
from RRPGModel import ErroSenhaUsuarioIncorreto, ErroAtualizarFicha, ErroComandoInvalido, ErroUsuarioIncorreto, ErroOpcaoNaoValida, ErroCriacaoUsuario, ErroCriarFicha, ErroCriacaodeSala, Usuario, Ficha, Sala, RolagemdeDados, Login, MyEncoder
from RRPGView import LoginGUI, TelaSalaGUI, SalaGUI, FichaGUI

HOST = '127.0.0.1'  # Endereco IP
PORT = 12011        # Porta

class Cliente:
	
	_data = {"Sala":"", "Usuario":"", "UsuarioC":""}
	
	def __init__(self, host, port, n, conn):
		self.root = tk.Tk()
		self.root.geometry('900x520+100+100')
		self.root.configure(bg = '#ffffff')
		
		self._conn = conn
		self._host = host
		self._port = port
		
		Thread.__init__(self)
		
		if n == 0:
			view = LoginGUI(self.root, self)
			tela = 'Tela Inicial'
		elif n == 1:
			view = TelaSalaGUI(self.root, self)
			tela = 'Tela das Salas'
		elif n == 2:
			view = SalaGUI(self.root, self)
			self.Atualizar()
			tela = Controller._data["Sala"]
		elif n == 3:
			view = FichaGUI(self.root, self)
			tela = 'Fichas'
			
		self.root.title(tela)
		
		self.view = view
		
		self.root.mainloop()
		
	#Tela Inicial......................................................................
	
	def cadastrar(self):
		self.view.cadastro()
		
	def cadastrar_usuario(self, pnome, snome, email, senha, senhac):
		self._conn.send(b'cadastrar')
		try:
		
			U = Usuario(pnome, snome, email, senha, senhac)
		
			self._conn.send(str.encode(json.dumps(U, cls= MyEncoder)))
		
			resposta = self._conn.recv(2048)
			r = resposta.decode()
			if r == 'True':
				self.view.cadastrar_ok()
			else:
				self.view.cadastrar_erro()
		except ErroCriacaoUsuario:
			self.view.cadastrar_erro()
		
	def logar_usuario(self, Email ,Senha):
		self._conn.send(b'logar')
		try:
			L = Login(Email ,Senha)
		
			self._conn.send(str.encode(json.dumps(L, cls= MyEncoder)))
		
			resposta = self._conn.recv(2048)
			r = resposta.decode()
			if r == 'True':
				Cliente._data["Usuario"] = Email
				self.view.logar_ok()
				self.root.destroy()
				Cliente(HOST,PORT,1,s)
			else:
				self.view.logar_erro()
		except ErroSenhaUsuarioIncorreto:
			self.view.logar_erro()
			
	#Tela das Salas..............................................................
	
	#def Criar(self):
		#self.view.Sala()
		
	def criar_sala(self, nome):
		self._conn.send(b'criar sala')
		try:
			usuario = Cliente._data["Usuario"]
			if nome !="" and usuario != "":
				S = Sala(nome, usuario)
				
				self._conn.send(str.encode(json.dumps(S, cls= MyEncoder)))
				
				resposta = self._conn.recv(2048)
				r = resposta.decode()
				if r == 'True':
					self.view.criar_sala_ok()
				else:
					self.view.criar_sala_erro()
			else:
				self.view.criar_sala_erro()
		except ErroCriacaodeSala:
			self.view.criar_sala_erro()
	
	def listar_salas(self):
		self.view.listar(Sala.listar())
		
	def abrir_sala(self, nome):
		self._conn.send(b'abrir sala')
		try:
			if nome !="":
				
				self._conn.sendall(nome)
				
				L = self._conn.recv(2048)
				usuario = Cliente._data["Usuario"]
				for s in L:
					sala = s._Nome
					u = s._Usuario
					for x in u:
						for q in x:
							Cliente._data["UsuarioC"] = q
							uc = Cliente._data["UsuarioC"]
							if uc == usuario:
								try:
									Cliente._data["Sala"] = sala
									self.root.destroy()
									with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
										s.connect((HOST, PORT))
										print("Conectado!")
										C = Cliente(HOST,PORT,2,s)
										C.iniciar()
			
								except Exception as E:
									print('Erro na conexao...{0}'.format(E))
									raise E
							else:
								self.view.abrir_sala_erro()
			else:
				self.view.abrir_sala_erro()
		except ErroOpcaoNaoValida:
			self.view.abrir_sala_erro()
			
	def logout(self):
		try:
			self.root.destroy()
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
				s.connect((HOST, PORT))
				print("Conectado!")
				C = Cliente(HOST,PORT,0,s)
				C.iniciar()
			
		except Exception as E:
			print('Erro na conexao...{0}'.format(E))
			raise E
			
	#Sala........................................................................

	def abrir_ficha(self):
		try:
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
				s.connect((HOST, PORT))
				print("Conectado!")
				C = Cliente(HOST,PORT,3,s)
				C.iniciar()
			
		except Exception as E:
			print('Erro na conexao...{0}'.format(E))
			raise E
		
	def adicionar_usuario(self,usuario):
		self._conn.send(b'adicionar usuario')
		try:
			sala = Cliente._data["Sala"]
			AS = AtualizarSala(sala,usuario)
			
			self._conn.send(str.encode(json.dumps(A, cls= MyEncoder)))
			
			resposta = self._conn.recv(2048)
			r = resposta.decode()
			if r == 'True':
				self.view.adicionar_usuario_ok()
			else:
				self.view.adicionar_usuario_erro()
		except ErroComandoInvalido:
			self.view.adicionar_usuario_erro()
			
	def sair_sala(self):
		try:
			self.root.destroy()
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
				s.connect((HOST, PORT))
				print("Conectado!")
				C = Cliente(HOST,PORT,1,s)
				C.iniciar()
			
		except Exception as E:
			print('Erro na conexao...{0}'.format(E))
			raise E
			
	#Chat.........................................................................
	
	def receber(self,msg):
		self._conn.send(b'enviar')
		try:        
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
				s.connect((HOST, PORT))
				usuario = Controller._data["Usuario"]
				msg = str(usuario)+ ": " +msg
				#botar nome do usuario
				s.send(msg.encode())
			self.view.limparM()
			
		except Exception as E:
			print("algo esta errado".format(E))
			raise E

	def limpar_chat(self):
		with open('lista.txt','w') as arq:
			arq.write("chat limpo...")
			arq.write('\n')
			
	def Atualizar(self):
		self.start()
		
	def run(self):
		try:
			while True:
				with open('lista.txt','r') as arq:
					time.sleep(1)
					l = arq.read()
					self.view.Conversa(l)
		except Exception as E:
			print('chat nao existe...'.format(E))
			raise E
			
	#Fichas........................................................................
	
	def salvar_ficha(self, nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car, equip, info, ataq, peri, test):
		self._conn.send(b'salvar ficha')
		try:
			sala = Controller._data["Sala"]
			usuario = Controller._data["Usuario"]
			
			F = Ficha(nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car, equip, info, ataq, peri, test, usuario, sala)
			
			self._conn.send(str.encode(json.dumps(F, cls= MyEncoder)))
			
			resposta = self._conn.recv(2048)
			r = resposta.decode()
			if r == 'True':
				self.view.salvar_ficha_ok()
			else:
				self.view.salvar_ficha_erro()
		except ErroCriarFicha:
			self.view.salvar_ficha_erro()
			
	def atualizar_ficha(self, nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car, equip, info, ataq, peri, test):
		self._conn.send(b'atualizar ficha')
		try:
			AF = AtualizarFicha(nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car, equip, info, ataq, peri, test)
			
			self._conn.send(str.encode(json.dumps(AF, cls= MyEncoder)))
			
			resposta = self._conn.recv(2048)
			r = resposta.decode()
			if r == 'True':
				self.view.salvar_ficha_ok()
			else:
				self.view.atualizar_ficha_ok()
		except ErroAtualizarFicha:
			self.view.atualizar_ficha_erro()
			
	def listar_fichas(self):
		self.view.listar(Ficha.listar())
		
	def fechar(self):
		self.root.destroy()

if __name__ == '__main__':
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.connect((HOST, PORT))
			print("Conectado!")
			C = Cliente(HOST,PORT,0,s)
			C.iniciar()
			
	except Exception as E:
		print('Erro na conexao...{0}'.format(E))
		raise E
