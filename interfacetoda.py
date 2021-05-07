import tkinter as tk
import webbrowser


def login():
	place = tk.Tk()
	place.title("login")
	place.geometry("650x500")

	#fundo da pagina
	fundo01 = tk.Label(place, padx=5, pady=5,background="gray")
	fundo01.place(x= 150, y = 125)
	fundo01.config(border=6, height = 20, width = 50 )
	

	#cabeçalho /link site
	logo = tk.Button (place, text="Folha CPA", foreground="white", command=lambda: webbrowser.open('https://mail.google.com/mail/u/0/#inbox'))
	logo.place(x = 243, y = 30)		
	logo.configure(relief="ridge", font="Arial 24 bold", border=6, background="gray")

	#campo escrito
	login1 = tk.Label(place, text = "Login")
	login1.place(x = 315,y = 160) 			
	senha1 = tk.Label(place,text = "Senha")
	senha1.place(x = 315,y = 250)

	#caixa de entrada
	entlog = tk.Entry(place, bd = 5)	
	entlog.place(x = 270,y = 190)
	entsen = tk.Entry(place,bd = 5)	
	entsen.place(x = 270,y = 280)

	#botoes
	ent1 = tk.Button(place, text = "Entrar", command=login)
	ent1.place(x = 305, y = 400)
	ent1.configure(relief="ridge", border=6,font="bold", height = 1, width = 5)

	

	botaos = tk.Button(place,text = "sair",command=place.quit)
	botaos.place( x = 616, y= 2)

def cadastro():
	place = tk.Tk()
	place.title("Cadastro")
	place.geometry("1060x600")

	#fundo da pagina
	fundo01 = tk.Label(place, padx=5, pady=5,background="gray")
	fundo01.place(x= 10, y = 125)
	fundo01.config(border=6, height = 27, width = 145)
	

	#cabeçalho /link site
	logo = tk.Button (place, text="Folha CPA", foreground="white",)
	logo.place(x = 400, y = 30)		
	logo.configure(relief="ridge", font="Arial 24 bold", border=6, background="gray")

	#campo escrito
	nome = tk.Label(place, text = " Nome : ")
	nome.place(x = 35,y = 140)
	entnome = tk.Entry(place, bd = 5, width=45)	
	entnome.place(x = 35,y = 170)

	email = tk.Label(place, text = " Email : ")
	email.place(x = 35,y = 230)
	entemail = tk.Entry(place, bd = 5, width=45)	
	entemail.place(x = 35,y = 260)

	datan = tk.Label(place, text = " Data de nascimento : ")
	datan.place(x = 35,y = 320)
	datan = tk.Entry(place, bd = 5)
	datan.place(x = 35,y = 350)

	matricula = tk.Label(place, text = " Matricula : ")
	matricula.place(x = 35,y = 410)
	entmatricula = tk.Entry (place, bd = 5, width=35)
	entmatricula.place(x = 35,y = 440)

	#sxd = tk.Checkbutton(place, text = " sexo : ")
	#sxd.place(x = 35,y = 420)
	#entemail = tk.Entry(place, bd = 5)	
	#entemail.place(x = 35,y = 450)

	#segunda fileira
	uf = tk.Label(place, text = " UF : ")
	uf.place(x = 400,y = 140)
	entuf = tk.Entry(place, bd = 5)	
	entuf.place(x = 400,y = 170)

	cep = tk.Label(place, text = " CEP : ")
	cep.place(x = 400,y = 220)
	entcep = tk.Entry(place, bd = 5)	
	entcep.place(x = 400,y = 250)

	endereço = tk.Label(place, text = " endereço : ")
	endereço.place(x = 400,y = 300)
	entendereço = tk.Entry(place, bd = 5, width=45)	
	entendereço.place(x = 400,y = 330)


	#3 coluna
	tel1 = tk.Label(place, text = " Telefone 1  : ")
	tel1.place(x = 800,y = 140)
	enttel1 = tk.Entry(place, bd = 5)	
	enttel1.place(x = 800,y = 170)

	tel2 = tk.Label(place, text = " telefone 2 : ")
	tel2.place(x = 800,y = 210)
	enttel2 = tk.Entry(place, bd = 5)	
	enttel2.place(x = 800,y = 240)

	#fundo senha
	fundo01 = tk.Label(place, padx=5, pady=5,background="black")
	fundo01.place(x= 770, y = 300)
	fundo01.config(border=6, height = 13, width = 30)


	#campo senha
	texsen = tk.Label(place, text = " Definir senha:  ")
	texsen.place(x = 840,y = 310)

	sen1 = tk.Label(place, text = " Digite a senha : ")
	sen1.place(x = 800,y = 360)
	entsen1 = tk.Entry(place, bd = 5)	
	entsen1.place(x = 800,y = 390)

	sen2 = tk.Label(place, text = " Repita a senha : ")
	sen2.place(x = 800,y = 440)
	entsen2 = tk.Entry(place, bd = 5)	
	entsen2.place(x = 800,y = 470)

	

	chkValue1 = tk.BooleanVar() 
	chkValue1.set(True)

	chkValue2 = tk.BooleanVar() 
	chkValue2.set(True)

	chkExample = tk.Checkbutton(place, text=' Masculino ', var=chkValue1) 
	chkExample.place(x = 400, y = 370)

	chkExample2 = tk.Checkbutton(place, text=' Feminino ', var=chkValue2) 
	chkExample2.place(x = 400, y = 400)


	
	#botoes
	ent1 = tk.Button(place, text = " Enviar ", command=cadastro)
	ent1.place(x = 490, y = 500)
	ent1.configure(relief="ridge", border=6,font="bold", height = 1, width = 5)

	botaos = tk.Button(place,text = "sair",command=place.quit)
	botaos.place( x = 1005, y= 2)

