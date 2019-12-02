# -*- coding: utf-8 -*-

import socket
import sys
from tinydb import TinyDB, Query
import random
import threading
import time
import _thread
import pickle
import select
import json

class MyEncoder(json.JSONEncoder):
	def default(self, o):
		d = vars(o) 
		d['tipo'] = o.__class__.__name__  
		return d
		
	@staticmethod
	def decode(d):
		if d['tipo'] == 'Usuario':
			return Usuario(d['_PNome'],d['_SNome'],d['_Email'],d['_Senha'],d['_SenhaC'])
		if d['tipo'] == 'Ficha':
			return Ficha(d['_Nome'],d['_Raca'],d['_Classe'],d['_Nivel'],d['_Vida'],d['_CA'],d['_Deslocamento'],d['_Antecedente'],d['_Forca'],d['_Destreza'],d['_Constituicao'],d['_Inteligencia'],d['_Sabedoria'],d['_Carisma'],d['_Equipamento'],d['_Ataques'],d['_Pericias'],d['_Testes'],d['_InformacaoPersonagem'],d['_Usuario'],d['_Sala'],d['_PosicaoX'],d['_PosicaoY'])
		if d['tipo'] == 'Sala':
			return Sala(d['_Nome'],d['_Usuario'],d['_Chat'])
		if d['tipo'] == 'RolagemdeDados':
			return RolagemdeDados(d['_ND'],d['_DPR'])
					
class ErroChat(Exception):
	def __init__(self):
		super().__init__("Erro no Chat")
	
class ErroSenhaUsuarioIncorreto(Exception):
	def __init__(self):
		super().__init__("Usuário/Senha inserida incorretamente")
	
class ErroNomeIncorreto(Exception):
	def __init__(self):
		super().__init__("Nome inserido incorreto")
	
class ErroCriarFicha(Exception):
	def __init__(self):
		super().__init__("Erro ao criar a ficha")
	
class ErroComandoInvalido(Exception):
	def __init__(self):
		super().__init__("Comando invalido")
	
class ErroInteracao(Exception):
	def __init__(self):
		super().__init__("Erro de interação")
	
class ErroOpcaoNaoValida(Exception):
	def __init__(self):
		super().__init__("Opção não valida")
	
class ErroCriacaoUsuario(Exception):
	def __init__(self):
		super().__init__("Usuario já existe")
		
class ErroCriacaodeSala(Exception):
	def __init__(self):
		super().__init__("Entrada incorreta, preencha os campos novamente")
	

class Usuario:
	def __init__(self, pnome, snome, email, senha, senhac):
		
		self._PNome = pnome
		self._SNome = snome
		self._Email = email
		self._Senha = senha
		self._SenhaC = senhac
	
	@staticmethod
	def Cadastrar(U):
		if U._PNome !="" and U._SNome !="" and U._Email !="" and U._Senha !="" and U._SenhaC !="":
			with  TinyDB('Usuarios.json') as db:
				Q = Query()
				d = db.search(Q._Email == U._Email)
				print(d)
				if d != []:
					for x in d:
						print("passa")
						u = Usuario.fromDict(x)
						print(u._Email)
						print(U._Email)
						return False
				else:
					db.insert(U.toDict())
					return True
									
	@staticmethod
	def Logar(email, senha):
		with TinyDB('Usuarios.json') as db:
			Q = Query()
			l = db.search(Q._SenhaC == senha)
			for x in l:
				u = Usuario.fromDict(x)
				if u._Email == email:
					return True 
				else:
					return False
					
	def toDict(self):
		s = json.dumps(self, cls=MyEncoder)
		return json.loads(s)
		
	@staticmethod
	def fromDict(d):
		s = json.dumps(d)
		return json.loads(s, object_hook=MyEncoder.decode)
		
	@property
	def PNome(self):
		return self._PNome
			
	@property
	def SNome(self):
		return self._SNome
		
	@property
	def Email(self):
		return self._Email
		
	@property
	def Senha(self):
		return self._Senha
		
	@property
	def SenhaConfirmacao(self):
		return self._SenhaC

