# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import StringVar, IntVar
from RRPGModel import Sala, Ficha
		
class LoginGUI:
	def __init__(self, master, controller):
		self.controller = controller
		self.frame = tk.Frame(master, bg='white', relief=tk.SUNKEN)
		self.frame.pack()
		
		self.vEmail2 = StringVar()
		self.vSenha2 = StringVar()
		
		self.lEmail2 = tk.Label(self.frame, text="Email:",bg='white',font=("Arial",12))
		self.eEmail2 = tk.Entry(self.frame, textvariable = self.vEmail2)
		self.lSenha2 = tk.Label(self.frame, text="Senha:",bg='white',font=("Arial",12))
		self.eSenha2 = tk.Entry(self.frame, textvariable = self.vSenha2)
		
		self.lTitulo = tk.Label(self.frame, text="RRPG", font=("Arial",18), bg = 'white')
		self.lEspaco = tk.Label(self.frame, text="", bg = 'white')
		self.lEspaco2 = tk.Label(self.frame, text="Ou", bg = 'white',font=("Arial",12))
		self.lEspaco3 = tk.Label(self.frame, text="", bg = 'white')
		
		self.btnLogar = tk.Button(self.frame, text="Logar",bg='#007FFF',font=("Arial",12))
		self.btnCadastro = tk.Button(self.frame, text="Cadastro",bg='#007FFF',font=("Arial",12))
		
		self.lTitulo.grid(row=1, column=0, sticky ='NW')
		self.lEspaco.grid(row=2, column=0)
		self.lEspaco2.grid(row=8, column=1)
		self.lEspaco3.grid(row=6, column=1)
		
		self.lEmail2.grid(row=4, column=0)
		self.eEmail2.grid(row=4, column=1)
		self.lSenha2.grid(row=5, column=0)
		self.eSenha2.grid(row=5, column=1)
		
		self.btnLogar.grid(row=7, column=1)
		self.btnCadastro.grid(row=9, column=1)
		
		self.btnLogar.bind("<Button>", lambda e: controller.logar_usuario(self.vEmail2.get(), self.vSenha2.get()))
		self.btnCadastro.bind("<Button>", lambda e: controller.cadastrar())
		
	def cadastro(self):
		win = tk.Toplevel(bg="white")
		win.wm_title("Cadastro")
		
		self.vPNome = StringVar()
		self.vSNome = StringVar()
		self.vEmail = StringVar()
		self.vSenha = StringVar()
		self.vSenhaC = StringVar()
		
		self.lPNome = tk.Label(win, text="Primeiro Nome:", bg='white')
		self.ePNome = tk.Entry(win, textvariable = self.vPNome)
		self.lSNome = tk.Label(win, text="Segundo Nome:",bg='white')
		self.eSNome = tk.Entry(win, textvariable = self.vSNome)
		self.lEmail = tk.Label(win, text="Email:",bg='white')
		self.eEmail = tk.Entry(win, textvariable = self.vEmail)
		self.lSenha = tk.Label(win, text="Senha:",bg='white')
		self.eSenha = tk.Entry(win, textvariable = self.vSenha)
		self.lSenhaC = tk.Label(win, text="Senha de Confirmação:",bg='white')
		self.eSenhaC = tk.Entry(win, textvariable = self.vSenhaC)
		
		self.lTitulo = tk.Label(win, text="RRPG", font=("Arial",18), bg = 'white')
		self.lEspaco = tk.Label(win, text="", bg = 'white')
		
		self.btnCadastrar = tk.Button(win, text="Cadastrar", bg='#007FFF')
		
		self.lTitulo.grid(row=1, column=0, sticky ='NW')
		self.lEspaco.grid(row=2, column=0)
		
		self.lPNome.grid(row=4, column=0)
		self.ePNome.grid(row=4, column=1)
		self.lSNome.grid(row=5, column=0)
		self.eSNome.grid(row=5, column=1)
		self.lEmail.grid(row=6, column=0)
		self.eEmail.grid(row=6, column=1)
		self.lSenha.grid(row=7, column=0)
		self.eSenha.grid(row=7, column=1)
		self.lSenhaC.grid(row=8, column=0)
		self.eSenhaC.grid(row=8, column=1)
		
		self.btnCadastrar.grid(row=10, column=1)
		
		self.btnCadastrar.bind("<Button>", lambda e: self.controller.cadastrar_usuario(self.vPNome.get(),self.vSNome.get(), self.vEmail.get(), self.vSenha.get(), self.vSenhaC.get()));
		
	def cadastrar_ok(self):
		messagebox.showinfo("Cadastro", "Usuario cadastrado!")
			
	def cadastrar_erro(self):
		messagebox.showinfo("Cadastro", "Usuario já cadastrado!")
		
	def logar_ok(self):
		messagebox.showinfo("Tela Inicial", "Usuario logado com sucesso!")
			
	def logar_erro(self):
		messagebox.showinfo("Tela Inicial", "Usuário/Senha inserida incorretamente!")
		
