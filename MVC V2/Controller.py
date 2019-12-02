# -*- coding: utf-8 -*-........................................

import s
import time

import socket
import sys
from tinydb import TinyDB, Query
import json
import tkinter as tk
from tkinter import *
from RRPGModel import ErroSenhaUsuarioIncorreto, ErroComandoInvalido, ErroOpcaoNaoValida, ErroCriacaoUsuario, ErroCriarFicha, ErroCriacaodeSala, Usuario, Ficha, Sala, RolagemdeDados
from RRPGView import LoginGUI, TelaSalaGUI, SalaGUI, FichaGUI
from threading import Thread

HOST = '127.0.0.1'  # Endereco IP do servidor
PORT = 12011        # Porta utilizada no servidor

class Controller(Thread):

	_data = {"Sala":"", "Usuario":"", "UsuarioC":""}

	def __init__(self, n, host, port):
		self.root = tk.Tk()
		self.root.geometry('900x520+100+100')
		self.root.configure(bg = '#ffffff')
		
		self._host = host
		self._port = port
		#self.__nome = nome criar variavel nome, que indicará o nome do usuario no chat (ultimamente o nome é simplismente "Usuario")
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
		
	#Tela Inicial.....................................................................
		
	def cadastrar(self):
		self.view.cadastro()
		
	def cadastrar_usuario(self, pnome, snome, email, senha, senhac):
		try:
			U = Usuario(pnome, snome, email, senha, senhac)
			resposta = Usuario.Cadastrar(U)
			if resposta == True:
				self.view.cadastrar_ok()
			else:
				raise ErroCriacaoUsuario()
		except ErroCriacaoUsuario:
			self.view.cadastrar_erro()

	def logar_usuario(self, email, senha):
		try:
			resposta = Usuario.Logar(email, senha)
			if resposta is True:
				Controller._data["Usuario"] = email
				self.view.logar_ok()
				self.root.destroy()
				Controller(1,HOST,PORT)
			else:
				self.view.logar_erro()
		except ErroSenhaUsuarioIncorreto:
			self.view.logar_erro()
			
	
	#Tela das Salas.............................................................
		
	def criar(self):
		self.view.Sala()
	
	def criar_sala(self, nome):
		try:
			usuario = Controller._data["Usuario"]
			S = Sala(nome, usuario)
			if S._Nome !="" and S._Usuario != "":
				Sala.Criar(S)
				self.view.criar_sala_ok()
			else:
				self.view.criar_sala_erro()
		except ErroCriacaodeSala:
			self.view.criar_sala_erro()
	
	def listar_salas(self):
		self.view.listar(Sala.listar())
		
	def abrir_sala(self, nome):
		try:
			if nome !="":
				L = Sala.Abrir(nome)
				usuario = Controller._data["Usuario"]
				for s in L:
					sala = s._Nome
					u = s._Usuario
					for x in u:
						for q in x:
							Controller._data["UsuarioC"] = q
							uc = Controller._data["UsuarioC"]
							if uc == usuario:
								Controller._data["Sala"] = sala
								self.root.destroy()
								Controller(2,HOST,PORT)
							else:
								print(u)
								print(uc)
								print(usuario)
								self.view.abrir_sala_erro()
			else:
				self.view.abrir_sala_erro()
		except ErroOpcaoNaoValida:
			self.view.abrir_sala_erro()
			
	def logout(self):
		self.root.destroy()
		Controller(0,HOST,PORT)
			
	#Sala........................................................................

	def abrir_ficha(self):
		Controller(3,HOST,PORT)
		self.view.abrir_ficha_ok
		
	def adicionar_usuario(self,usuario):
		try:
			sala = Controller._data["Sala"]
			Sala.Atualizar_Usuario(sala,usuario)
			self.view.adicionar_usuario_ok()
		except ErroComandoInvalido:
			self.view.adicionar_usuario_erro()
			
	def sair_sala(self):
		self.root.destroy()
		Controller(1,HOST,PORT)
		
	#Chat.........................................................................
	
	def receber(self,msg):
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
		
		try:
			sala = Controller._data["Sala"]
			usuario = Controller._data["Usuario"]
			F = Ficha(nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car, equip, info, ataq, peri, test, usuario, sala)
			Ficha.Criar(F)
			self.view.salvar_ficha_ok()
		except ErroCriarFicha:
			self.view.salvar_ficha_erro()
			
	def atualizar_ficha(self, nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car, equip, info, ataq, peri, test):
		
		try:
			Ficha.Atualizar(nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car, equip, info, ataq, peri, test)
			self.view.salvar_ficha_ok()
		except ErroCriarFicha:
			self.view.salvar_ficha_erro()
			
	def listar_fichas(self):
		self.view.listar(Ficha.listar())
		
	def fechar(self):
		self.root.destroy()
		
