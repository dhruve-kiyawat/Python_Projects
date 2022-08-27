a=""
b,c,d,E=0,0,0,0

import math
import tkinter as tk

window=tk.Tk()
window.title("Advanced Calculator")
window.columnconfigure([0,1,2,3],minsize=22,weight=1)
window.rowconfigure([0,1,2,3,4,5],minsize=22,weight=1)
frm1=tk.Frame(master=window,relief=tk.RAISED,borderwidth=15)
frm2=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm3=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm4=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm5=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm6=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm7=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm8=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm9=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm10=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm11=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm12=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm13=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm14=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm15=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm16=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm17=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm18=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm19=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm20=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm21=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)
frm22=tk.Frame(master=window,relief=tk.RAISED,borderwidth=10)

frm1.grid(row=0, column=0,columnspan=3,  sticky="nsew")
frm2.grid(row=0, column=3,  sticky="nsew")
frm3.grid(row=2, column=0,  sticky="nsew")
frm4.grid(row=3, column=0,  sticky="nsew")
frm5.grid(row=4, column=0,  sticky="nsew")
frm6.grid(row=5, column=0,  sticky="nsew") 
frm7.grid(row=2, column=1,  sticky="nsew")
frm8.grid(row=3, column=1,  sticky="nsew")
frm9.grid(row=4, column=1,  sticky="nsew")
frm10.grid(row=5, column=1,  sticky="nsew") 
frm11.grid(row=2, column=2,  sticky="nsew")
frm12.grid(row=3, column=2,  sticky="nsew")
frm13.grid(row=4, column=2,  sticky="nsew")
frm14.grid(row=5, column=2,  sticky="nsew") 
frm15.grid(row=2, column=3,  sticky="nsew")
frm16.grid(row=3, column=3,  sticky="nsew")
frm17.grid(row=4, column=3,  sticky="nsew")
frm18.grid(row=5, column=3,  sticky="nsew")
frm19.grid(row=1, column=0,  sticky="nsew")
frm20.grid(row=1, column=1,  sticky="nsew")	
frm21.grid(row=1, column=2,  sticky="nsew")	
frm22.grid(row=1, column=3,  sticky="nsew")	

def one():
	global a
	a=a+"1"
	lbl1.configure(text=a)

def two():
	global a
	a=a+"2"
	lbl1.configure(text=a)

def three():
	global a
	a=a+"3"
	lbl1.configure(text=a)

def four():
	global a
	a=a+"4"
	lbl1.configure(text=a)

def five():
	global a
	a=a+"5"
	lbl1.configure(text=a)

def six():
	global a
	a=a+"6"
	lbl1.configure(text=a)	

def seven():
	global a
	a=a+"7"
	lbl1.configure(text=a)	

def eight():
	global a
	a=a+"8"
	lbl1.configure(text=a)	

def nine():
	global a
	a=a+"9"
	lbl1.configure(text=a)	

def zero():
	global a
	a=a+"0"
	lbl1.configure(text=a)

def add():
	global a,b,c,d
	a=calc(a)
	b=float(a)
	a=""	
	d="+"
	lbl1.configure(text=a)
	btn10.configure(command=decimal)
	btn13.configure(command=none)
	btn14.configure(command=none)
	btn15.configure(command=none)
	btn16.configure(command=none)
	btn17.configure(command=none)
	btn18.configure(command=none)
	btn19.configure(command=none)
	btn20.configure(command=none)

def substract():	
	global a,b,c,d
	a=calc(a)
	b=float(a)
	a=""	
	d="-"
	lbl1.configure(text=a)
	btn10.configure(command=decimal)
	btn13.configure(command=none)
	btn14.configure(command=none)
	btn15.configure(command=none)
	btn16.configure(command=none)
	btn17.configure(command=none)
	btn18.configure(command=none)
	btn19.configure(command=none)
	btn20.configure(command=none)

def multiply():	
	global a,b,c,d
	a=calc(a)
	b=float(a)
	a=""	
	d="*"
	lbl1.configure(text=a)
	btn10.configure(command=decimal)
	btn13.configure(command=none)
	btn14.configure(command=none)
	btn15.configure(command=none)
	btn16.configure(command=none)
	btn17.configure(command=none)
	btn18.configure(command=none)
	btn19.configure(command=none)
	btn20.configure(command=none)