class TelaSalaGUI:
	def __init__(self, master, controller):
		self.controller = controller
		self.frame = tk.Frame(master, bg='white', relief=tk.SUNKEN)
		self.frame.pack()
		
		self.vNome = StringVar()
		
		self.lNome = tk.Label(self.frame, text="Nome:", bg='white',font=("Arial",12))
		self.eNome = tk.Entry(self.frame, textvariable = self.vNome)
		
		self.lTitulo = tk.Label(self.frame, text="RRPG", font=("Arial",18), bg = 'white')
		self.lEspaco = tk.Label(self.frame, text="", bg = 'white')
		self.lEspaco2 = tk.Label(self.frame, text="", bg = 'white')
		self.lEspaco3 = tk.Label(self.frame, text="", bg = 'white')
		self.lEspaco4 = tk.Label(self.frame, text="", bg = 'white')
		
		self.btnAbrir = tk.Button(self.frame, text="Abrir Sala", bg='#007FFF', font=("Arial",12))
		self.btnList = tk.Button(self.frame, text="Listar Salas", bg='#007FFF', font=("Arial",12))
		#self.btnSala = tk.Button(self.frame, text="Criar Salas", bg='#007FFF', font=("Arial",12))
		self.btnLogout = tk.Button(self.frame, text="Logout", bg='#007FFF', font=("Arial",12))
		self.btnCriar = tk.Button(self.frame, text="Criar", bg='#007FFF', font=("Arial",12))
		
		self.lTitulo.grid(row=1, column=0)
		self.lEspaco.grid(row=2, column=0)
		self.lEspaco2.grid(row=5, column=2)
		self.lEspaco3.grid(row=7, column=2)
		self.lEspaco4.grid(row=9, column=2)
		
		self.lNome.grid(row=3, column=2)
		self.eNome.grid(row=4, column=2)
		#self.btnSala.grid(row=6, column=2)
		self.btnCriar.grid(row=6, column=2)
		self.btnAbrir.grid(row=8, column=2)
		self.btnList.grid(row=10, column=2)
		self.btnLogout.grid(row=0, column=9)
		
		#self.btnSala.bind("<Button>", lambda e: controller.Criar());
		self.btnCriar.bind("<Button>", lambda e: controller.criar_sala(self.vNome.get()));
		self.btnAbrir.bind("<Button>", lambda e: controller.abrir_sala(self.vNome.get()));
		self.btnList.bind("<Button>", lambda e: controller.listar_salas());
		self.btnLogout.bind("<Button>", lambda e: controller.logout());
			
	#def Sala(self):
		#win = tk.Toplevel( bg= 'white')
		#win.wm_title("Criar Sala")
		
		#self.vNome = StringVar()
		
		#self.lNome = tk.Label(win, text="Nome:", bg='white',font=("Arial",12))
		#self.eNome = tk.Entry(win, textvariable = self.vNome)
		
		#self.lTitulo = tk.Label(win, text="RRPG", font=("Arial",18), bg = 'white')
		#self.lEspaco = tk.Label(win, text="", bg = 'white')
		#self.lEspaco2 = tk.Label(win, text="", bg = 'white')
		#self.lEspaco3 = tk.Label(win, text="", bg = 'white')
		#self.lEspaco4 = tk.Label(win, text="", bg = 'white')
		
		#self.btnCriar = tk.Button(win, text="Criar", bg='#007FFF', font=("Arial",12))
				
		#self.lTitulo.grid(row=1, column=0)
		#self.lEspaco.grid(row=2, column=0)
		#self.lEspaco2.grid(row=5, column=2)
		#self.lEspaco3.grid(row=7, column=2)
		#self.lEspaco4.grid(row=9, column=2)
		
		#self.lNome.grid(row=3, column=2)
		#self.eNome.grid(row=4, column=2)
		#self.btnCriar.grid(row=6, column=2)
		#self.btnAbrir.grid(row=8, column=2)
		#self.btnList.grid(row=10, column=2)
		
		#self.btnCriar.bind("<Button>", lambda e: self.controller.Criar_Sala(self.vNome.get()));
		
	def mostrar_sala(self, s, win):
		def fmostrar(e):
			self.vNome.set(s._Nome)
			#Fechar janela
			win.destroy()
		return fmostrar

	def listar(self, L):
		win = tk.Toplevel()
		win.wm_title("Lista de Salas")
		
		tk.Label(win, text="Salas",bg="black", fg="white", width=40).grid(row=0, column=0)
		tk.Label(win, text="Usuarios",bg="black", fg="white", width=40).grid(row=0, column=1)
		i = 1
		for s in L:
			LSala = tk.Label(win, text=s._Nome, fg="#007FFF")
			LSala.bind("<Button>", self.mostrar_sala(s, win))
			LSala.grid(row=i, column=0)
			tk.Label(win, text=s._Usuario).grid(row=i, column=1)
			i +=1
			
	def criar_sala_ok(self):
		messagebox.showinfo("Sala", "Sala criada!")
		
	def criar_sala_erro(self):
		messagebox.showinfo("Sala", "Erro ao criar a sala, tente novamente")
		
	def abrir_sala_ok(self):
		messagebox.showinfo("Sala", "Sala aberta!")
		
	def abrir_sala_erro(self):
		messagebox.showinfo("Sala", "Erro ao abrir a sala, tente novamente")
		