def perguntas():
	place = tk.Tk()
	place.title("login")
	place.geometry("1350x660")
	place.configure(background="#999")

	#fundo da pagina
	fundo01 = tk.Label(place, padx=5, pady=5,background="gray")
	fundo01.place(x= 30, y = 80)
	fundo01.config(border=6, height = 37, width = 185 )

	#botoes da pag
	ent1 = tk.Button(place, text = "Proximo", command = perguntas2)
	ent1.place(x = 1280, y = 620)
	#ent1.configure( relief="ridge", border=6, font="10 bold", height = 1, width = 5)

	ent2 = tk.Button(place, text = "Enviar", command=place.after)
	ent2.place(x = 1190, y = 620)
	#ent2.configure( relief="ridge", border=6, font="10 bold", height = 1, width = 5)

	#ent3 = tk.Button(place, text = "Anterior", command=inicio)
	#ent3.place(x = 50, y = 620)
	#ent3.configure( relief="ridge", border=6, font="10 bold", height = 1, width = 5)

	botaos = tk.Button(place,text = "sair",command=place.quit)
	botaos.place( x = 1330, y= 2)
	

	#Logo /link site
	logo = tk.Button (place, text="Folha CPA", foreground="white", command=lambda: webbrowser.open('https://mail.google.com/mail/u/0/#inbox'))
	logo.place(x = 620, y = 10)		
	logo.configure(relief="ridge", font="Arial 20 bold", border=4, background="gray")

	#infomar pagina
	infpg1 = tk.Label (place, text= " Pagina 1 ")
	infpg1.place(x = 20, y = 20)
	infpg1.config(relief="ridge", font="Arial 8 ", background="#999")

	#cabeçalho primeiro modulo de questoes
	titulo1 = tk.Label (place, text= " 1)Acadêmico – Disciplinas ")
	titulo1.place(x = 50, y = 100)
	titulo1.config(relief="ridge", font="Arial 12 bold", border=3, background="gray")

	# Enunciado 1)questao questao
	pegt1a = tk.Label (place, text= "A) Voce acredita que as disciplinas cursadas contribuíram para\n sua formação integral, como cidadão e profissional.", anchor='w')
	pegt1a.place(x = 50, y = 140, width=395, height=35,)

	#bloco variaveis da resposta 1.A
	ckp10 = tk.IntVar() 
	ckp10.set(0)
	ckp11 = tk.IntVar() 
	ckp11.set(1)
	ckp12 = tk.IntVar() 
	ckp12.set(2)
	ckp13 = tk.IntVar() 
	ckp13.set(3)
	ckp14 = tk.IntVar() 
	ckp14.set(4)
	ckp15 = tk.IntVar() 
	ckp15.set(5)
	ckp16 = tk.IntVar() 
	ckp16.set(6)

    #checkbox resposta, questao 1.A
	chk10 = tk.Checkbutton(place, text='0', var=ckp10) 
	chk10.place(x = 50, y = 180)
	chk11 = tk.Checkbutton(place, text='1', var=ckp11) 
	chk11.place(x = 80, y = 180)
	chk12 = tk.Checkbutton(place, text='2', var=ckp12) 
	chk12.place(x = 110, y = 180)
	chk13 = tk.Checkbutton(place, text='3', var=ckp13) 
	chk13.place(x = 140, y = 180)
	chk14 = tk.Checkbutton(place, text='4', var=ckp14) 
	chk14.place(x = 170, y = 180)
	chk15 = tk.Checkbutton(place, text='5', var=ckp15) 
	chk15.place(x = 200, y = 180)
	chk16 = tk.Checkbutton(place, text='6', var=ckp16) 
	chk16.place(x = 230, y = 180)

	# Enunciado 1.B)questao questao
	pegt1b = tk.Label (place, anchor='w',text= "B) Os conteúdos abordados nas disciplinas do curso favoreceram sua\n atuação em estágios ou em atividades de iniciação profissional. ")
	pegt1b.place(x = 50, y = 240, width=395, height=35 )

	#bloco variaveis da resposta 1.B
	ckp20 = tk.IntVar() 
	ckp20.set(0)
	ckp21 = tk.IntVar() 
	ckp21.set(1)
	ckp22 = tk.IntVar() 
	ckp22.set(2)
	ckp23 = tk.IntVar() 
	ckp23.set(3)
	ckp24 = tk.IntVar() 
	ckp24.set(4)
	ckp25 = tk.IntVar() 
	ckp25.set(5)
	ckp26 = tk.IntVar() 
	ckp26.set(6)

	#checkbox resposta, questao 1.B
	chk20 = tk.Checkbutton(place, text='0', var=ckp20) 
	chk20.place(x = 50, y = 280)
	chk21 = tk.Checkbutton(place, text='1', var=ckp21) 
	chk21.place(x = 80, y = 280)
	chk22 = tk.Checkbutton(place, text='2', var=ckp22) 
	chk22.place(x = 110, y = 280)
	chk23 = tk.Checkbutton(place, text='3', var=ckp23) 
	chk23.place(x = 140, y = 280)
	chk24 = tk.Checkbutton(place, text='4', var=ckp24) 
	chk24.place(x = 170, y = 280)
	chk25 = tk.Checkbutton(place, text='5', var=ckp25) 
	chk25.place(x = 200, y = 280)
	chk26 = tk.Checkbutton(place, text='6', var=ckp26) 
	chk26.place(x = 230, y = 280)


	# Enunciado 1.C)questao questao
	pegt1c = tk.Label (place, anchor='w',text= "C) Os planos de ensino apresentados pelos professores contribuíram para\n o desenvolvimento das atividades acadêmicas e para seus estudos.  ")
	pegt1c.place(x = 50, y = 340, width=395, height=35 )

	#bloco variaveis da resposta 1.C 
	ckp30 = tk.IntVar() 
	ckp30.set(0)
	ckp31 = tk.IntVar() 
	ckp31.set(1)
	ckp32 = tk.IntVar() 
	ckp32.set(2)
	ckp33 = tk.IntVar() 
	ckp33.set(3)
	ckp34 = tk.IntVar() 
	ckp34.set(4)
	ckp35 = tk.IntVar() 
	ckp35.set(5)
	ckp36 = tk.IntVar() 
	ckp36.set(6)

	#checkbox resposta, questao 1.C
	chk30 = tk.Checkbutton(place, text='0', var=ckp30) 
	chk30.place(x = 50, y = 380)
	chk31 = tk.Checkbutton(place, text='1', var=ckp31) 
	chk31.place(x = 80, y = 380)
	chk32 = tk.Checkbutton(place, text='2', var=ckp32) 
	chk32.place(x = 110, y = 380)
	chk33 = tk.Checkbutton(place, text='3', var=ckp33) 
	chk33.place(x = 140, y = 380)
	chk34 = tk.Checkbutton(place, text='4', var=ckp34) 
	chk34.place(x = 170, y = 380)
	chk35 = tk.Checkbutton(place, text='5', var=ckp35) 
	chk35.place(x = 200, y = 380)
	chk36 = tk.Checkbutton(place, text='6', var=ckp36) 
	chk36.place(x = 230, y = 380)


	# Enunciado 1.D)questao questao
	pegt1d = tk.Label (place,anchor='w', text= "D) As referências bibliográficas indicadas pelos professores nos planos\n de ensino contribuíram para seus estudos e aprendizagens. ")
	pegt1d.place(x = 50, y = 440, width=395, height=35 )

	#bloco variaveis da resposta 1.D
	ckp40 = tk.IntVar() 
	ckp40.set(0)
	ckp41 = tk.IntVar() 
	ckp41.set(1)
	ckp42 = tk.IntVar() 
	ckp42.set(2)
	ckp43 = tk.IntVar() 
	ckp43.set(3)
	ckp44 = tk.IntVar() 
	ckp44.set(4)
	ckp45 = tk.IntVar() 
	ckp45.set(5)
	ckp46 = tk.IntVar() 
	ckp46.set(6)

	#checkbox resposta, questao 1.D
	chk40 = tk.Checkbutton(place, text='0', var=ckp40) 
	chk40.place(x = 50, y = 480)
	chk41 = tk.Checkbutton(place, text='1', var=ckp41) 
	chk41.place(x = 80, y = 480)
	chk42 = tk.Checkbutton(place, text='2', var=ckp42) 
	chk42.place(x = 110, y = 480)
	chk43 = tk.Checkbutton(place, text='3', var=ckp43) 
	chk43.place(x = 140, y = 480)
	chk44 = tk.Checkbutton(place, text='4', var=ckp44) 
	chk44.place(x = 170, y = 480)
	chk45 = tk.Checkbutton(place, text='5', var=ckp45) 
	chk45.place(x = 200, y = 480)
	chk46 = tk.Checkbutton(place, text='6', var=ckp46) 
	chk46.place(x = 230, y = 480)


	# Enunciado 1.E)questao questao
	pegt1e = tk.Label (place, anchor='w', text= "E)As avaliações da aprendizagem realizadas durante o curso foram compatíveis\n com os conteúdos ou temas trabalhados pelos professores.")
	pegt1e.place(x = 50, y = 540, width=395, height=35 )

	#bloco variaveis da resposta 1.E
	ckp50 = tk.IntVar() 
	ckp50.set(0)
	ckp51 = tk.IntVar() 
	ckp51.set(1)
	ckp52 = tk.IntVar() 
	ckp52.set(2)
	ckp53 = tk.IntVar() 
	ckp53.set(3)
	ckp54 = tk.IntVar() 
	ckp54.set(4)
	ckp55 = tk.IntVar() 
	ckp55.set(5)
	ckp56 = tk.IntVar() 
	ckp56.set(6)

	#checkbox resposta, questao 1.E
	chk50 = tk.Checkbutton(place, text='0', var=ckp50) 
	chk50.place(x = 50, y = 580)
	chk51 = tk.Checkbutton(place, text='1', var=ckp51) 
	chk51.place(x = 80, y = 580)
	chk52 = tk.Checkbutton(place, text='2', var=ckp52) 
	chk52.place(x = 110, y = 580)
	chk53 = tk.Checkbutton(place, text='3', var=ckp53) 
	chk53.place(x = 140, y = 580)
	chk54 = tk.Checkbutton(place, text='4', var=ckp54) 
	chk54.place(x = 170, y = 580)
	chk55 = tk.Checkbutton(place, text='5', var=ckp55) 
	chk55.place(x = 200, y = 580)
	chk56 = tk.Checkbutton(place, text='6', var=ckp56) 
	chk56.place(x = 230, y = 580)


	# Enunciado 1.F)questao questao
	pegt1f = tk.Label (place, text= "F) A biblioteca dispôs das referências bibliográficas que os estudantes\n necessitaram. ", anchor='w')
	pegt1f.place(x = 480, y = 140, width=395, height=35 )

    #bloco variaveis da resposta 1.F
	ckp60 = tk.IntVar() 
	ckp60.set(0)
	ckp61 = tk.IntVar() 
	ckp61.set(1)
	ckp62 = tk.IntVar() 
	ckp62.set(2)
	ckp63 = tk.IntVar() 
	ckp63.set(3)
	ckp64 = tk.IntVar() 
	ckp64.set(4)
	ckp65 = tk.IntVar() 
	ckp65.set(5)
	ckp66 = tk.IntVar() 
	ckp66.set(6)

    #checkbox resposta, questao 1.F
	chk60 = tk.Checkbutton(place, text='0', var=ckp60) 
	chk60.place(x = 480, y = 180)
	chk61 = tk.Checkbutton(place, text='1', var=ckp61) 
	chk61.place(x = 510, y = 180)
	chk62 = tk.Checkbutton(place, text='2', var=ckp62) 
	chk62.place(x = 540, y = 180)
	chk63 = tk.Checkbutton(place, text='3', var=ckp63) 
	chk63.place(x = 570, y = 180)
	chk64 = tk.Checkbutton(place, text='4', var=ckp64) 
	chk64.place(x = 600, y = 180)
	chk65 = tk.Checkbutton(place, text='5', var=ckp65) 
	chk65.place(x = 630, y = 180)
	chk66 = tk.Checkbutton(place, text='6', var=ckp66) 
	chk66.place(x = 660, y = 180)

	# Enunciado 1.G)questao questao
	pegt1g = tk.Label (place, text= "G)  ", anchor='w')
	pegt1g.place(x = 480, y = 240, width=395, height=35 )

    #bloco variaveis da resposta 1.G
	ckp70 = tk.IntVar() 
	ckp70.set(0)
	ckp71 = tk.IntVar() 
	ckp71.set(1)
	ckp72 = tk.IntVar() 
	ckp72.set(2)
	ckp73 = tk.IntVar() 
	ckp73.set(3)
	ckp74 = tk.IntVar() 
	ckp74.set(4)
	ckp75 = tk.IntVar() 
	ckp75.set(5)
	ckp76 = tk.IntVar() 
	ckp76.set(6)

    #checkbox resposta, questao 1.G
	chk70 = tk.Checkbutton(place, text='0', var=ckp70) 
	chk70.place(x = 480, y = 280)
	chk71 = tk.Checkbutton(place, text='1', var=ckp71) 
	chk71.place(x = 510, y = 280)
	chk72 = tk.Checkbutton(place, text='2', var=ckp72) 
	chk72.place(x = 540, y = 280)
	chk73 = tk.Checkbutton(place, text='3', var=ckp73) 
	chk73.place(x = 570, y = 280)
	chk74 = tk.Checkbutton(place, text='4', var=ckp74) 
	chk74.place(x = 600, y = 280)
	chk75 = tk.Checkbutton(place, text='5', var=ckp75) 
	chk75.place(x = 630, y = 280)
	chk76 = tk.Checkbutton(place, text='6', var=ckp76) 
	chk76.place(x = 660, y = 280)


	# Enunciado 1.H)questao questao
	pegt1h = tk.Label (place, text= "H)  ", anchor='w')
	pegt1h.place(x = 480, y = 340, width=395, height=35 )

    #bloco variaveis da resposta 1.H
	ckp80 = tk.IntVar() 
	ckp80.set(0)
	ckp81 = tk.IntVar() 
	ckp81.set(1)
	ckp82 = tk.IntVar() 
	ckp82.set(2)
	ckp83 = tk.IntVar() 
	ckp83.set(3)
	ckp84 = tk.IntVar() 
	ckp84.set(4)
	ckp85 = tk.IntVar() 
	ckp85.set(5)
	ckp86 = tk.IntVar() 
	ckp86.set(6)

    #checkbox resposta, questao 1.H
	chk80 = tk.Checkbutton(place, text='0', var=ckp80) 
	chk80.place(x = 480, y = 380)
	chk81 = tk.Checkbutton(place, text='1', var=ckp81) 
	chk81.place(x = 510, y = 380)
	chk82 = tk.Checkbutton(place, text='2', var=ckp82) 
	chk82.place(x = 540, y = 380)
	chk83 = tk.Checkbutton(place, text='3', var=ckp83) 
	chk83.place(x = 570, y = 380)
	chk84 = tk.Checkbutton(place, text='4', var=ckp84) 
	chk84.place(x = 600, y = 380)
	chk85 = tk.Checkbutton(place, text='5', var=ckp85) 
	chk85.place(x = 630, y = 380)
	chk86 = tk.Checkbutton(place, text='6', var=ckp86) 
	chk86.place(x = 660, y = 380)


	# Enunciado 1.I)questao questao
	pegt1i = tk.Label (place, text= "I)  ", anchor='w')
	pegt1i.place(x = 480, y = 440, width=395, height=35 )

    #bloco variaveis da resposta 1.I
	ckp90 = tk.IntVar() 
	ckp90.set(0)
	ckp91 = tk.IntVar() 
	ckp91.set(1)
	ckp92 = tk.IntVar() 
	ckp92.set(2)
	ckp93 = tk.IntVar() 
	ckp93.set(3)
	ckp94 = tk.IntVar() 
	ckp94.set(4)
	ckp95 = tk.IntVar() 
	ckp95.set(5)
	ckp96 = tk.IntVar() 
	ckp96.set(6)

    #checkbox resposta, questao 1.I
	chk90 = tk.Checkbutton(place, text='0', var=ckp90) 
	chk90.place(x = 480, y = 480)
	chk91 = tk.Checkbutton(place, text='1', var=ckp91) 
	chk91.place(x = 510, y = 480)
	chk92 = tk.Checkbutton(place, text='2', var=ckp92) 
	chk92.place(x = 540, y = 480)
	chk93 = tk.Checkbutton(place, text='3', var=ckp93) 
	chk93.place(x = 570, y = 480)
	chk94 = tk.Checkbutton(place, text='4', var=ckp94) 
	chk94.place(x = 600, y = 480)
	chk95 = tk.Checkbutton(place, text='5', var=ckp95) 
	chk95.place(x = 630, y = 480)
	chk96 = tk.Checkbutton(place, text='6', var=ckp96) 
	chk96.place(x = 660, y = 480)


	# Enunciado 1.J)questao questao
	pegt1j = tk.Label (place, text= "J)  ", anchor='w')
	pegt1j.place(x = 480, y = 540, width=395, height=35 )

    #bloco variaveis da resposta 1.J
	ckp100 = tk.IntVar() 
	ckp100.set(0)
	ckp101 = tk.IntVar() 
	ckp101.set(1)
	ckp102 = tk.IntVar() 
	ckp102.set(2)
	ckp103 = tk.IntVar() 
	ckp103.set(3)
	ckp104 = tk.IntVar() 
	ckp104.set(4)
	ckp105 = tk.IntVar() 
	ckp105.set(5)
	ckp106 = tk.IntVar() 
	ckp106.set(6)

    #checkbox resposta, questao 1.J
	chk100 = tk.Checkbutton(place, text='0', var=ckp100) 
	chk100.place(x = 480, y = 580)
	chk101 = tk.Checkbutton(place, text='1', var=ckp101) 
	chk101.place(x = 510, y = 580)
	chk102 = tk.Checkbutton(place, text='2', var=ckp102) 
	chk102.place(x = 540, y = 580)
	chk103 = tk.Checkbutton(place, text='3', var=ckp103) 
	chk103.place(x = 570, y = 580)
	chk104 = tk.Checkbutton(place, text='4', var=ckp104) 
	chk104.place(x = 600, y = 580)
	chk105 = tk.Checkbutton(place, text='5', var=ckp105) 
	chk105.place(x = 630, y = 580)
	chk106 = tk.Checkbutton(place, text='6', var=ckp106) 
	chk106.place(x = 660, y = 580)



	#cabeçalho segundo modulo de questoes
	titulo3 = tk.Label (place, text= " 02) Acadêmico  - Metodologia de Ensino ")
	titulo3.place(x = 910, y = 100)
	titulo3.config(relief="ridge", font="Arial 12 bold", border=3, background="gray")

	# Enunciado 2.A)questao questao
	pegt2a = tk.Label (place, anchor='w',text= "A) As metodologias de ensino utilizadas no curso desafiaram você a aprofundar\n conhecimentos e desenvolver competências reflexivas e críticas. ")
	pegt2a.place(x = 910, y = 140, width=400, height=35 )

	#bloco variaveis da resposta 2.A
	ckp220 = tk.IntVar() 
	ckp220.set(0)
	ckp221 = tk.IntVar() 
	ckp221.set(1)
	ckp222 = tk.IntVar() 
	ckp222.set(2)
	ckp223 = tk.IntVar() 
	ckp223.set(3)
	ckp224 = tk.IntVar() 
	ckp224.set(4)
	ckp225 = tk.IntVar() 
	ckp225.set(5)
	ckp226 = tk.IntVar() 
	ckp226.set(6)

    #checkbox resposta, questao 2.A
	chk220 = tk.Checkbutton(place, text='0', var=ckp220) 
	chk220.place(x = 910, y = 180)
	chk221 = tk.Checkbutton(place, text='1', var=ckp221) 
	chk221.place(x = 940, y = 180)
	chk222 = tk.Checkbutton(place, text='2', var=ckp222) 
	chk222.place(x = 970, y = 180)
	chk223 = tk.Checkbutton(place, text='3', var=ckp223) 
	chk223.place(x = 1000, y = 180)
	chk224 = tk.Checkbutton(place, text='4', var=ckp224) 
	chk224.place(x = 1030, y = 180)
	chk225 = tk.Checkbutton(place, text='5', var=ckp225) 
	chk225.place(x = 1060, y = 180)
	chk226 = tk.Checkbutton(place, text='6', var=ckp226) 
	chk226.place(x = 1090, y = 180)