def divide():	
	global a,b,c,d
	a=calc(a)
	b=float(a)
	a=""	
	d="/"
	lbl1.configure(text=a)
	btn10.configure(command=decimal)
	btn13.configure(command=none)
	btn14.configure(command=none)
	btn15.configure(command=none)
	btn16.configure(command=none)
	btn17.configure(command=none)
	btn18.configure(command=none)
	btn19.configure(command=none)
	btn20.configure(command=none)

def clear():
	global a,b,c,d
	a=""
	lbl1.configure(text=a)
	b,c,d=0,0,0
	btn10.configure(command=decimal)
	btn12.configure(bg="white",text="DEL",command=delete)
	btn11.configure(text="=",command=equal)
	btn13.configure(command=multiply)
	btn14.configure(command=divide)
	btn15.configure(command=add)
	btn16.configure(command=substract)
	btn17.configure(command=Sin)
	btn18.configure(command=Cos)
	btn19.configure(command=Tan)
	btn20.configure(command=Root)

def delete():	
	global a,b,c,d	
	l=len(a)
	e=""
	if a[0:3]=="Sin" or a[0:3]=="Cos" or a[0:3]=="Tan" or a[0]=="√":
		a=""
	else:
		for i in range (l-1):
			e=e+a[i]
		a=e
	lbl1.configure(text=a)

def equal():
  global a,b,c,d	
  if a[0:3]=="Sin" or a[0:3]=="Cos" or a[0:3]=="Tan" or a[0]=="√":
    a=calc(a)
    c=float(a)
    a=c
    lbl1.configure(text=a)
  else:
    c=float(a)
    a=""
    lbl1.configure(text=a)
    if d=="+":
      a=c+b
      lbl1.configure(text=a)
    if d=="-":
      a=b-c
      lbl1.configure(text=a)
    if d=="*":
      a=c*b
      lbl1.configure(text=a)
    if d=="/":
      a=b/c
      lbl1.configure(text=a)
  btn12.configure(bg="#EF5350",text="CLEAR",command=clear)
  btn11.configure(text="=",command=equal2)

def equal2():
	global a,b,c,d
	if a[0:3]=="Sin" or a[0:3]=="Cos" or a[0:3]=="Tan" or a[0]=="√":
		a=calc(a)
		b=float(a)
		a=b
		lbl1.configure(text=a)
	else:
		b=float(a)
		a=""
		lbl1.configure(text=a)
		if d=="+":
			a=c+b
			lbl1.configure(text=a)
		if d=="-":
			a=b-c
			lbl1.configure(text=a)
		if d=="*":
			a=c*b
			lbl1.configure(text=a)
		if d=="/":
			a=b/c
			lbl1.configure(text=a)
	btn11.configure(text="=",command=equal2)

def decimal():	
	global a
	a=a+"."
	lbl1.configure(text=a)
	btn10.configure(command=none)

def Sin():
	global a
	if a=="" or a==" ":
		a=a+"Sin"
	else:
		None
	lbl1.configure(text=a)
	math.sin((math.pi/180)*a)

def Cos():
	global a
	if a=="" or a==" ":
		a=a+"Cos"
	else:
		None
	lbl1.configure(text=a)
	math.cos((math.pi/180)*a)

def Tan():
	global a
	if a=="" or a==" ":
		a=a+"Tan"
	else:
		None
	lbl1.configure(text=a)
	math.tan((math.pi/180)*a)

def none():
	None

def Root():
	global a
	if a=="" or a==" ":
		a=a+"√"
	else:
		None
	lbl1.configure(text=a)
	

def calc(a):
	if a[0:3]=="Sin":
		return math.sin((math.pi/180)*float(a[3:]))
	elif a[:3]=="Cos":
		return math.cos((math.pi/180)*float(a[3:])) 
	elif a[:3]=="Tan":
		return math.tan((math.pi/180)*float(a[3:]))
	elif a[0]=="√":
		return math.sqrt(float(a[1:]))
	else:
		return a
	