class Ficha:
	def __init__(self, nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car, equip, ataq, peri, test, info, usuario, sala):
		self._Nome = nome
		self._Raca = raca
		self._Classe = classe
		self._Nivel = nivel
		self._Vida = vida
		self._CA = ca
		self._Deslocamento = deslc
		self._Antecedente = antec
		self._Forca = forc
		self._Destreza = dex
		self._Constituicao = cons
		self._Inteligencia = intl
		self._Sabedoria = sab
		self._Carisma = car
		self._Equipamento = equip
		self._Ataques = ataq
		self._Pericias = peri
		self._Testes = test
		self._InformacaoPersonagem = info
		self._Usuario = usuario
		self._Sala = sala
		self._PosicaoX = 0
		self._PosicaoY = 0
		
	@staticmethod
	def Criar(F):
		if F._Nome !="" and F._Raca !="" and F._Classe !="" and F._Nivel !="" and F._Vida !="" and F._CA !="" and F._Deslocamento !="" and F._Antecedente !="" and F._Forca !="" and F._Destreza !="" and F._Constituicao !="" and F._Inteligencia !="" and F._Sabedoria !="" and F._Carisma !="" and F._Equipamento  !="" and F._Ataque !="" and F._Pericias !="" and F._Testes !="" and F._InformacaoPersonagem !="":
			with TinyDB('Fichas.json') as db:
				db.insert(F.toDict())
		else:
			raise ErroCriarFicha()
				
	@staticmethod
	def listar():
		L = []
		with TinyDB('Fichas.json') as db:
			for f in db:
				L.append(Ficha(f['_Nome'],f['_Raca'],f['_Classe'],f['_Nivel'],f['_Vida'],f['_CA'],f['_Deslocamento'],f['_Antecedente'],f['_Forca'],f['_Destreza'],f['_Constituicao'],f['_Inteligencia'],f['_Sabedoria'],f['_Carisma'],f['_Equipamento'],f['_Ataques'],f['_Pericias'],f['_Testes'],f['_InformacaoPersonagem'],f['_Usuario'],f['_Sala']))
		return L
		
	@staticmethod
	def AdicionarPosicaoX(x, usuario):
		with TinyDB('Fichas.json') as db:
			Q = Query()
			l = db.update({'_PosicaoX': x }, Q._Usuario == usuario)
				
	@staticmethod
	def AdicionarPosicaoY(y, usuario):
		with TinyDB('Fichas.json') as db:
			Q = Query()
			l = db.update({'_PosicaoY': y }, Q._Usuario == usuario)
	
	@staticmethod
	def AbrirPosicaoX(usuario):
		with TinyDB('Fichas.json') as db:
			F = []
			Q = Query()
			l = db.search(Q._Usuario == usuario)
			for x in l:
				f = Ficha.fromDict(x)
				F.append(Ficha(x['_PosicaoX']))
		return F
		
	@staticmethod
	def AbrirPosicaoY(usuario):
		with TinyDB('Fichas.json') as db:
			F = []
			Q = Query()
			l = db.search(Q._Usuario == usuario)
			for x in l:
				f = Ficha.fromDict(x)
				F.append(Ficha(x['_PosicaoY']))
		return F
		
	@staticmethod
	def TemFicha():
		with TinyDB('Fichas.json') as db:
			for x in db:
				if x!= "":
					return True
				else:
					return False
	
	@staticmethod			
	def Atualizar(nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car, equip, ataq, peri, test, info):
		with TinyDB('Fichas.json') as db:
			Q = Query()
			l = db.update({'_Nome': nome},{'_Raca': raca},{'_Classe': classe},{'_Nivel': nivel},{'_Vida': vida},{'_CA': ca},{'_Deslocamento' :deslc},{'_Antecedente': antec},{'_Forca': forc},{'_Destreza': dex},{'_Constituicao': cons},{'_Inteligencia': intl},{'_Sabedoria': sab},{'_Carisma': car},{'_Equipamento': equip},{'_Ataques': ataq},{'_Pericias': peri},{'_Testes': test},{'_InformacaoPersonagem': info}, Q._Nome == nome)
		
	def toDict(self):
		s = json.dumps(self, cls=MyEncoder)
		return json.loads(s)
        
	@staticmethod
	def fromDict(d):
		s = json.dumps(d)
		return json.loads(s, object_hook=MyEncoder.decode)
		
	def __repr__(self):
		return 'Ficha({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18})'.format(self._Nome,self._Raca,self._Classe,self._Nivel,self._Vida,self._CA,self._Deslocamento,self._Antecedente,self._Forca,self._Destreza,self._Constituicao,self._Inteligencia,self._Sabedoria,self._Carisma,self._Equipamento,self._Ataques,self._Pericias,self._Testes,self._InformacaoPersonagem)
		
	@property
	def Nome(self):
		return self._Nome
		
	@property
	def Raca(self):
		return self._Raca
		
	@property
	def Classe(self):
		return self._Classe
		
	@property
	def Nivel(self):
		return self._Nivel
		
	@property
	def Vida(self):
		return self._Vida
		
	@property
	def CA(self):
		return self._CA
		
	@property
	def Deslocamento(self):
		return self._Deslocamento
		
	@property
	def Antecedente(self):
		return self._Antecedente 
		
	@property
	def Forca(self):
		return self._Forca
		
	@property
	def Destreza(self):
		return self._Destreza
		
	@property
	def Constituicao(self):
		return self._Constituicao
		
	@property
	def Inteligencia(self):
		return self._Inteligencia
		
	@property
	def Sabedoria(self):
		return self._Sabedoria
		
	@property
	def Carisma(self):
		return self._Carisma
		
	@property
	def Equipamento(self):
		return self._Equipamento
		
	@property
	def InformacaoPersonagem(self):
		return self._InformacaoPersonagem
		
	@property
	def Ataque(self):
		return self._Ataques
		
	@property
	def Pericia(self):
		return self._Pericias
		
	@property
	def Teste(self):
		return self._Testes
		
	@property
	def Usuario(self):
		return self._Usuario
			
	@property
	def Sala(self):
		return self._Sala
		
	@property
	def PosicaoX(self):
		return self._PosicaoX
		
	@property
	def PosicaoY(self):
		return self._PosicaoY
		