def perguntas2():
	place = tk.Tk()
	place.title("login")
	place.geometry("1400x660")
	place.configure(background="#999")

	#fundo da pagina
	fundo01 = tk.Label(place, padx=5, pady=5,background="gray")
	fundo01.place(x= 30, y = 80)
	fundo01.config(border=6, height = 37, width = 185 )

	#botoes da pag
	ent1 = tk.Button(place, text = "Proximo", command = perguntas3)
	ent1.place(x = 1280, y = 620)
	#ent1.configure( relief="ridge", border=6, font="10 bold", height = 1, width = 5)

	ent2 = tk.Button(place, text = "Enviar", command=place.after)
	ent2.place(x = 1190, y = 620)
	#ent2.configure( relief="ridge", border=6, font="10 bold", height = 1, width = 5)

	ent3 = tk.Button(place, text = "Anterior", command=perguntas)
	ent3.place(x = 50, y = 620)
	#ent3.configure( relief="ridge", border=6, font="10 bold", height = 1, width = 5)

	botaos = tk.Button(place,text = "sair",command=place.quit)
	botaos.place( x = 1330, y= 2)
	

	#Logo /link site
	logo = tk.Button (place, text="Folha CPA", foreground="white", command=lambda: webbrowser.open('https://mail.google.com/mail/u/0/#inbox'))
	logo.place(x = 620, y = 10)		
	logo.configure(relief="ridge", font="Arial 20 bold", border=4, background="gray")

	#infomar pagina
	infpg2 = tk.Label (place, text= " Pagina 2 ")
	infpg2.place(x = 20, y = 20)
	infpg2.config(relief="ridge", font="Arial 8 ", background="#999")

	#cabeçalho primeiro modulo de questoes
	titulo3 = tk.Label (place, text= " 3)Acadêmico – ")
	titulo3.place(x = 50, y = 100)
	titulo3.config(relief="ridge", font="Arial 12 bold", border=3, background="gray")

	# Enunciado 1)questao questao
	pegt1 = tk.Label (place, text= "A) ", anchor='w')
	pegt1.place(x = 50, y = 140, width=395, height=35,)

	#bloco variaveis da resposta 1.A
	ckp10 = tk.IntVar() 
	ckp10.set(0)
	ckp11 = tk.IntVar() 
	ckp11.set(1)
	ckp12 = tk.IntVar() 
	ckp12.set(2)
	ckp13 = tk.IntVar() 
	ckp13.set(3)
	ckp14 = tk.IntVar() 
	ckp14.set(4)
	ckp15 = tk.IntVar() 
	ckp15.set(5)
	ckp16 = tk.IntVar() 
	ckp16.set(6)
	ckp17 = tk.IntVar() 
	ckp17.set(7)
	ckp18 = tk.IntVar() 
	ckp18.set(8)
	ckp19 = tk.IntVar() 
	ckp19.set(9)
	ckp100 = tk.IntVar() 
	ckp100.set(10)

    #checkbox resposta, questao 1.A
	chk10 = tk.Checkbutton(place, text='0', var=ckp10) 
	chk10.place(x = 50, y = 180)
	chk11 = tk.Checkbutton(place, text='1', var=ckp11) 
	chk11.place(x = 80, y = 180)
	chk12 = tk.Checkbutton(place, text='2', var=ckp12) 
	chk12.place(x = 110, y = 180)
	chk13 = tk.Checkbutton(place, text='3', var=ckp13) 
	chk13.place(x = 140, y = 180)
	chk14 = tk.Checkbutton(place, text='4', var=ckp14) 
	chk14.place(x = 170, y = 180)
	chk15 = tk.Checkbutton(place, text='5', var=ckp15) 
	chk15.place(x = 200, y = 180)
	chk16 = tk.Checkbutton(place, text='6', var=ckp16) 
	chk16.place(x = 230, y = 180)
	chk17 = tk.Checkbutton(place, text='7', var=ckp17) 
	chk17.place(x = 260, y = 180)
	chk18 = tk.Checkbutton(place, text='8', var=ckp18) 
	chk18.place(x = 290, y = 180)
	chk19 = tk.Checkbutton(place, text='9', var=ckp19) 
	chk19.place(x = 320, y = 180)
	chk100 = tk.Checkbutton(place, text='10', var=ckp100) 
	chk100.place(x = 350, y = 180)

	# Enunciado 1.B)questao questao
	pegt2 = tk.Label (place, anchor='w',text= "B) ")
	pegt2.place(x = 50, y = 240, width=395, height=35 )

	#bloco variaveis da resposta 1.B
	ckp20 = tk.IntVar() 
	ckp20.set(0)
	ckp21 = tk.IntVar() 
	ckp21.set(1)
	ckp22 = tk.IntVar() 
	ckp22.set(2)
	ckp23 = tk.IntVar() 
	ckp23.set(3)
	ckp24 = tk.IntVar() 
	ckp24.set(4)
	ckp25 = tk.IntVar() 
	ckp25.set(5)
	ckp26 = tk.IntVar() 
	ckp26.set(6)

	#checkbox resposta, questao 1.B
	chk20 = tk.Checkbutton(place, text='0', var=ckp20) 
	chk20.place(x = 50, y = 280)
	chk21 = tk.Checkbutton(place, text='1', var=ckp21) 
	chk21.place(x = 80, y = 280)
	chk22 = tk.Checkbutton(place, text='2', var=ckp22) 
	chk22.place(x = 110, y = 280)
	chk23 = tk.Checkbutton(place, text='3', var=ckp23) 
	chk23.place(x = 140, y = 280)
	chk24 = tk.Checkbutton(place, text='4', var=ckp24) 
	chk24.place(x = 170, y = 280)
	chk25 = tk.Checkbutton(place, text='5', var=ckp25) 
	chk25.place(x = 200, y = 280)
	chk26 = tk.Checkbutton(place, text='6', var=ckp26) 
	chk26.place(x = 230, y = 280)


	# Enunciado 1.C)questao questao
	pegt3 = tk.Label (place, anchor='w',text= "C)  ")
	pegt3.place(x = 50, y = 340, width=395, height=35 )

	#bloco variaveis da resposta 1.C 
	ckp30 = tk.IntVar() 
	ckp30.set(0)
	ckp31 = tk.IntVar() 
	ckp31.set(1)
	ckp32 = tk.IntVar() 
	ckp32.set(2)
	ckp33 = tk.IntVar() 
	ckp33.set(3)
	ckp34 = tk.IntVar() 
	ckp34.set(4)
	ckp35 = tk.IntVar() 
	ckp35.set(5)
	ckp36 = tk.IntVar() 
	ckp36.set(6)

	#checkbox resposta, questao 1.C
	chk30 = tk.Checkbutton(place, text='0', var=ckp30) 
	chk30.place(x = 50, y = 380)
	chk31 = tk.Checkbutton(place, text='1', var=ckp31) 
	chk31.place(x = 80, y = 380)
	chk32 = tk.Checkbutton(place, text='2', var=ckp32) 
	chk32.place(x = 110, y = 380)
	chk33 = tk.Checkbutton(place, text='3', var=ckp33) 
	chk33.place(x = 140, y = 380)
	chk34 = tk.Checkbutton(place, text='4', var=ckp34) 
	chk34.place(x = 170, y = 380)
	chk35 = tk.Checkbutton(place, text='5', var=ckp35) 
	chk35.place(x = 200, y = 380)
	chk36 = tk.Checkbutton(place, text='6', var=ckp36) 
	chk36.place(x = 230, y = 380)


	# Enunciado 1.D)questao questao
	pegt4 = tk.Label (place,anchor='w', text= "D)  ")
	pegt4.place(x = 50, y = 440, width=395, height=35 )

	#bloco variaveis da resposta 1.D
	ckp40 = tk.IntVar() 
	ckp40.set(0)
	ckp41 = tk.IntVar() 
	ckp41.set(1)
	ckp42 = tk.IntVar() 
	ckp42.set(2)
	ckp43 = tk.IntVar() 
	ckp43.set(3)
	ckp44 = tk.IntVar() 
	ckp44.set(4)
	ckp45 = tk.IntVar() 
	ckp45.set(5)
	ckp46 = tk.IntVar() 
	ckp46.set(6)

	#checkbox resposta, questao 1.D
	chk40 = tk.Checkbutton(place, text='0', var=ckp40) 
	chk40.place(x = 50, y = 480)
	chk41 = tk.Checkbutton(place, text='1', var=ckp41) 
	chk41.place(x = 80, y = 480)
	chk42 = tk.Checkbutton(place, text='2', var=ckp42) 
	chk42.place(x = 110, y = 480)
	chk43 = tk.Checkbutton(place, text='3', var=ckp43) 
	chk43.place(x = 140, y = 480)
	chk44 = tk.Checkbutton(place, text='4', var=ckp44) 
	chk44.place(x = 170, y = 480)
	chk45 = tk.Checkbutton(place, text='5', var=ckp45) 
	chk45.place(x = 200, y = 480)
	chk46 = tk.Checkbutton(place, text='6', var=ckp46) 
	chk46.place(x = 230, y = 480)


	# Enunciado 1.E)questao questao
	pegt5 = tk.Label (place, anchor='w', text= "E)")
	pegt5.place(x = 50, y = 540, width=395, height=35 )

	#bloco variaveis da resposta 1.E
	ckp50 = tk.IntVar() 
	ckp50.set(0)
	ckp51 = tk.IntVar() 
	ckp51.set(1)
	ckp52 = tk.IntVar() 
	ckp52.set(2)
	ckp53 = tk.IntVar() 
	ckp53.set(3)
	ckp54 = tk.IntVar() 
	ckp54.set(4)
	ckp55 = tk.IntVar() 
	ckp55.set(5)
	ckp56 = tk.IntVar() 
	ckp56.set(6)

	#checkbox resposta, questao 1.E
	chk50 = tk.Checkbutton(place, text='0', var=ckp50) 
	chk50.place(x = 50, y = 580)
	chk51 = tk.Checkbutton(place, text='1', var=ckp51) 
	chk51.place(x = 80, y = 580)
	chk52 = tk.Checkbutton(place, text='2', var=ckp52) 
	chk52.place(x = 110, y = 580)
	chk53 = tk.Checkbutton(place, text='3', var=ckp53) 
	chk53.place(x = 140, y = 580)
	chk54 = tk.Checkbutton(place, text='4', var=ckp54) 
	chk54.place(x = 170, y = 580)
	chk55 = tk.Checkbutton(place, text='5', var=ckp55) 
	chk55.place(x = 200, y = 580)
	chk56 = tk.Checkbutton(place, text='6', var=ckp56) 
	chk56.place(x = 230, y = 580)


	# Enunciado 1.F)questao questao
	pegt6 = tk.Label (place, text= "F)  ", anchor='w')
	pegt6.place(x = 480, y = 140, width=395, height=35 )

    #bloco variaveis da resposta 1.F
	ckp60 = tk.IntVar() 
	ckp60.set(0)
	ckp61 = tk.IntVar() 
	ckp61.set(1)
	ckp62 = tk.IntVar() 
	ckp62.set(2)
	ckp63 = tk.IntVar() 
	ckp63.set(3)
	ckp64 = tk.IntVar() 
	ckp64.set(4)
	ckp65 = tk.IntVar() 
	ckp65.set(5)
	ckp66 = tk.IntVar() 
	ckp66.set(6)

    #checkbox resposta, questao 1.F
	chk60 = tk.Checkbutton(place, text='0', var=ckp60) 
	chk60.place(x = 480, y = 180)
	chk61 = tk.Checkbutton(place, text='1', var=ckp61) 
	chk61.place(x = 510, y = 180)
	chk62 = tk.Checkbutton(place, text='2', var=ckp62) 
	chk62.place(x = 540, y = 180)
	chk63 = tk.Checkbutton(place, text='3', var=ckp63) 
	chk63.place(x = 570, y = 180)
	chk64 = tk.Checkbutton(place, text='4', var=ckp64) 
	chk64.place(x = 600, y = 180)
	chk65 = tk.Checkbutton(place, text='5', var=ckp65) 
	chk65.place(x = 630, y = 180)
	chk66 = tk.Checkbutton(place, text='6', var=ckp66) 
	chk66.place(x = 660, y = 180)

	# Enunciado 1.G)questao questao
	pegt7 = tk.Label (place, text= "G)  ", anchor='w')
	pegt7.place(x = 480, y = 240, width=395, height=35 )

    #bloco variaveis da resposta 1.G
	ckp70 = tk.IntVar() 
	ckp70.set(0)
	ckp71 = tk.IntVar() 
	ckp71.set(1)
	ckp72 = tk.IntVar() 
	ckp72.set(2)
	ckp73 = tk.IntVar() 
	ckp73.set(3)
	ckp74 = tk.IntVar() 
	ckp74.set(4)
	ckp75 = tk.IntVar() 
	ckp75.set(5)
	ckp76 = tk.IntVar() 
	ckp76.set(6)

    #checkbox resposta, questao 1.G
	chk70 = tk.Checkbutton(place, text='0', var=ckp70) 
	chk70.place(x = 480, y = 280)
	chk71 = tk.Checkbutton(place, text='1', var=ckp71) 
	chk71.place(x = 510, y = 280)
	chk72 = tk.Checkbutton(place, text='2', var=ckp72) 
	chk72.place(x = 540, y = 280)
	chk73 = tk.Checkbutton(place, text='3', var=ckp73) 
	chk73.place(x = 570, y = 280)
	chk74 = tk.Checkbutton(place, text='4', var=ckp74) 
	chk74.place(x = 600, y = 280)
	chk75 = tk.Checkbutton(place, text='5', var=ckp75) 
	chk75.place(x = 630, y = 280)
	chk76 = tk.Checkbutton(place, text='6', var=ckp76) 
	chk76.place(x = 660, y = 280)


	# Enunciado 1.H)questao questao
	pegt8 = tk.Label (place, text= "H)  ", anchor='w')
	pegt8.place(x = 480, y = 340, width=395, height=35 )

    #bloco variaveis da resposta 1.H
	ckp80 = tk.IntVar() 
	ckp80.set(0)
	ckp81 = tk.IntVar() 
	ckp81.set(1)
	ckp82 = tk.IntVar() 
	ckp82.set(2)
	ckp83 = tk.IntVar() 
	ckp83.set(3)
	ckp84 = tk.IntVar() 
	ckp84.set(4)
	ckp85 = tk.IntVar() 
	ckp85.set(5)
	ckp86 = tk.IntVar() 
	ckp86.set(6)

    #checkbox resposta, questao 1.H
	chk80 = tk.Checkbutton(place, text='0', var=ckp80) 
	chk80.place(x = 480, y = 380)
	chk81 = tk.Checkbutton(place, text='1', var=ckp81) 
	chk81.place(x = 510, y = 380)
	chk82 = tk.Checkbutton(place, text='2', var=ckp82) 
	chk82.place(x = 540, y = 380)
	chk83 = tk.Checkbutton(place, text='3', var=ckp83) 
	chk83.place(x = 570, y = 380)
	chk84 = tk.Checkbutton(place, text='4', var=ckp84) 
	chk84.place(x = 600, y = 380)
	chk85 = tk.Checkbutton(place, text='5', var=ckp85) 
	chk85.place(x = 630, y = 380)
	chk86 = tk.Checkbutton(place, text='6', var=ckp86) 
	chk86.place(x = 660, y = 380)


	# Enunciado 1.I)questao questao
	pegt7 = tk.Label (place, text= "I)  ", anchor='w')
	pegt7.place(x = 480, y = 440, width=395, height=35 )

    #bloco variaveis da resposta 1.I
	ckp90 = tk.IntVar() 
	ckp90.set(0)
	ckp91 = tk.IntVar() 
	ckp91.set(1)
	ckp92 = tk.IntVar() 
	ckp92.set(2)
	ckp93 = tk.IntVar() 
	ckp93.set(3)
	ckp94 = tk.IntVar() 
	ckp94.set(4)
	ckp95 = tk.IntVar() 
	ckp95.set(5)
	ckp96 = tk.IntVar() 
	ckp96.set(6)

    #checkbox resposta, questao 1.I
	chk90 = tk.Checkbutton(place, text='0', var=ckp90) 
	chk90.place(x = 480, y = 480)
	chk91 = tk.Checkbutton(place, text='1', var=ckp91) 
	chk91.place(x = 510, y = 480)
	chk92 = tk.Checkbutton(place, text='2', var=ckp92) 
	chk92.place(x = 540, y = 480)
	chk93 = tk.Checkbutton(place, text='3', var=ckp93) 
	chk93.place(x = 570, y = 480)
	chk94 = tk.Checkbutton(place, text='4', var=ckp94) 
	chk94.place(x = 600, y = 480)
	chk95 = tk.Checkbutton(place, text='5', var=ckp95) 
	chk95.place(x = 630, y = 480)
	chk96 = tk.Checkbutton(place, text='6', var=ckp96) 
	chk96.place(x = 660, y = 480)


	# Enunciado 1.J)questao questao
	pegt7 = tk.Label (place, text= "J)  ", anchor='w')
	pegt7.place(x = 480, y = 540, width=395, height=35 )

    #bloco variaveis da resposta 1.J
	ckp100 = tk.IntVar() 
	ckp100.set(0)
	ckp101 = tk.IntVar() 
	ckp101.set(1)
	ckp102 = tk.IntVar() 
	ckp102.set(2)
	ckp103 = tk.IntVar() 
	ckp103.set(3)
	ckp104 = tk.IntVar() 
	ckp104.set(4)
	ckp105 = tk.IntVar() 
	ckp105.set(5)
	ckp106 = tk.IntVar() 
	ckp106.set(6)

    #checkbox resposta, questao 1.J
	chk100 = tk.Checkbutton(place, text='0', var=ckp100) 
	chk100.place(x = 480, y = 580)
	chk101 = tk.Checkbutton(place, text='1', var=ckp101) 
	chk101.place(x = 510, y = 580)
	chk102 = tk.Checkbutton(place, text='2', var=ckp102) 
	chk102.place(x = 540, y = 580)
	chk103 = tk.Checkbutton(place, text='3', var=ckp103) 
	chk103.place(x = 570, y = 580)
	chk104 = tk.Checkbutton(place, text='4', var=ckp104) 
	chk104.place(x = 600, y = 580)
	chk105 = tk.Checkbutton(place, text='5', var=ckp105) 
	chk105.place(x = 630, y = 580)
	chk106 = tk.Checkbutton(place, text='6', var=ckp106) 
	chk106.place(x = 660, y = 580)



	#cabeçalho segundo modulo de questoes
	titulo4 = tk.Label (place, text= " 04) Acadêmico   ")
	titulo4.place(x = 910, y = 100)
	titulo4.config(relief="ridge", font="Arial 12 bold", border=3, background="gray")

	# Enunciado 2.A)questao questao
	pegt4 = tk.Label (place, anchor='w',text= "A)  ")
	pegt4.place(x = 910, y = 140, width=400, height=35 )

	#bloco variaveis da resposta 2.A
	ckp220 = tk.IntVar() 
	ckp220.set(0)
	ckp221 = tk.IntVar() 
	ckp221.set(1)
	ckp222 = tk.IntVar() 
	ckp222.set(2)
	ckp223 = tk.IntVar() 
	ckp223.set(3)
	ckp224 = tk.IntVar() 
	ckp224.set(4)
	ckp225 = tk.IntVar() 
	ckp225.set(5)
	ckp226 = tk.IntVar() 
	ckp226.set(6)

    #checkbox resposta, questao 2.A
	chk220 = tk.Checkbutton(place, text='0', var=ckp220) 
	chk220.place(x = 910, y = 180)
	chk221 = tk.Checkbutton(place, text='1', var=ckp221) 
	chk221.place(x = 940, y = 180)
	chk222 = tk.Checkbutton(place, text='2', var=ckp222) 
	chk222.place(x = 970, y = 180)
	chk223 = tk.Checkbutton(place, text='3', var=ckp223) 
	chk223.place(x = 1000, y = 180)
	chk224 = tk.Checkbutton(place, text='4', var=ckp224) 
	chk224.place(x = 1030, y = 180)
	chk225 = tk.Checkbutton(place, text='5', var=ckp225) 
	chk225.place(x = 1060, y = 180)
	chk226 = tk.Checkbutton(place, text='6', var=ckp226) 
	chk226.place(x = 1090, y = 180)


	# Enunciado 2.B)questao questao
	pegt2 = tk.Label (place, anchor='w',text= "B)  ")
	pegt2.place(x = 910, y = 240, width=400, height=35 )

	#bloco variaveis da resposta 2.B
	ckp230 = tk.IntVar() 
	ckp230.set(0)
	ckp231 = tk.IntVar() 
	ckp231.set(1)
	ckp232 = tk.IntVar() 
	ckp232.set(2)
	ckp233 = tk.IntVar() 
	ckp233.set(3)
	ckp234 = tk.IntVar() 
	ckp234.set(4)
	ckp235 = tk.IntVar() 
	ckp235.set(5)
	ckp236 = tk.IntVar() 
	ckp236.set(6)

    #checkbox resposta, questao 2.B
	chk230 = tk.Checkbutton(place, text='0', var=ckp230) 
	chk230.place(x = 910, y = 280)
	chk231 = tk.Checkbutton(place, text='1', var=ckp231) 
	chk231.place(x = 940, y = 280)
	chk232 = tk.Checkbutton(place, text='2', var=ckp232) 
	chk232.place(x = 970, y = 280)
	chk233 = tk.Checkbutton(place, text='3', var=ckp233) 
	chk233.place(x = 1000, y = 280)
	chk234 = tk.Checkbutton(place, text='4', var=ckp234) 
	chk234.place(x = 1030, y = 280)
	chk235 = tk.Checkbutton(place, text='5', var=ckp235) 
	chk235.place(x = 1060, y = 280)
	chk236 = tk.Checkbutton(place, text='6', var=ckp236) 
	chk236.place(x = 1090, y = 280)

	
	# Enunciado 2.C)questao questao
	pegt4 = tk.Label (place, anchor='w',text= "C)  ")
	pegt4.place(x = 910, y = 340, width=400, height=35 )

	#bloco variaveis da resposta 2.C
	ckp240 = tk.IntVar() 
	ckp240.set(0)
	ckp241 = tk.IntVar() 
	ckp241.set(1)
	ckp242 = tk.IntVar() 
	ckp242.set(2)
	ckp243 = tk.IntVar() 
	ckp243.set(3)
	ckp244 = tk.IntVar() 
	ckp244.set(4)
	ckp245 = tk.IntVar() 
	ckp245.set(5)
	ckp246 = tk.IntVar() 
	ckp246.set(6)

    #checkbox resposta, questao 2.C
	chk240 = tk.Checkbutton(place, text='0', var=ckp240) 
	chk240.place(x = 910, y = 380)
	chk241 = tk.Checkbutton(place, text='1', var=ckp241) 
	chk241.place(x = 940, y = 380)
	chk242 = tk.Checkbutton(place, text='2', var=ckp242) 
	chk242.place(x = 970, y = 380)
	chk243 = tk.Checkbutton(place, text='3', var=ckp243) 
	chk243.place(x = 1000, y = 380)
	chk244 = tk.Checkbutton(place, text='4', var=ckp244) 
	chk244.place(x = 1030, y = 380)
	chk245 = tk.Checkbutton(place, text='5', var=ckp245) 
	chk245.place(x = 1060, y = 380)
	chk246 = tk.Checkbutton(place, text='6', var=ckp246) 
	chk246.place(x = 1090, y = 380)


	# Enunciado 2.D)questao questao
	pegt4 = tk.Label (place, anchor='w',text= "D)  ")
	pegt4.place(x = 910, y = 440, width=400, height=35 )

	#bloco variaveis da resposta 2.D
	ckp250 = tk.IntVar() 
	ckp250.set(0)
	ckp251 = tk.IntVar() 
	ckp251.set(1)
	ckp252 = tk.IntVar() 
	ckp252.set(2)
	ckp253 = tk.IntVar() 
	ckp253.set(3)
	ckp254 = tk.IntVar() 
	ckp254.set(4)
	ckp255 = tk.IntVar() 
	ckp255.set(5)
	ckp256 = tk.IntVar() 
	ckp256.set(6)

    #checkbox resposta, questao 2.D
	chk250 = tk.Checkbutton(place, text='0', var=ckp250) 
	chk250.place(x = 910, y = 480)
	chk251 = tk.Checkbutton(place, text='1', var=ckp251) 
	chk251.place(x = 940, y = 480)
	chk252 = tk.Checkbutton(place, text='2', var=ckp252) 
	chk252.place(x = 970, y = 480)
	chk253 = tk.Checkbutton(place, text='3', var=ckp253) 
	chk253.place(x = 1000, y = 480)
	chk254 = tk.Checkbutton(place, text='4', var=ckp254) 
	chk254.place(x = 1030, y = 480)
	chk255 = tk.Checkbutton(place, text='5', var=ckp255) 
	chk255.place(x = 1060, y = 480)
	chk256 = tk.Checkbutton(place, text='6', var=ckp256) 
	chk256.place(x = 1090, y = 480)

