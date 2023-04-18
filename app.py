from tkinter import *

class TelaPrincipal:

    def _init_(self):
        self.root=Tk()
        self.config()
        self.frames()
        self.widgets()

        self.root.mainloop()

    def config(self):
        self.root.state('zoomed')
        self.root.configure(bg='#B8E0D2')
        self.root.title('Países')

    def frames(self):
        self.frame1=Frame(self.root, bg='gray')
        self.frame1.place(relx=0.02, rely=0.03, relheight=0.65, relwidth=0.425)

        self.frame2=Frame(self.frame1, bg='white')
        self.frame2.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)

        self.frame3=Frame(self.root, bg='white')
        self.frame3.place(relx=0.48, rely=0.03, relheight=0.94, relwidth=0.50)

        self.frame4=Frame(self.root, bg='gray')
        self.frame4.place(relx=0.02, rely=0.7, relheight=0.27, relwidth=0.425)

    def widgets(self):
        self.btn_brazil=PhotoImage(file='btn_brazil.png')
        self.btn1_brazil=Button(self.frame4,bg='gray',image=self.btn_brazil,bd=0,activebackground='gray',command=self.mostrar_brasil)
        self.btn1_brazil.grid(row=0, column=0)

        self.btn_arg=PhotoImage(file='btn_arg.png')
        self.btn2_arg=Button(self.frame4,bg='gray',image=self.btn_arg,bd=0,activebackground='gray',command=self.mostrar_argentina)
        self.btn2_arg.grid(row=1, column=0)

        self.btn_cuba=PhotoImage(file='btn_cuba.png')
        self.btn3_cuba=Button(self.frame4,bg='gray',image=self.btn_cuba,bd=0,activebackground='gray',command=self.mostrar_cuba)
        self.btn3_cuba.grid(row=0, column=1)

        self.btn_grec=PhotoImage(file='btn_grec.png')
        self.btn4_grec=Button(self.frame4,bg='gray',image=self.btn_grec,bd=0,activebackground='gray',command=self.mostrar_grec)
        self.btn4_grec.grid(row=1, column=1)

        self.btn_end=PhotoImage(file='btn_azul.png')
        self.btn5_end=Button(self.frame4,bg='gray',image=self.btn_end,bd=0,activebackground='gray',command=self.fechar)
        self.btn5_end.place(relx=0.60, rely=0.30)

    def mostrar_brasil(self):
        self.limpar()
        self.txt_info=Label(self.frame2, text='Brasil \n Local:\n América do Sul \nAno de Independência: 1822\nPopulação: 214,3 milhões \nPIB: 1,609 trilhão USD',bg='white', fg='black',font=('courier',32))
        self.txt_info.pack(padx=20, pady=20)
       
        self.img_br=PhotoImage(file='mapa_br4.png')
        self.lbl_img_br=Label(self.frame3,image=self.img_br, bg='white')
        self.lbl_img_br.pack(pady=20)

    def mostrar_argentina(self):
        self.limpar()
        self.txt_info=Label(self.frame2, text='Argentina \n Local:\n América do Sul \nAno de Independência: 1810\nPopulação: 45,81 milhões \nPIB: 487,2 bilhões USD ',bg='white', fg='black',font=('courier',32))
        self.txt_info.pack(padx=20, pady=20)

        self.img_ar=PhotoImage(file='mapa_argentina.png')
        self.lbl_img_ar1=Label(self.frame3,image=self.img_ar, bg='white')
        self.lbl_img_ar1.pack(pady=20)


    def mostrar_cuba(self):
        self.limpar()
        self.txt_info=Label(self.frame2, text='Cuba \n Local:\n América Central \nAno de Independência: 1898\nPopulação: 11,26 milhões \nPIB: 107,4 bilhões USD ',bg='white', fg='black',font=('courier',32))
        self.txt_info.pack(padx=20, pady=20)

        self.img_cuba=PhotoImage(file='mapa_cuba.png')
        self.lbl_img_cuba2=Label(self.frame3,image=self.img_cuba, bg='white')
        self.lbl_img_cuba2.pack(pady=20)

    def mostrar_grec(self):
        self.limpar()
        self.txt_info=Label(self.frame2, text='Grécia \n Local:\n Sudeste da Europa \nAno de Independência: 1832\nPopulação: 10,64 milhões \nPIB: 214,9 bilhões USD ',bg='white', fg='black',font=('courier',32))
        self.txt_info.pack(padx=20, pady=20)

        self.img_grecia=PhotoImage(file='mapa_grecia.png')
        self.lbl_img_grecia3=Label(self.frame3,image=self.img_grecia, bg='white')
        self.lbl_img_grecia3.pack(pady=20)

    def limpar(self):
        for item in self.frame2.winfo_children():
            item.destroy()
        for item in self.frame3.winfo_children():
            item.destroy()
        self.frame3['bg']='white'

    def fechar(self):
        self.root.destroy()