class SalaGUI:
	def __init__(self, master, controller):
		#criar plano de fundo
		self.canvas = tk.Canvas(master, width=600, height=520,bg = '#ffffff')
		self.canvas.pack()
		
		#linhas da vertical
		self.canvas.create_line(0, 0, 600, 0, fill = 'black')
		self.canvas.create_line(0, 40, 600, 40, fill = 'black')
		self.canvas.create_line(0, 80, 600, 80, fill = 'black')
		self.canvas.create_line(0, 120, 600, 120, fill = 'black')
		self.canvas.create_line(0, 160, 600, 160, fill = 'black')
		self.canvas.create_line(0, 200, 600, 200, fill = 'black')
		self.canvas.create_line(0, 240, 600, 240, fill = 'black')
		self.canvas.create_line(0, 280, 600, 280, fill = 'black')
		self.canvas.create_line(0, 320, 600, 320, fill = 'black')
		self.canvas.create_line(0, 360, 600, 360, fill = 'black')
		self.canvas.create_line(0, 400, 600, 400, fill = 'black')
		self.canvas.create_line(0, 440, 600, 440, fill = 'black')
		self.canvas.create_line(0, 480, 600, 480, fill = 'black')
		self.canvas.create_line(0, 520, 600, 520, fill = 'black')
		
		#linhas da horizontal
		self.canvas.create_line(0, 0, 0, 520, fill = 'black')
		self.canvas.create_line(40, 0, 40, 520, fill = 'black')
		self.canvas.create_line(80, 0, 80, 520, fill = 'black')
		self.canvas.create_line(120, 0, 120, 520, fill = 'black')
		self.canvas.create_line(160, 0, 160, 520, fill = 'black')
		self.canvas.create_line(200, 0, 200, 520, fill = 'black')
		self.canvas.create_line(240, 0, 240, 520, fill = 'black')
		self.canvas.create_line(280, 0, 280, 520, fill = 'black')
		self.canvas.create_line(320, 0, 320, 520, fill = 'black')
		self.canvas.create_line(360, 0, 360, 520, fill = 'black')
		self.canvas.create_line(400, 0, 400, 520, fill = 'black')
		self.canvas.create_line(440, 0, 440, 520, fill = 'black')
		self.canvas.create_line(480, 0, 480, 520, fill = 'black')
		self.canvas.create_line(520, 0, 520, 520, fill = 'black')
		self.canvas.create_line(560, 0, 560, 520, fill = 'black')
		self.canvas.create_line(600, 0, 600, 520, fill = 'black')
		
		self.canvas.pack(side=tk.LEFT)
		
		self.controller = controller
		self.frame = tk.Frame(master, bg='white', relief=tk.SUNKEN)
		self.frame.pack()
		
		self.vUsuario = StringVar()
		
		self.lUsuario = tk.Label(self.frame, text="Nome:", bg='white')
		self.eUsuario = tk.Entry(self.frame, textvariable = self.vUsuario)
		
		self.btnCriar = tk.Button(self.frame, text="Ficha", bg='#007FFF')
		self.btnSair = tk.Button(self.frame, text="Sair", bg='#007FFF')
		self.btnAdd = tk.Button(self.frame, text="Adicionar Jogador", bg='#007FFF')
		
		self.lUsuario.grid(row=1, column=10)
		self.eUsuario.grid(row=2, column=10)
		self.btnAdd.grid(row=3, column=10)
		
		self.btnCriar.grid(row=1, column=11)
		self.btnSair.grid(row=1, column=12)
		
		self.btnCriar.bind("<Button>", lambda e: controller.abrir_ficha());
		self.btnSair.bind("<Button>", lambda e: controller.sair_sala());
		self.btnAdd.bind("<Button>", lambda e: controller.adicionar_usuario(self.vUsuario.get));
		
	#chat........................................................................................
		self.mensagem = StringVar()
		self.historico = StringVar("")
		
		self.lBloco = tk.Label(self.frame,text = "Digite:",bg='white')
		self.conversa = tk.Label(self.frame, textvariable=self.historico, bg='white')
		self.espaco = tk.Label(self.frame,text = "",bg='white')
		
		self.eBloco = tk.Entry(self.frame, textvariable = self.mensagem)
		
		self.enviar = tk.Button(self.frame, text="Enviar", bg='#007FFF')
		self.atualizar = tk.Button(self.frame, text ="Atualizar" ,bg='#007FFF')
		self.limpar = tk.Button(self.frame, text ="limpar historico" ,bg='#007FFF')
		
		
		
		self.lBloco.grid(row=4, column=10)
		self.eBloco.grid(row=4, column=11)
		self.enviar.grid(row=5, column=10)
		self.atualizar.grid(row =5, column = 11)
		self.espaco.grid(row = 6,column = 10)
		self.limpar.grid(row =6, column =11)
		self.conversa.grid(row =7, column =10)
	
		
		self.enviar.bind("<Button>", lambda e: controller.receber(self.mensagem.get()))
		self.atualizar.bind("<Button>", lambda e: controller.Atualizar())
		self.limpar.bind("<Button>", lambda e: controller.limpar_chat())
		
		
		# this data is used to keep track of an 
		# item being dragged
		self._drag_data = {"x": 0, "y": 0, "item": None, "Sala" : "", "Usuario": "", "PX": 100, "PY": 100}
		
		F = Ficha.TemFicha()
		if F is True:
			s = Sala.listar()
			for l in s:
				self._drag_data["Sala"] = l._Nome
				self._drag_data["Usuario"] = l._Usuario
			
			sala = self._drag_data["Sala"]
			usuario = self._drag_data["Usuario"]
			
			px = Ficha.AbrirPosicaoX(usuario)
			py = Ficha.AbrirPosicaoY(usuario)
			
			for xp in px:
				self._drag_data["PX"] = xp._PosicaoX
			for yp in py:
				self._drag_data["PY"] = yp._PosicaoY
				
			x = self._drag_data["PX"]
			y = self._drag_data["PY"]
		else:
			x = 100
			y = 100
		
		# create a couple movable objects
		self._create_token((x, y), "black")
		
		# add bindings for clicking, dragging and releasing over
		# any object with the "token" tag
		self.canvas.tag_bind("token", "<ButtonPress-1>", self.OnTokenButtonPress)
		self.canvas.tag_bind("token", "<ButtonRelease-1>", self.OnTokenButtonRelease)
		self.canvas.tag_bind("token", "<B1-Motion>", self.OnTokenMotion)
		
	def _create_token(self, coord, color):
		'''Create a token at the given coordinate in the given color'''
		(x,y) = coord
		self.canvas.create_oval(x-20, y-20, x+20, y+20, outline=color, fill=color, tags="token")
                                
	def OnTokenButtonPress(self, event):
		'''Being drag of an object'''
		# record the item and its location
		self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
		self._drag_data["x"] = event.x
		self._drag_data["y"] = event.y
		
	def OnTokenButtonRelease(self, event):
		'''End drag of an object'''
		# reset the drag information
		self._drag_data["item"] = None
		self._drag_data["x"] = 0
		self._drag_data["y"] = 0
		
	def OnTokenMotion(self, event):
		'''Handle dragging of an object'''
		# compute how much this object has moved
		delta_x = event.x - self._drag_data["x"]
		delta_y = event.y - self._drag_data["y"]
		# move the object the appropriate amount
		self.canvas.move(self._drag_data["item"], delta_x, delta_y)
		# record the new position
		self._drag_data["x"] = event.x
		self._drag_data["y"] = event.y
		
		sala = self._drag_data["Sala"]
		usuario = self._drag_data["Usuario"]
		x = event.x
		y = event.y
		Ficha.AdicionarPosicaoX(x, usuario)
		Ficha.AdicionarPosicaoY(y, usuario)
				
	def Conversa(self,msg):
		self.historico.set(msg)
		
	def limparM(self):
		self.mensagem.set("")
		
	def historico_erro(self):
		messagebox.showinfo("arquivo nao existe", "Nao existe historico do chat")
		
	def adicionar_usuario_ok(self):
		messagebox.showinfo("Sala", "Usuario adicionado")
		
	def adicionar_usuario_erro(self):
		messagebox.showinfo("Sala", "Erro ao adicionar usuario")
	
	def abrir_ficha_ok(self):
		messagebox.showinfo("Ficha", "Ficha aberta!")
		
	def abrir_ficha_erro(self):
		messagebox.showinfo("Ficha", "Erro ao abrir a ficha, tente novamente")
		