def perguntas3():

	place = tk.Tk()
	place.title("login")
	place.geometry("1400x660")
	place.configure(background="#999")

	#fundo da pagina
	fundo01 = tk.Label(place, padx=5, pady=5,background="gray")
	fundo01.place(x= 30, y = 80)
	fundo01.config(border=6, height = 37, width = 185 )

	#botoes da pag
	ent1 = tk.Button(place, text = "Proximo", command = perguntas4)
	ent1.place(x = 1280, y = 620)
	#ent1.configure( relief="ridge", border=6, font="10 bold", height = 1, width = 5)

	ent2 = tk.Button(place, text = "Enviar", command=perguntas2)
	ent2.place(x = 1190, y = 620)
	#ent2.configure( relief="ridge", border=6, font="10 bold", height = 1, width = 5)

	ent3 = tk.Button(place, text = "Anterior", command=place.event_info)
	ent3.place(x = 50, y = 620)
	#ent3.configure( relief="ridge", border=6, font="10 bold", height = 1, width = 5)

	botaos = tk.Button(place,text = "sair",command=place.quit)
	botaos.place( x = 1330, y= 2)
	

	#Logo /link site
	logo = tk.Button (place, text="Folha CPA", foreground="white", command=lambda: webbrowser.open('https://mail.google.com/mail/u/0/#inbox'))
	logo.place(x = 620, y = 10)		
	logo.configure(relief="ridge", font="Arial 20 bold", border=4, background="gray")

	#infomar pagina
	infpg3 = tk.Label (place, text= " Pagina 3 ")
	infpg3.place(x = 20, y = 20)
	infpg3.config(relief="ridge", font="Arial 8 ", background="#999")

	#cabeçalho primeiro modulo de questoes
	titulo2 = tk.Label (place, text= " 3)Acadêmico – ")
	titulo2.place(x = 50, y = 100)
	titulo2.config(relief="ridge", font="Arial 12 bold", border=3, background="gray")

	# Enunciado 1)questao questao
	pegt1 = tk.Label (place, text= "A) ", anchor='w')
	pegt1.place(x = 50, y = 140, width=395, height=35,)

	#bloco variaveis da resposta 1.A
	ckp10 = tk.IntVar() 
	ckp10.set(0)
	ckp11 = tk.IntVar() 
	ckp11.set(1)
	ckp12 = tk.IntVar() 
	ckp12.set(2)
	ckp13 = tk.IntVar() 
	ckp13.set(3)
	ckp14 = tk.IntVar() 
	ckp14.set(4)
	ckp15 = tk.IntVar() 
	ckp15.set(5)
	ckp16 = tk.IntVar() 
	ckp16.set(6)

    #checkbox resposta, questao 1.A
	chk10 = tk.Checkbutton(place, text='0', var=ckp10) 
	chk10.place(x = 50, y = 180)
	chk11 = tk.Checkbutton(place, text='1', var=ckp11) 
	chk11.place(x = 80, y = 180)
	chk12 = tk.Checkbutton(place, text='2', var=ckp12) 
	chk12.place(x = 110, y = 180)
	chk13 = tk.Checkbutton(place, text='3', var=ckp13) 
	chk13.place(x = 140, y = 180)
	chk14 = tk.Checkbutton(place, text='4', var=ckp14) 
	chk14.place(x = 170, y = 180)
	chk15 = tk.Checkbutton(place, text='5', var=ckp15) 
	chk15.place(x = 200, y = 180)
	chk16 = tk.Checkbutton(place, text='6', var=ckp16) 
	chk16.place(x = 230, y = 180)

	# Enunciado 1.B)questao questao
	pegt2 = tk.Label (place, anchor='w',text= "B) ")
	pegt2.place(x = 50, y = 240, width=395, height=35 )

	#bloco variaveis da resposta 1.B
	ckp20 = tk.IntVar() 
	ckp20.set(0)
	ckp21 = tk.IntVar() 
	ckp21.set(1)
	ckp22 = tk.IntVar() 
	ckp22.set(2)
	ckp23 = tk.IntVar() 
	ckp23.set(3)
	ckp24 = tk.IntVar() 
	ckp24.set(4)
	ckp25 = tk.IntVar() 
	ckp25.set(5)
	ckp26 = tk.IntVar() 
	ckp26.set(6)

	#checkbox resposta, questao 1.B
	chk20 = tk.Checkbutton(place, text='0', var=ckp20) 
	chk20.place(x = 50, y = 280)
	chk21 = tk.Checkbutton(place, text='1', var=ckp21) 
	chk21.place(x = 80, y = 280)
	chk22 = tk.Checkbutton(place, text='2', var=ckp22) 
	chk22.place(x = 110, y = 280)
	chk23 = tk.Checkbutton(place, text='3', var=ckp23) 
	chk23.place(x = 140, y = 280)
	chk24 = tk.Checkbutton(place, text='4', var=ckp24) 
	chk24.place(x = 170, y = 280)
	chk25 = tk.Checkbutton(place, text='5', var=ckp25) 
	chk25.place(x = 200, y = 280)
	chk26 = tk.Checkbutton(place, text='6', var=ckp26) 
	chk26.place(x = 230, y = 280)


	# Enunciado 1.C)questao questao
	pegt3 = tk.Label (place, anchor='w',text= "C)  ")
	pegt3.place(x = 50, y = 340, width=395, height=35 )

	#bloco variaveis da resposta 1.C 
	ckp30 = tk.IntVar() 
	ckp30.set(0)
	ckp31 = tk.IntVar() 
	ckp31.set(1)
	ckp32 = tk.IntVar() 
	ckp32.set(2)
	ckp33 = tk.IntVar() 
	ckp33.set(3)
	ckp34 = tk.IntVar() 
	ckp34.set(4)
	ckp35 = tk.IntVar() 
	ckp35.set(5)
	ckp36 = tk.IntVar() 
	ckp36.set(6)

	#checkbox resposta, questao 1.C
	chk30 = tk.Checkbutton(place, text='0', var=ckp30) 
	chk30.place(x = 50, y = 380)
	chk31 = tk.Checkbutton(place, text='1', var=ckp31) 
	chk31.place(x = 80, y = 380)
	chk32 = tk.Checkbutton(place, text='2', var=ckp32) 
	chk32.place(x = 110, y = 380)
	chk33 = tk.Checkbutton(place, text='3', var=ckp33) 
	chk33.place(x = 140, y = 380)
	chk34 = tk.Checkbutton(place, text='4', var=ckp34) 
	chk34.place(x = 170, y = 380)
	chk35 = tk.Checkbutton(place, text='5', var=ckp35) 
	chk35.place(x = 200, y = 380)
	chk36 = tk.Checkbutton(place, text='6', var=ckp36) 
	chk36.place(x = 230, y = 380)


	# Enunciado 1.D)questao questao
	pegt4 = tk.Label (place,anchor='w', text= "D)  ")
	pegt4.place(x = 50, y = 440, width=395, height=35 )

	#bloco variaveis da resposta 1.D
	ckp40 = tk.IntVar() 
	ckp40.set(0)
	ckp41 = tk.IntVar() 
	ckp41.set(1)
	ckp42 = tk.IntVar() 
	ckp42.set(2)
	ckp43 = tk.IntVar() 
	ckp43.set(3)
	ckp44 = tk.IntVar() 
	ckp44.set(4)
	ckp45 = tk.IntVar() 
	ckp45.set(5)
	ckp46 = tk.IntVar() 
	ckp46.set(6)

	#checkbox resposta, questao 1.D
	chk40 = tk.Checkbutton(place, text='0', var=ckp40) 
	chk40.place(x = 50, y = 480)
	chk41 = tk.Checkbutton(place, text='1', var=ckp41) 
	chk41.place(x = 80, y = 480)
	chk42 = tk.Checkbutton(place, text='2', var=ckp42) 
	chk42.place(x = 110, y = 480)
	chk43 = tk.Checkbutton(place, text='3', var=ckp43) 
	chk43.place(x = 140, y = 480)
	chk44 = tk.Checkbutton(place, text='4', var=ckp44) 
	chk44.place(x = 170, y = 480)
	chk45 = tk.Checkbutton(place, text='5', var=ckp45) 
	chk45.place(x = 200, y = 480)
	chk46 = tk.Checkbutton(place, text='6', var=ckp46) 
	chk46.place(x = 230, y = 480)


	# Enunciado 1.E)questao questao
	pegt5 = tk.Label (place, anchor='w', text= "E)")
	pegt5.place(x = 50, y = 540, width=395, height=35 )

	#bloco variaveis da resposta 1.E
	ckp50 = tk.IntVar() 
	ckp50.set(0)
	ckp51 = tk.IntVar() 
	ckp51.set(1)
	ckp52 = tk.IntVar() 
	ckp52.set(2)
	ckp53 = tk.IntVar() 
	ckp53.set(3)
	ckp54 = tk.IntVar() 
	ckp54.set(4)
	ckp55 = tk.IntVar() 
	ckp55.set(5)
	ckp56 = tk.IntVar() 
	ckp56.set(6)

	#checkbox resposta, questao 1.E
	chk50 = tk.Checkbutton(place, text='0', var=ckp50) 
	chk50.place(x = 50, y = 580)
	chk51 = tk.Checkbutton(place, text='1', var=ckp51) 
	chk51.place(x = 80, y = 580)
	chk52 = tk.Checkbutton(place, text='2', var=ckp52) 
	chk52.place(x = 110, y = 580)
	chk53 = tk.Checkbutton(place, text='3', var=ckp53) 
	chk53.place(x = 140, y = 580)
	chk54 = tk.Checkbutton(place, text='4', var=ckp54) 
	chk54.place(x = 170, y = 580)
	chk55 = tk.Checkbutton(place, text='5', var=ckp55) 
	chk55.place(x = 200, y = 580)
	chk56 = tk.Checkbutton(place, text='6', var=ckp56) 
	chk56.place(x = 230, y = 580)


	# Enunciado 1.F)questao questao
	pegt6 = tk.Label (place, text= "F)  ", anchor='w')
	pegt6.place(x = 480, y = 140, width=395, height=35 )

    #bloco variaveis da resposta 1.F
	ckp60 = tk.IntVar() 
	ckp60.set(0)
	ckp61 = tk.IntVar() 
	ckp61.set(1)
	ckp62 = tk.IntVar() 
	ckp62.set(2)
	ckp63 = tk.IntVar() 
	ckp63.set(3)
	ckp64 = tk.IntVar() 
	ckp64.set(4)
	ckp65 = tk.IntVar() 
	ckp65.set(5)
	ckp66 = tk.IntVar() 
	ckp66.set(6)

    #checkbox resposta, questao 1.F
	chk60 = tk.Checkbutton(place, text='0', var=ckp60) 
	chk60.place(x = 480, y = 180)
	chk61 = tk.Checkbutton(place, text='1', var=ckp61) 
	chk61.place(x = 510, y = 180)
	chk62 = tk.Checkbutton(place, text='2', var=ckp62) 
	chk62.place(x = 540, y = 180)
	chk63 = tk.Checkbutton(place, text='3', var=ckp63) 
	chk63.place(x = 570, y = 180)
	chk64 = tk.Checkbutton(place, text='4', var=ckp64) 
	chk64.place(x = 600, y = 180)
	chk65 = tk.Checkbutton(place, text='5', var=ckp65) 
	chk65.place(x = 630, y = 180)
	chk66 = tk.Checkbutton(place, text='6', var=ckp66) 
	chk66.place(x = 660, y = 180)

	# Enunciado 1.G)questao questao
	pegt7 = tk.Label (place, text= "G)  ", anchor='w')
	pegt7.place(x = 480, y = 240, width=395, height=35 )

    #bloco variaveis da resposta 1.G
	ckp70 = tk.IntVar() 
	ckp70.set(0)
	ckp71 = tk.IntVar() 
	ckp71.set(1)
	ckp72 = tk.IntVar() 
	ckp72.set(2)
	ckp73 = tk.IntVar() 
	ckp73.set(3)
	ckp74 = tk.IntVar() 
	ckp74.set(4)
	ckp75 = tk.IntVar() 
	ckp75.set(5)
	ckp76 = tk.IntVar() 
	ckp76.set(6)

    #checkbox resposta, questao 1.G
	chk70 = tk.Checkbutton(place, text='0', var=ckp70) 
	chk70.place(x = 480, y = 280)
	chk71 = tk.Checkbutton(place, text='1', var=ckp71) 
	chk71.place(x = 510, y = 280)
	chk72 = tk.Checkbutton(place, text='2', var=ckp72) 
	chk72.place(x = 540, y = 280)
	chk73 = tk.Checkbutton(place, text='3', var=ckp73) 
	chk73.place(x = 570, y = 280)
	chk74 = tk.Checkbutton(place, text='4', var=ckp74) 
	chk74.place(x = 600, y = 280)
	chk75 = tk.Checkbutton(place, text='5', var=ckp75) 
	chk75.place(x = 630, y = 280)
	chk76 = tk.Checkbutton(place, text='6', var=ckp76) 
	chk76.place(x = 660, y = 280)


	# Enunciado 1.H)questao questao
	pegt8 = tk.Label (place, text= "H)  ", anchor='w')
	pegt8.place(x = 480, y = 340, width=395, height=35 )

    #bloco variaveis da resposta 1.H
	ckp80 = tk.IntVar() 
	ckp80.set(0)
	ckp81 = tk.IntVar() 
	ckp81.set(1)
	ckp82 = tk.IntVar() 
	ckp82.set(2)
	ckp83 = tk.IntVar() 
	ckp83.set(3)
	ckp84 = tk.IntVar() 
	ckp84.set(4)
	ckp85 = tk.IntVar() 
	ckp85.set(5)
	ckp86 = tk.IntVar() 
	ckp86.set(6)

    #checkbox resposta, questao 1.H
	chk80 = tk.Checkbutton(place, text='0', var=ckp80) 
	chk80.place(x = 480, y = 380)
	chk81 = tk.Checkbutton(place, text='1', var=ckp81) 
	chk81.place(x = 510, y = 380)
	chk82 = tk.Checkbutton(place, text='2', var=ckp82) 
	chk82.place(x = 540, y = 380)
	chk83 = tk.Checkbutton(place, text='3', var=ckp83) 
	chk83.place(x = 570, y = 380)
	chk84 = tk.Checkbutton(place, text='4', var=ckp84) 
	chk84.place(x = 600, y = 380)
	chk85 = tk.Checkbutton(place, text='5', var=ckp85) 
	chk85.place(x = 630, y = 380)
	chk86 = tk.Checkbutton(place, text='6', var=ckp86) 
	chk86.place(x = 660, y = 380)


	# Enunciado 1.I)questao questao
	pegt7 = tk.Label (place, text= "I)  ", anchor='w')
	pegt7.place(x = 480, y = 440, width=395, height=35 )

    #bloco variaveis da resposta 1.I
	ckp90 = tk.IntVar() 
	ckp90.set(0)
	ckp91 = tk.IntVar() 
	ckp91.set(1)
	ckp92 = tk.IntVar() 
	ckp92.set(2)
	ckp93 = tk.IntVar() 
	ckp93.set(3)
	ckp94 = tk.IntVar() 
	ckp94.set(4)
	ckp95 = tk.IntVar() 
	ckp95.set(5)
	ckp96 = tk.IntVar() 
	ckp96.set(6)

    #checkbox resposta, questao 1.I
	chk90 = tk.Checkbutton(place, text='0', var=ckp90) 
	chk90.place(x = 480, y = 480)
	chk91 = tk.Checkbutton(place, text='1', var=ckp91) 
	chk91.place(x = 510, y = 480)
	chk92 = tk.Checkbutton(place, text='2', var=ckp92) 
	chk92.place(x = 540, y = 480)
	chk93 = tk.Checkbutton(place, text='3', var=ckp93) 
	chk93.place(x = 570, y = 480)
	chk94 = tk.Checkbutton(place, text='4', var=ckp94) 
	chk94.place(x = 600, y = 480)
	chk95 = tk.Checkbutton(place, text='5', var=ckp95) 
	chk95.place(x = 630, y = 480)
	chk96 = tk.Checkbutton(place, text='6', var=ckp96) 
	chk96.place(x = 660, y = 480)


	# Enunciado 1.J)questao questao
	pegt7 = tk.Label (place, text= "J)  ", anchor='w')
	pegt7.place(x = 480, y = 540, width=395, height=35 )

    #bloco variaveis da resposta 1.J
	ckp100 = tk.IntVar() 
	ckp100.set(0)
	ckp101 = tk.IntVar() 
	ckp101.set(1)
	ckp102 = tk.IntVar() 
	ckp102.set(2)
	ckp103 = tk.IntVar() 
	ckp103.set(3)
	ckp104 = tk.IntVar() 
	ckp104.set(4)
	ckp105 = tk.IntVar() 
	ckp105.set(5)
	ckp106 = tk.IntVar() 
	ckp106.set(6)

    #checkbox resposta, questao 1.J
	chk100 = tk.Checkbutton(place, text='0', var=ckp100) 
	chk100.place(x = 480, y = 580)
	chk101 = tk.Checkbutton(place, text='1', var=ckp101) 
	chk101.place(x = 510, y = 580)
	chk102 = tk.Checkbutton(place, text='2', var=ckp102) 
	chk102.place(x = 540, y = 580)
	chk103 = tk.Checkbutton(place, text='3', var=ckp103) 
	chk103.place(x = 570, y = 580)
	chk104 = tk.Checkbutton(place, text='4', var=ckp104) 
	chk104.place(x = 600, y = 580)
	chk105 = tk.Checkbutton(place, text='5', var=ckp105) 
	chk105.place(x = 630, y = 580)
	chk106 = tk.Checkbutton(place, text='6', var=ckp106) 
	chk106.place(x = 660, y = 580)



	#cabeçalho segundo modulo de questoes
	titulo3 = tk.Label (place, text= " 02) Acadêmico   ")
	titulo3.place(x = 910, y = 100)
	titulo3.config(relief="ridge", font="Arial 12 bold", border=3, background="gray")

	# Enunciado 2.A)questao questao
	pegt2 = tk.Label (place, anchor='w',text= "A)  ")
	pegt2.place(x = 910, y = 140, width=400, height=35 )

	#bloco variaveis da resposta 2.A
	ckp220 = tk.IntVar() 
	ckp220.set(0)
	ckp221 = tk.IntVar() 
	ckp221.set(1)
	ckp222 = tk.IntVar() 
	ckp222.set(2)
	ckp223 = tk.IntVar() 
	ckp223.set(3)
	ckp224 = tk.IntVar() 
	ckp224.set(4)
	ckp225 = tk.IntVar() 
	ckp225.set(5)
	ckp226 = tk.IntVar() 
	ckp226.set(6)

    #checkbox resposta, questao 2.A
	chk220 = tk.Checkbutton(place, text='0', var=ckp220) 
	chk220.place(x = 910, y = 180)
	chk221 = tk.Checkbutton(place, text='1', var=ckp221) 
	chk221.place(x = 940, y = 180)
	chk222 = tk.Checkbutton(place, text='2', var=ckp222) 
	chk222.place(x = 970, y = 180)
	chk223 = tk.Checkbutton(place, text='3', var=ckp223) 
	chk223.place(x = 1000, y = 180)
	chk224 = tk.Checkbutton(place, text='4', var=ckp224) 
	chk224.place(x = 1030, y = 180)
	chk225 = tk.Checkbutton(place, text='5', var=ckp225) 
	chk225.place(x = 1060, y = 180)
	chk226 = tk.Checkbutton(place, text='6', var=ckp226) 
	chk226.place(x = 1090, y = 180)

	# Enunciado 2.B)questao questao
	pegt2 = tk.Label (place, anchor='w',text= "B)  ")
	pegt2.place(x = 910, y = 240, width=400, height=35 )

	#bloco variaveis da resposta 2.B
	ckp230 = tk.IntVar() 
	ckp230.set(0)
	ckp231 = tk.IntVar() 
	ckp231.set(1)
	ckp232 = tk.IntVar() 
	ckp232.set(2)
	ckp233 = tk.IntVar() 
	ckp233.set(3)
	ckp234 = tk.IntVar() 
	ckp234.set(4)
	ckp235 = tk.IntVar() 
	ckp235.set(5)
	ckp236 = tk.IntVar() 
	ckp236.set(6)

    #checkbox resposta, questao 2.B
	chk230 = tk.Checkbutton(place, text='0', var=ckp230) 
	chk230.place(x = 910, y = 280)
	chk231 = tk.Checkbutton(place, text='1', var=ckp231) 
	chk231.place(x = 940, y = 280)
	chk232 = tk.Checkbutton(place, text='2', var=ckp232) 
	chk232.place(x = 970, y = 280)
	chk233 = tk.Checkbutton(place, text='3', var=ckp233) 
	chk233.place(x = 1000, y = 280)
	chk234 = tk.Checkbutton(place, text='4', var=ckp234) 
	chk234.place(x = 1030, y = 280)
	chk235 = tk.Checkbutton(place, text='5', var=ckp235) 
	chk235.place(x = 1060, y = 280)
	chk236 = tk.Checkbutton(place, text='6', var=ckp236) 
	chk236.place(x = 1090, y = 280)

	
	# Enunciado 2.C)questao questao
	pegt4 = tk.Label (place, anchor='w',text= "C)  ")
	pegt4.place(x = 910, y = 340, width=400, height=35 )

	#bloco variaveis da resposta 2.C
	ckp240 = tk.IntVar() 
	ckp240.set(0)
	ckp241 = tk.IntVar() 
	ckp241.set(1)
	ckp242 = tk.IntVar() 
	ckp242.set(2)
	ckp243 = tk.IntVar() 
	ckp243.set(3)
	ckp244 = tk.IntVar() 
	ckp244.set(4)
	ckp245 = tk.IntVar() 
	ckp245.set(5)
	ckp246 = tk.IntVar() 
	ckp246.set(6)

    #checkbox resposta, questao 2.C
	chk240 = tk.Checkbutton(place, text='0', var=ckp240) 
	chk240.place(x = 910, y = 380)
	chk241 = tk.Checkbutton(place, text='1', var=ckp241) 
	chk241.place(x = 940, y = 380)
	chk242 = tk.Checkbutton(place, text='2', var=ckp242) 
	chk242.place(x = 970, y = 380)
	chk243 = tk.Checkbutton(place, text='3', var=ckp243) 
	chk243.place(x = 1000, y = 380)
	chk244 = tk.Checkbutton(place, text='4', var=ckp244) 
	chk244.place(x = 1030, y = 380)
	chk245 = tk.Checkbutton(place, text='5', var=ckp245) 
	chk245.place(x = 1060, y = 380)
	chk246 = tk.Checkbutton(place, text='6', var=ckp246) 
	chk246.place(x = 1090, y = 380)


	# Enunciado 2.D)questao questao
	pegt4 = tk.Label (place, anchor='w',text= "D)  ")
	pegt4.place(x = 910, y = 440, width=400, height=35 )

	#bloco variaveis da resposta 2.D
	ckp250 = tk.IntVar() 
	ckp250.set(0)
	ckp251 = tk.IntVar() 
	ckp251.set(1)
	ckp252 = tk.IntVar() 
	ckp252.set(2)
	ckp253 = tk.IntVar() 
	ckp253.set(3)
	ckp254 = tk.IntVar() 
	ckp254.set(4)
	ckp255 = tk.IntVar() 
	ckp255.set(5)
	ckp256 = tk.IntVar() 
	ckp256.set(6)

    #checkbox resposta, questao 2.D
	chk250 = tk.Checkbutton(place, text='0', var=ckp250) 
	chk250.place(x = 910, y = 480)
	chk251 = tk.Checkbutton(place, text='1', var=ckp251) 
	chk251.place(x = 940, y = 480)
	chk252 = tk.Checkbutton(place, text='2', var=ckp252) 
	chk252.place(x = 970, y = 480)
	chk253 = tk.Checkbutton(place, text='3', var=ckp253) 
	chk253.place(x = 1000, y = 480)
	chk254 = tk.Checkbutton(place, text='4', var=ckp254) 
	chk254.place(x = 1030, y = 480)
	chk255 = tk.Checkbutton(place, text='5', var=ckp255) 
	chk255.place(x = 1060, y = 480)
	chk256 = tk.Checkbutton(place, text='6', var=ckp256) 
	chk256.place(x = 1090, y = 480)