lbl1=tk.Label(master=frm1,text="",height=2,width=5,bg="lightgreen") 
btn1=tk.Button(master=frm3, text="1",width=5,command=one)
btn2=tk.Button(master=frm7, text="2",width=5,command=two)
btn3=tk.Button(master=frm11, text="3",width=5,command=three)
btn4=tk.Button(master=frm4, text="4",width=5,command=four)
btn5=tk.Button(master=frm8, text="5",width=5,command=five)
btn6=tk.Button(master=frm12, text="6",width=5,command=six)
btn7=tk.Button(master=frm5, text="7",width=5,command=seven)
btn8=tk.Button(master=frm9, text="8",width=5,command=eight)
btn9=tk.Button(master=frm13, text="9",width=5,command=nine)
btn0=tk.Button(master=frm10, text="0",width=5,command=zero)
btn10=tk.Button(master=frm6, text=".",width=5,command=decimal)
btn11=tk.Button(master=frm14, text="=",width=5,command=equal) 
btn12=tk.Button(master=frm2, text="DEL",width=5,command=delete)
btn13=tk.Button(master=frm15, text="*",width=5,command=multiply)
btn14=tk.Button(master=frm16, text="/",width=5,command=divide)
btn15=tk.Button(master=frm17, text="+",width=5,command=add)
btn16=tk.Button(master=frm18, text="-",width=5,command=substract) 
btn17=tk.Button(master=frm19, text="Sin",width=5,command=Sin) 
btn18=tk.Button(master=frm20, text="Cos",width=5,command=Cos) 
btn19=tk.Button(master=frm21, text="Tan",width=5,command=Tan) 
btn20=tk.Button(master=frm22, text="√",width=5,command=Root) 

lbl1.pack(   side=tk.LEFT,fill=tk.BOTH ,expand=True)
btn1.pack(  side=tk.LEFT, fill=tk.BOTH,expand=True)
btn2.pack(   side=tk.LEFT,fill=tk.BOTH, expand=True)
btn3.pack(   side=tk.LEFT,fill=tk.BOTH, expand=True)
btn4.pack(   side=tk.LEFT,fill=tk.BOTH, expand=True)
btn5.pack(   side=tk.LEFT,fill=tk.BOTH, expand=True)
btn6.pack(   side=tk.LEFT,fill=tk.BOTH, expand=True)
btn7.pack(   side=tk.LEFT,fill=tk.BOTH, expand=True)
btn8.pack(   side=tk.LEFT,fill=tk.BOTH, expand=True)
btn9.pack(   side=tk.LEFT,fill=tk.BOTH, expand=True)
btn10.pack(   side=tk.LEFT,fill=tk.BOTH, expand=True)
btn0.pack(   side=tk.LEFT, fill=tk.BOTH,expand=True)
btn11.pack(   side=tk.LEFT,fill=tk.BOTH, expand=True) 
btn12.pack( ipady=10 ,  side=tk.LEFT,fill=tk.BOTH, expand=True)
btn13.pack(   side=tk.LEFT ,fill=tk.BOTH,expand=True)
btn14.pack(   side=tk.TOP, fill=tk.BOTH,expand=True)
btn15.pack(   side=tk.TOP, fill=tk.BOTH,expand=True)
btn16.pack(   side=tk.TOP, fill=tk.BOTH,expand=True) 
btn17.pack(   side=tk.TOP, fill=tk.BOTH,expand=True) 
btn18.pack(   side=tk.TOP, fill=tk.BOTH,expand=True) 
btn19.pack(   side=tk.TOP, fill=tk.BOTH,expand=True) 
btn20.pack(   side=tk.TOP, fill=tk.BOTH,expand=True) 

lbl1.configure(font=("Arial, 30"))
btn1.configure(font=("Arial, 28"))
btn2.configure(font=("Arial, 28"))
btn3.configure(font=("Arial, 28"))
btn4.configure(font=("Arial, 28"))
btn5.configure(font=("Arial, 28"))
btn6.configure(font=("Arial, 28"))
btn7.configure(font=("Arial, 28"))
btn8.configure(font=("Arial, 28"))
btn9.configure(font=("Arial, 28"))
btn10.configure(font=("Arial, 28"))
btn11.configure(font=("Arial, 28"))
btn12.configure(font=("Arial, 22"))
btn13.configure(font=("Arial, 28"))
btn14.configure(font=("Arial, 28"))
btn15.configure(font=("Arial, 28"))
btn16.configure(font=("Arial, 28"))
btn17.configure(font=("Arial, 28"))
btn18.configure(font=("Arial, 28"))
btn19.configure(font=("Arial, 28"))
btn20.configure(font=("Arial, 28"))
btn0.configure(font=("Arial, 28"))

window.mainloop()