class FichaGUI:
	def __init__(self, master, controller):
		self.controller = controller
		self.frame = tk.Frame(master, bg='white', relief=tk.SUNKEN)
		self.frame.pack()
		
		self.vNome = StringVar()
		self.vRaca = StringVar()
		self.vClasse = StringVar()
		self.vNivel = IntVar()
		self.vVida = IntVar()
		self.vCA = IntVar()
		self.vDeslocamento = IntVar()
		self.vAntecedente = StringVar()
		self.vForca = IntVar()
		self.vDestreza = IntVar()
		self.vConstituicao = IntVar()
		self.vInteligencia= IntVar()
		self.vSabedoria = IntVar()
		self.vCarisma = IntVar()
		self.vEquipamento = StringVar()
		self.vAtaques = StringVar()
		self.vPericias = StringVar()
		self.vTestes = StringVar()
		self.vInfo = StringVar()
		
		self.lNome = tk.Label(self.frame, text="Nome:", bg='white')
		self.eNome = tk.Entry(self.frame, textvariable=self.vNome)
		self.lRaca = tk.Label(self.frame, text="Raça:", bg='white')
		self.eRaca = tk.Entry(self.frame, textvariable=self.vRaca)
		self.lClasse = tk.Label(self.frame, text="Classe:", bg='white')
		self.eClasse = tk.Entry(self.frame, textvariable=self.vClasse)
		self.lNivel = tk.Label(self.frame, text="Nível:", bg='white')
		self.eNivel = tk.Entry(self.frame, textvariable=self.vNivel)
		self.lVida = tk.Label(self.frame, text="Vida:", bg='white')
		self.eVida = tk.Entry(self.frame, textvariable=self.vVida)
		self.lCA = tk.Label(self.frame, text="CA:", bg='white')
		self.eCA = tk.Entry(self.frame, textvariable=self.vCA)
		self.lDeslocamento = tk.Label(self.frame, text="Deslocamento:", bg='white')
		self.eDeslocamento = tk.Entry(self.frame, textvariable=self.vDeslocamento)
		self.lAntecedente = tk.Label(self.frame, text="Antecedente:", bg='white')
		self.eAntecedente = tk.Entry(self.frame, textvariable=self.vAntecedente)
		self.lForca = tk.Label(self.frame, text="Força:", bg='white')
		self.eForca = tk.Entry(self.frame, textvariable=self.vForca)
		self.lDestreza = tk.Label(self.frame, text="Destreza:", bg='white')
		self.eDestreza = tk.Entry(self.frame, textvariable=self.vDestreza)
		self.lConstituicao = tk.Label(self.frame, text="Constituição:", bg='white')
		self.eConstituicao = tk.Entry(self.frame, textvariable=self.vConstituicao)
		self.lInteligencia = tk.Label(self.frame, text="Inteligência:", bg='white')
		self.eInteligencia = tk.Entry(self.frame, textvariable=self.vInteligencia)
		self.lSabedoria = tk.Label(self.frame, text="Sabedoria:", bg='white')
		self.eSabedoria = tk.Entry(self.frame, textvariable=self.vSabedoria)
		self.lCarisma = tk.Label(self.frame, text="Carisma:", bg='white')
		self.eCarisma = tk.Entry(self.frame, textvariable=self.vCarisma)
		
		self.lEquipamento = tk.Label(self.frame, text="Equipamento:", bg='white')
		self.eEquipamento = tk.Entry(self.frame, textvariable=self.vEquipamento)

		self.lInfo = tk.Label(self.frame, text="Informação do Personagem:", bg='white')
		self.eInfo = tk.Entry(self.frame, textvariable = self.vInfo)
		
		self.lAtaques = tk.Label(self.frame, text="Ataques:", bg='white')
		self.eAtaques = tk.Entry(self.frame, textvariable=self.vAtaques)
		
		self.lPericias = tk.Label(self.frame, text="Pericias:", bg='white')
		self.ePericias = tk.Entry(self.frame, textvariable=self.vPericias)
		
		self.lTestes = tk.Label(self.frame, text="Testes:", bg='white')
		self.eTestes = tk.Entry(self.frame, textvariable=self.vTestes)
		
		self.btnSalvar = tk.Button(self.frame, text="Salvar",bg='#007FFF')
		self.btnAtualizar = tk.Button(self.frame, text="Atualizar",bg='#007FFF')
		self.btnList = tk.Button(self.frame, text="Listar Fichas",bg='#007FFF')
		self.btnFechar = tk.Button(self.frame, text="Fechar",bg='#007FFF')
		
		self.lNome.grid(row=1, column=11)
		self.eNome.grid(row=2, column=11)
		self.lRaca.grid(row=1, column=12)
		self.eRaca.grid(row=2, column=12)
		self.lClasse.grid(row=1, column=13)
		self.eClasse.grid(row=2, column=13)
		self.lNivel.grid(row=1, column=14)
		self.eNivel.grid(row=2, column=14)
		self.lVida.grid(row=3, column=12)
		self.eVida.grid(row=4, column=12)
		self.lCA.grid(row=3, column=13)
		self.eCA.grid(row=4, column=13)
		self.lDeslocamento.grid(row=3, column=14)
		self.eDeslocamento.grid(row=4, column=14)
		self.lAntecedente.grid(row=1, column=15)
		self.eAntecedente.grid(row=2, column=15)
		self.lForca.grid(row=5, column=11)
		self.eForca.grid(row=6, column=11)
		self.lDestreza.grid(row=7, column=11)
		self.eDestreza.grid(row=8, column=11)
		self.lConstituicao.grid(row=9, column=11)
		self.eConstituicao.grid(row=10, column=11)
		self.lInteligencia.grid(row=11, column=11)
		self.eInteligencia.grid(row=12, column=11)
		self.lSabedoria.grid(row=13, column=11)
		self.eSabedoria.grid(row=14, column=11)
		self.lCarisma.grid(row=15, column=11)
		self.eCarisma.grid(row=16, column=11)
		self.lEquipamento.grid(row=11, column=13)
		self.eEquipamento.grid(row=12, column=13)
		self.lInfo.grid(row=9, column=15)
		self.eInfo.grid(row=10, column=15)
		self.lAtaques.grid(row=9, column=13)
		self.eAtaques.grid(row=10, column=13)
		self.lPericias.grid(row=9, column=12)
		self.ePericias.grid(row=10, column=12)
		self.lTestes.grid(row=7, column=12)
		self.eTestes.grid(row=8, column=12)
		
		self.btnSalvar.grid(row=17, column=12)
		self.btnAtualizar.grid(row=17, column=13)
		self.btnList.grid(row=17, column=14)
		self.btnFechar.grid(row=17, column=15)
		
		self.btnSalvar.bind("<Button>", lambda e: controller.salvar_ficha(self.vNome.get(), self.vRaca.get(), self.vClasse.get(), self.vNivel.get(), self.vVida.get(), self.vCA.get(), self.vDeslocamento.get(), self.vAntecedente.get(), self.vForca.get(), self.vDestreza.get(), self.vConstituicao.get(), self.vInteligencia.get(), self.vSabedoria.get(), self.vCarisma.get(), self.vTestes.get(), self.vPericias.get(), self.vAtaques.get(),self.vEquipamento.get(), self.vInfo.get()));
		self.btnAtualizar.bind("<Button>", lambda e: controller.atualizar_ficha(self.vNome.get(), self.vRaca.get(), self.vClasse.get(), self.vNivel.get(), self.vVida.get(), self.vCA.get(), self.vDeslocamento.get(), self.vAntecedente.get(), self.vForca.get(), self.vDestreza.get(), self.vConstituicao.get(), self.vInteligencia.get(), self.vSabedoria.get(), self.vCarisma.get(), self.vTestes.get(), self.vPericias.get(), self.vAtaques.get(),self.vEquipamento.get(), self.vInfo.get()));
		self.btnList.bind("<Button>", lambda e: controller.listar_fichas());
		self.btnFechar.bind("<Button>", lambda e: controller.fechar());
		
	def mostrar_ficha(self, f, win):
		def fmostrar(e):
			self.vNome.set(f._Nome)
			self.vRaca.set(f._Raca)
			self.vClasse.set(f._Classe)
			self.vNivel.set(f._Nivel)
			self.vVida.set(f._Vida)
			self.vCA.set(f._CA)
			self.vDeslocamento.set(f._Deslocamento)
			self.vAntecedente.set(f._Antecedente)
			self.vForca.set(f._Forca)
			self.vDestreza.set(f._Destreza)
			self.vConstituicao.set(f._Constituicao)
			self.vInteligencia.set(f._Inteligencia)
			self.vSabedoria.set(f._Sabedoria)
			self.vCarisma.set(f._Carisma)
			self.vEquipamento.set(f._Equipamento)
			self.vAtaques.set(f._Ataques)
			self.vPericias.set(f._Pericias)
			self.vTestes.set(f._Testes)
			self.vInfo.set(f._InformacaoPersonagem)
			win.destroy()
		return fmostrar

	def listar(self, L):
		win = tk.Toplevel()
		win.wm_title("Lista de Fichas")
		
		tk.Label(win, text="Fichas",bg="black", fg="white", width=40).grid(row=0, column=2)
		i = 1
		for f in L:
			LFicha = tk.Label(win, text=f._Nome, fg="#007FFF")
			LFicha.bind("<Button>", self.mostrar_ficha(f, win))
			LFicha.grid(row=i, column=2)
			i += 1
		
	def salvar_ficha_ok(self):
		messagebox.showinfo("Ficha", "Ficha salva!")
		
	def salvar_ficha_erro(self):
		messagebox.showinfo("Ficha", "Erro ao salvar a ficha, tente novamente")
		
	def atualizar_ficha_ok(self):
		messagebox.showinfo("Ficha", "Ficha atualizada!")
		
	def atualizar_ficha_erro(self):
		messagebox.showinfo("Ficha", "Erro ao atualizar a ficha, tente novamente")
		