def perguntas4():
	place = tk.Tk()
	place.title("login")
	place.geometry("1400x660")
	place.configure(background="#999")

	#fundo da pagina
	fundo01 = tk.Label(place, padx=5, pady=5,background="gray")
	fundo01.place(x= 30, y = 80)
	fundo01.config(border=6, height = 37, width = 185 )

	#botoes da pag
	#ent1 = tk.Button(place, text = "Proximo")
	#ent1.place(x = 1280, y = 620)
	#ent1.configure( relief="ridge", border=6, font="10 bold", height = 1, width = 5)

	ent2 = tk.Button(place, text = "Enviar", command=place.quit)
	ent2.place(x = 1290, y = 620)
	#ent2.configure( relief="ridge", border=6, font="10 bold", height = 1, width = 5)

	ent3 = tk.Button(place, text = "Anterior", command=place.event_info)
	ent3.place(x = 50, y = 620)
	#ent3.configure( relief="ridge", border=6, font="10 bold", height = 1, width = 5)

	botaos = tk.Button(place,text = "sair",command=place.quit)
	botaos.place( x = 1330, y= 2)


	#campo feedback
	fdbk = tk.Label(place, text = " Deixe seu Feedback")
	fdbk.place(x = 980,y = 440, width = 300, height=20)
	fdbkent = tk.Entry(place, bd = 5)	
	fdbkent.place(x = 980,y = 480,width = 300, height=90 )
	

	#Logo /link site
	logo = tk.Button (place, text="Folha CPA", foreground="white", command=lambda: webbrowser.open('https://mail.google.com/mail/u/0/#inbox'))
	logo.place(x = 620, y = 10)		
	logo.configure(relief="ridge", font="Arial 20 bold", border=4, background="gray")


	#infomar pagina
	infpg4 = tk.Label (place, text= " Pagina 4 ")
	infpg4.place(x = 20, y = 20)
	infpg4.config(relief="ridge", font="Arial 8 ", background="#999")

	#cabeçalho primeiro modulo de questoes
	titulo2 = tk.Label (place, text= " 3)Acadêmico – ")
	titulo2.place(x = 50, y = 100)
	titulo2.config(relief="ridge", font="Arial 12 bold", border=3, background="gray")

	# Enunciado 1)questao questao
	pegt1 = tk.Label (place, text= "A) ", anchor='w')
	pegt1.place(x = 50, y = 140, width=395, height=35,)

	#bloco variaveis da resposta 1.A
	ckp10 = tk.IntVar() 
	ckp10.set(0)
	ckp11 = tk.IntVar() 
	ckp11.set(1)
	ckp12 = tk.IntVar() 
	ckp12.set(2)
	ckp13 = tk.IntVar() 
	ckp13.set(3)
	ckp14 = tk.IntVar() 
	ckp14.set(4)
	ckp15 = tk.IntVar() 
	ckp15.set(5)
	ckp16 = tk.IntVar() 
	ckp16.set(6)

    #checkbox resposta, questao 1.A
	chk10 = tk.Checkbutton(place, text='0', var=ckp10) 
	chk10.place(x = 50, y = 180)
	chk11 = tk.Checkbutton(place, text='1', var=ckp11) 
	chk11.place(x = 80, y = 180)
	chk12 = tk.Checkbutton(place, text='2', var=ckp12) 
	chk12.place(x = 110, y = 180)
	chk13 = tk.Checkbutton(place, text='3', var=ckp13) 
	chk13.place(x = 140, y = 180)
	chk14 = tk.Checkbutton(place, text='4', var=ckp14) 
	chk14.place(x = 170, y = 180)
	chk15 = tk.Checkbutton(place, text='5', var=ckp15) 
	chk15.place(x = 200, y = 180)
	chk16 = tk.Checkbutton(place, text='6', var=ckp16) 
	chk16.place(x = 230, y = 180)

	# Enunciado 1.B)questao questao
	pegt2 = tk.Label (place, anchor='w',text= "B) ")
	pegt2.place(x = 50, y = 240, width=395, height=35 )

	#bloco variaveis da resposta 1.B
	ckp20 = tk.IntVar() 
	ckp20.set(0)
	ckp21 = tk.IntVar() 
	ckp21.set(1)
	ckp22 = tk.IntVar() 
	ckp22.set(2)
	ckp23 = tk.IntVar() 
	ckp23.set(3)
	ckp24 = tk.IntVar() 
	ckp24.set(4)
	ckp25 = tk.IntVar() 
	ckp25.set(5)
	ckp26 = tk.IntVar() 
	ckp26.set(6)

	#checkbox resposta, questao 1.B
	chk20 = tk.Checkbutton(place, text='0', var=ckp20) 
	chk20.place(x = 50, y = 280)
	chk21 = tk.Checkbutton(place, text='1', var=ckp21) 
	chk21.place(x = 80, y = 280)
	chk22 = tk.Checkbutton(place, text='2', var=ckp22) 
	chk22.place(x = 110, y = 280)
	chk23 = tk.Checkbutton(place, text='3', var=ckp23) 
	chk23.place(x = 140, y = 280)
	chk24 = tk.Checkbutton(place, text='4', var=ckp24) 
	chk24.place(x = 170, y = 280)
	chk25 = tk.Checkbutton(place, text='5', var=ckp25) 
	chk25.place(x = 200, y = 280)
	chk26 = tk.Checkbutton(place, text='6', var=ckp26) 
	chk26.place(x = 230, y = 280)


	# Enunciado 1.C)questao questao
	pegt3 = tk.Label (place, anchor='w',text= "C)  ")
	pegt3.place(x = 50, y = 340, width=395, height=35 )

	#bloco variaveis da resposta 1.C 
	ckp30 = tk.IntVar() 
	ckp30.set(0)
	ckp31 = tk.IntVar() 
	ckp31.set(1)
	ckp32 = tk.IntVar() 
	ckp32.set(2)
	ckp33 = tk.IntVar() 
	ckp33.set(3)
	ckp34 = tk.IntVar() 
	ckp34.set(4)
	ckp35 = tk.IntVar() 
	ckp35.set(5)
	ckp36 = tk.IntVar() 
	ckp36.set(6)

	#checkbox resposta, questao 1.C
	chk30 = tk.Checkbutton(place, text='0', var=ckp30) 
	chk30.place(x = 50, y = 380)
	chk31 = tk.Checkbutton(place, text='1', var=ckp31) 
	chk31.place(x = 80, y = 380)
	chk32 = tk.Checkbutton(place, text='2', var=ckp32) 
	chk32.place(x = 110, y = 380)
	chk33 = tk.Checkbutton(place, text='3', var=ckp33) 
	chk33.place(x = 140, y = 380)
	chk34 = tk.Checkbutton(place, text='4', var=ckp34) 
	chk34.place(x = 170, y = 380)
	chk35 = tk.Checkbutton(place, text='5', var=ckp35) 
	chk35.place(x = 200, y = 380)
	chk36 = tk.Checkbutton(place, text='6', var=ckp36) 
	chk36.place(x = 230, y = 380)


	# Enunciado 1.D)questao questao
	pegt4 = tk.Label (place,anchor='w', text= "D)  ")
	pegt4.place(x = 50, y = 440, width=395, height=35 )

	#bloco variaveis da resposta 1.D
	ckp40 = tk.IntVar() 
	ckp40.set(0)
	ckp41 = tk.IntVar() 
	ckp41.set(1)
	ckp42 = tk.IntVar() 
	ckp42.set(2)
	ckp43 = tk.IntVar() 
	ckp43.set(3)
	ckp44 = tk.IntVar() 
	ckp44.set(4)
	ckp45 = tk.IntVar() 
	ckp45.set(5)
	ckp46 = tk.IntVar() 
	ckp46.set(6)

	#checkbox resposta, questao 1.D
	chk40 = tk.Checkbutton(place, text='0', var=ckp40) 
	chk40.place(x = 50, y = 480)
	chk41 = tk.Checkbutton(place, text='1', var=ckp41) 
	chk41.place(x = 80, y = 480)
	chk42 = tk.Checkbutton(place, text='2', var=ckp42) 
	chk42.place(x = 110, y = 480)
	chk43 = tk.Checkbutton(place, text='3', var=ckp43) 
	chk43.place(x = 140, y = 480)
	chk44 = tk.Checkbutton(place, text='4', var=ckp44) 
	chk44.place(x = 170, y = 480)
	chk45 = tk.Checkbutton(place, text='5', var=ckp45) 
	chk45.place(x = 200, y = 480)
	chk46 = tk.Checkbutton(place, text='6', var=ckp46) 
	chk46.place(x = 230, y = 480)


	# Enunciado 1.E)questao questao
	pegt5 = tk.Label (place, anchor='w', text= "E)")
	pegt5.place(x = 50, y = 540, width=395, height=35 )

	#bloco variaveis da resposta 1.E
	ckp50 = tk.IntVar() 
	ckp50.set(0)
	ckp51 = tk.IntVar() 
	ckp51.set(1)
	ckp52 = tk.IntVar() 
	ckp52.set(2)
	ckp53 = tk.IntVar() 
	ckp53.set(3)
	ckp54 = tk.IntVar() 
	ckp54.set(4)
	ckp55 = tk.IntVar() 
	ckp55.set(5)
	ckp56 = tk.IntVar() 
	ckp56.set(6)

	#checkbox resposta, questao 1.E
	chk50 = tk.Checkbutton(place, text='0', var=ckp50) 
	chk50.place(x = 50, y = 580)
	chk51 = tk.Checkbutton(place, text='1', var=ckp51) 
	chk51.place(x = 80, y = 580)
	chk52 = tk.Checkbutton(place, text='2', var=ckp52) 
	chk52.place(x = 110, y = 580)
	chk53 = tk.Checkbutton(place, text='3', var=ckp53) 
	chk53.place(x = 140, y = 580)
	chk54 = tk.Checkbutton(place, text='4', var=ckp54) 
	chk54.place(x = 170, y = 580)
	chk55 = tk.Checkbutton(place, text='5', var=ckp55) 
	chk55.place(x = 200, y = 580)
	chk56 = tk.Checkbutton(place, text='6', var=ckp56) 
	chk56.place(x = 230, y = 580)


	# Enunciado 1.F)questao questao
	pegt6 = tk.Label (place, text= "F)  ", anchor='w')
	pegt6.place(x = 480, y = 140, width=395, height=35 )

    #bloco variaveis da resposta 1.F
	ckp60 = tk.IntVar() 
	ckp60.set(0)
	ckp61 = tk.IntVar() 
	ckp61.set(1)
	ckp62 = tk.IntVar() 
	ckp62.set(2)
	ckp63 = tk.IntVar() 
	ckp63.set(3)
	ckp64 = tk.IntVar() 
	ckp64.set(4)
	ckp65 = tk.IntVar() 
	ckp65.set(5)
	ckp66 = tk.IntVar() 
	ckp66.set(6)

    #checkbox resposta, questao 1.F
	chk60 = tk.Checkbutton(place, text='0', var=ckp60) 
	chk60.place(x = 480, y = 180)
	chk61 = tk.Checkbutton(place, text='1', var=ckp61) 
	chk61.place(x = 510, y = 180)
	chk62 = tk.Checkbutton(place, text='2', var=ckp62) 
	chk62.place(x = 540, y = 180)
	chk63 = tk.Checkbutton(place, text='3', var=ckp63) 
	chk63.place(x = 570, y = 180)
	chk64 = tk.Checkbutton(place, text='4', var=ckp64) 
	chk64.place(x = 600, y = 180)
	chk65 = tk.Checkbutton(place, text='5', var=ckp65) 
	chk65.place(x = 630, y = 180)
	chk66 = tk.Checkbutton(place, text='6', var=ckp66) 
	chk66.place(x = 660, y = 180)

	# Enunciado 1.G)questao questao
	pegt7 = tk.Label (place, text= "G)  ", anchor='w')
	pegt7.place(x = 480, y = 240, width=395, height=35 )

    #bloco variaveis da resposta 1.G
	ckp70 = tk.IntVar() 
	ckp70.set(0)
	ckp71 = tk.IntVar() 
	ckp71.set(1)
	ckp72 = tk.IntVar() 
	ckp72.set(2)
	ckp73 = tk.IntVar() 
	ckp73.set(3)
	ckp74 = tk.IntVar() 
	ckp74.set(4)
	ckp75 = tk.IntVar() 
	ckp75.set(5)
	ckp76 = tk.IntVar() 
	ckp76.set(6)

    #checkbox resposta, questao 1.G
	chk70 = tk.Checkbutton(place, text='0', var=ckp70) 
	chk70.place(x = 480, y = 280)
	chk71 = tk.Checkbutton(place, text='1', var=ckp71) 
	chk71.place(x = 510, y = 280)
	chk72 = tk.Checkbutton(place, text='2', var=ckp72) 
	chk72.place(x = 540, y = 280)
	chk73 = tk.Checkbutton(place, text='3', var=ckp73) 
	chk73.place(x = 570, y = 280)
	chk74 = tk.Checkbutton(place, text='4', var=ckp74) 
	chk74.place(x = 600, y = 280)
	chk75 = tk.Checkbutton(place, text='5', var=ckp75) 
	chk75.place(x = 630, y = 280)
	chk76 = tk.Checkbutton(place, text='6', var=ckp76) 
	chk76.place(x = 660, y = 280)


	# Enunciado 1.H)questao questao
	pegt8 = tk.Label (place, text= "H)  ", anchor='w')
	pegt8.place(x = 480, y = 340, width=395, height=35 )

    #bloco variaveis da resposta 1.H
	ckp80 = tk.IntVar() 
	ckp80.set(0)
	ckp81 = tk.IntVar() 
	ckp81.set(1)
	ckp82 = tk.IntVar() 
	ckp82.set(2)
	ckp83 = tk.IntVar() 
	ckp83.set(3)
	ckp84 = tk.IntVar() 
	ckp84.set(4)
	ckp85 = tk.IntVar() 
	ckp85.set(5)
	ckp86 = tk.IntVar() 
	ckp86.set(6)

    #checkbox resposta, questao 1.H
	chk80 = tk.Checkbutton(place, text='0', var=ckp80) 
	chk80.place(x = 480, y = 380)
	chk81 = tk.Checkbutton(place, text='1', var=ckp81) 
	chk81.place(x = 510, y = 380)
	chk82 = tk.Checkbutton(place, text='2', var=ckp82) 
	chk82.place(x = 540, y = 380)
	chk83 = tk.Checkbutton(place, text='3', var=ckp83) 
	chk83.place(x = 570, y = 380)
	chk84 = tk.Checkbutton(place, text='4', var=ckp84) 
	chk84.place(x = 600, y = 380)
	chk85 = tk.Checkbutton(place, text='5', var=ckp85) 
	chk85.place(x = 630, y = 380)
	chk86 = tk.Checkbutton(place, text='6', var=ckp86) 
	chk86.place(x = 660, y = 380)


	# Enunciado 1.I)questao questao
	pegt7 = tk.Label (place, text= "I)  ", anchor='w')
	pegt7.place(x = 480, y = 440, width=395, height=35 )

    #bloco variaveis da resposta 1.I
	ckp90 = tk.IntVar() 
	ckp90.set(0)
	ckp91 = tk.IntVar() 
	ckp91.set(1)
	ckp92 = tk.IntVar() 
	ckp92.set(2)
	ckp93 = tk.IntVar() 
	ckp93.set(3)
	ckp94 = tk.IntVar() 
	ckp94.set(4)
	ckp95 = tk.IntVar() 
	ckp95.set(5)
	ckp96 = tk.IntVar() 
	ckp96.set(6)

    #checkbox resposta, questao 1.I
	chk90 = tk.Checkbutton(place, text='0', var=ckp90) 
	chk90.place(x = 480, y = 480)
	chk91 = tk.Checkbutton(place, text='1', var=ckp91) 
	chk91.place(x = 510, y = 480)
	chk92 = tk.Checkbutton(place, text='2', var=ckp92) 
	chk92.place(x = 540, y = 480)
	chk93 = tk.Checkbutton(place, text='3', var=ckp93) 
	chk93.place(x = 570, y = 480)
	chk94 = tk.Checkbutton(place, text='4', var=ckp94) 
	chk94.place(x = 600, y = 480)
	chk95 = tk.Checkbutton(place, text='5', var=ckp95) 
	chk95.place(x = 630, y = 480)
	chk96 = tk.Checkbutton(place, text='6', var=ckp96) 
	chk96.place(x = 660, y = 480)


	# Enunciado 1.J)questao questao
	pegt7 = tk.Label (place, text= "J)  ", anchor='w')
	pegt7.place(x = 480, y = 540, width=395, height=35 )

    #bloco variaveis da resposta 1.J
	ckp100 = tk.IntVar() 
	ckp100.set(0)
	ckp101 = tk.IntVar() 
	ckp101.set(1)
	ckp102 = tk.IntVar() 
	ckp102.set(2)
	ckp103 = tk.IntVar() 
	ckp103.set(3)
	ckp104 = tk.IntVar() 
	ckp104.set(4)
	ckp105 = tk.IntVar() 
	ckp105.set(5)
	ckp106 = tk.IntVar() 
	ckp106.set(6)

    #checkbox resposta, questao 1.J
	chk100 = tk.Checkbutton(place, text='0', var=ckp100) 
	chk100.place(x = 480, y = 580)
	chk101 = tk.Checkbutton(place, text='1', var=ckp101) 
	chk101.place(x = 510, y = 580)
	chk102 = tk.Checkbutton(place, text='2', var=ckp102) 
	chk102.place(x = 540, y = 580)
	chk103 = tk.Checkbutton(place, text='3', var=ckp103) 
	chk103.place(x = 570, y = 580)
	chk104 = tk.Checkbutton(place, text='4', var=ckp104) 
	chk104.place(x = 600, y = 580)
	chk105 = tk.Checkbutton(place, text='5', var=ckp105) 
	chk105.place(x = 630, y = 580)
	chk106 = tk.Checkbutton(place, text='6', var=ckp106) 
	chk106.place(x = 660, y = 580)



	#cabeçalho segundo modulo de questoes
	titulo3 = tk.Label (place, text= " 02) Acadêmico   ")
	titulo3.place(x = 910, y = 100)
	titulo3.config(relief="ridge", font="Arial 12 bold", border=3, background="gray")

	# Enunciado 2.A)questao questao
	pegt2 = tk.Label (place, anchor='w',text= "A)  ")
	pegt2.place(x = 910, y = 140, width=400, height=35 )

	#bloco variaveis da resposta 2.A
	ckp220 = tk.IntVar() 
	ckp220.set(0)
	ckp221 = tk.IntVar() 
	ckp221.set(1)
	ckp222 = tk.IntVar() 
	ckp222.set(2)
	ckp223 = tk.IntVar() 
	ckp223.set(3)
	ckp224 = tk.IntVar() 
	ckp224.set(4)
	ckp225 = tk.IntVar() 
	ckp225.set(5)
	ckp226 = tk.IntVar() 
	ckp226.set(6)

    #checkbox resposta, questao 2.A
	chk220 = tk.Checkbutton(place, text='0', var=ckp220) 
	chk220.place(x = 910, y = 180)
	chk221 = tk.Checkbutton(place, text='1', var=ckp221) 
	chk221.place(x = 940, y = 180)
	chk222 = tk.Checkbutton(place, text='2', var=ckp222) 
	chk222.place(x = 970, y = 180)
	chk223 = tk.Checkbutton(place, text='3', var=ckp223) 
	chk223.place(x = 1000, y = 180)
	chk224 = tk.Checkbutton(place, text='4', var=ckp224) 
	chk224.place(x = 1030, y = 180)
	chk225 = tk.Checkbutton(place, text='5', var=ckp225) 
	chk225.place(x = 1060, y = 180)
	chk226 = tk.Checkbutton(place, text='6', var=ckp226) 
	chk226.place(x = 1090, y = 180)

	# Enunciado 2.B)questao questao
	pegt2 = tk.Label (place, anchor='w',text= "B)  ")
	pegt2.place(x = 910, y = 240, width=400, height=35 )

	#bloco variaveis da resposta 2.B
	ckp230 = tk.IntVar() 
	ckp230.set(0)
	ckp231 = tk.IntVar() 
	ckp231.set(1)
	ckp232 = tk.IntVar() 
	ckp232.set(2)
	ckp233 = tk.IntVar() 
	ckp233.set(3)
	ckp234 = tk.IntVar() 
	ckp234.set(4)
	ckp235 = tk.IntVar() 
	ckp235.set(5)
	ckp236 = tk.IntVar() 
	ckp236.set(6)

    #checkbox resposta, questao 2.B
	chk230 = tk.Checkbutton(place, text='0', var=ckp230) 
	chk230.place(x = 910, y = 280)
	chk231 = tk.Checkbutton(place, text='1', var=ckp231) 
	chk231.place(x = 940, y = 280)
	chk232 = tk.Checkbutton(place, text='2', var=ckp232) 
	chk232.place(x = 970, y = 280)
	chk233 = tk.Checkbutton(place, text='3', var=ckp233) 
	chk233.place(x = 1000, y = 280)
	chk234 = tk.Checkbutton(place, text='4', var=ckp234) 
	chk234.place(x = 1030, y = 280)
	chk235 = tk.Checkbutton(place, text='5', var=ckp235) 
	chk235.place(x = 1060, y = 280)
	chk236 = tk.Checkbutton(place, text='6', var=ckp236) 
	chk236.place(x = 1090, y = 280)

	
	# Enunciado 2.C)questao questao
	pegt4 = tk.Label (place, anchor='w',text= "C)  ")
	pegt4.place(x = 910, y = 340, width=400, height=35 )

	#bloco variaveis da resposta 2.C
	ckp240 = tk.IntVar() 
	ckp240.set(0)
	ckp241 = tk.IntVar() 
	ckp241.set(1)
	ckp242 = tk.IntVar() 
	ckp242.set(2)
	ckp243 = tk.IntVar() 
	ckp243.set(3)
	ckp244 = tk.IntVar() 
	ckp244.set(4)
	ckp245 = tk.IntVar() 
	ckp245.set(5)
	ckp246 = tk.IntVar() 
	ckp246.set(6)

    #checkbox resposta, questao 2.C
	chk240 = tk.Checkbutton(place, text='0', var=ckp240) 
	chk240.place(x = 910, y = 380)
	chk241 = tk.Checkbutton(place, text='1', var=ckp241) 
	chk241.place(x = 940, y = 380)
	chk242 = tk.Checkbutton(place, text='2', var=ckp242) 
	chk242.place(x = 970, y = 380)
	chk243 = tk.Checkbutton(place, text='3', var=ckp243) 
	chk243.place(x = 1000, y = 380)
	chk244 = tk.Checkbutton(place, text='4', var=ckp244) 
	chk244.place(x = 1030, y = 380)
	chk245 = tk.Checkbutton(place, text='5', var=ckp245) 
	chk245.place(x = 1060, y = 380)
	chk246 = tk.Checkbutton(place, text='6', var=ckp246) 
	chk246.place(x = 1090, y = 380)