class RolagemdeDados:
	
	def __init__(self):
		pass
		
	@staticmethod
	def RolarDados(ND, DPR):
		soma = 0
		i = 0
		dado = []
		if ND > 0 and (DPR == 4 or DPR == 6 or DPR == 8 or DPR == 10 or DPR ==12 or DPR ==20 or DPR == 100):
				
			for x in range(ND):
				
				dado.append(random.randint(1,DPR))
				soma = soma+dado[i] 
				i = i+1
			return dado, soma
		else:
			raise ErroComandoInvalido('Nao existe esse dados')
			
	def toDict(self):
		s = json.dumps(self, cls=MyEncoder)
		return json.loads(s)
			
	@staticmethod
	def fromDict(d):
		s = json.dumps(d)
		return json.loads(s, object_hook = MyEncoder.decode)

class Sala:
	def __init__(self, nome, usuario):
		
		self._Nome = nome
		self._Usuario = [usuario]
		self._Chat = []
	
	@staticmethod
	def Criar(S):
		if S._Nome !="" and S._Usuario != "":
			with TinyDB('Salas.json') as db:
				db.insert(S.toDict())
					
	@staticmethod
	def listar():
		L = []
		with TinyDB('Salas.json') as db:
			for s in db:
				L.append(Sala(s['_Nome'],s['_Usuario']))
		return L

	@staticmethod
	def Abrir(nome):
		L = []
		with TinyDB('Salas.json') as db:
			Q = Query()
			l = db.search(Q._Nome == nome)
			for x in l:
				L.append(Sala(x['_Nome'],x['_Usuario']))
		return L
		
	@staticmethod
	def Atualizar_Usuario(sala, usuario):
		with TinyDB('Salas.json') as db:
			Q = Query()
			l = db.update({'_Usuario': usuario}, Q._Nome == sala)
		
	
	def __repr__(self):
		return 'Sala({0},{1})'.format(self._Nome,self._Usuario)
		
	def toDict(self):
		s = json.dumps(self, cls=MyEncoder)
		return json.loads(s)
		
	@staticmethod
	def fromDict(d):
		s = json.dumps(d)
		return json.loads(s, object_hook=MyEncoder.decode)
        
	@property
	def Nome(self):
		return self._Nome
		
	@property
	def Usuario(self):
		return self._Usuario
		