class place ( tk.Frame ):


	def __init__ (self):
		place = tk.Tk()
		place.title("FolhaCPA")
		place.geometry("650x600")




		#fundo da pagina
		fundo01 = tk.Label(place, padx=1, pady=5,background="gray")
		fundo01.place(x= 0, y = 125)
		fundo01.config(border=6, height = 1, width = 600 )

		fundo02 = tk.Label(place, padx=5, pady=5,background="gray")
		fundo02.place(x= 0, y = 265)
		fundo02.config(border=6, height = 6, width = 600 )

		#cabeçalho /link site
		rotulo = tk.Button (place, text=" Folha CPA ", foreground="white")
		rotulo.place(x = 240, y = 30)		
		rotulo.configure(relief="ridge", font="Arial 24 bold", border=6, background="gray")

		#botoes home
		botao1 = tk.Button(place, text = "login", command = login)
		botao1.place(x = 440, y = 130)

		botao2 = tk.Button(place, text = "Configurações")
		botao2.place(x = 540, y = 130)

		botao3 = tk.Button(place, text = "Cadastro", command = cadastro)
		botao3.place(x = 480, y = 130)

		#botoes pag
		botao6 = tk.Button(place, text = "Perguntas", command = perguntas)
		botao6.place(x = 180, y = 270)
		botao6.configure(relief="ridge",font="Arial 15 bold", border=4, background="white",height = 1, width = 24)

		botao4 = tk.Button(place, text = "Empresas")
		botao4.place(x = 180, y = 320)
		botao4.configure(relief="ridge",font="Arial 15 bold", border=4, background="white",height = 1, width = 11)

		botao5 = tk.Button(place, text = "Resultados")
		botao5.place(x = 337, y = 320)
		botao5.configure(relief="ridge",font="Arial 15 bold", border=4, background="white",height = 1, width = 11)



		#rodapé
		rodaPe = tk.Label(place, text ="Joao Luz, Marcos, Lucas 3° periodo-ADS")
		rodaPe.place (x= 0, y = 575)
		#rodaPe.config (border=6, height = 1, width = 600, background="Grey" )


		botaos = tk.Button(place,text = "sair",command=place.quit)
		botaos.place( x = 616, y= 2)
place()
tk.mainloop()