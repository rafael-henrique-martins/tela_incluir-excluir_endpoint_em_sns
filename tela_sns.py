from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()

class Funcs():
    def limpar_tela(self):
        self.endpoint_entry.delete(0, END)
        self.protocolo_entry.delete(0, END)
        self.topico_entry.delete(0, END)

    def OnDoubleClick(self, event):
        self.listaCli.selection()

        if self.topico_entry.get() == "":
            self.limpar_tela()
            for n in self.listaCli.selection():
                col1 = self.listaCli.item(n, 'values')
                self.topico_entry.insert(END, col1)
        else:
            for n in self.listaCli.selection():
                col1 = self.listaCli.item(n, 'values')
                self.endpoint_entry.insert(END, col1)

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()

        root.mainloop()

    def tela(self):
        self.root.title("cadastrar email")
        self.root.configure(background="#393939")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.minsize = self.root.minsize(width=500, height=500)
    def frames_da_tela(self):
        self.frames_1 = Frame(self.root, border=4, bg="#DCDCDC",highlightbackground="#808080",highlightthickness=3)
        self.frames_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frames_2 = Frame(self.root, border=4, bg="#DCDCDC", highlightbackground="#808080", highlightthickness=3)
        self.frames_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        self.bt_limpar = Button(self.frames_1, text="Limpar", bd=2,bg="#FFFAFA", fg="#107db2", font=("verdana", 8, "bold"),
                                command=self.limpar_tela)
        self.bt_limpar.place(relx=0.05, rely=0.75, relwidth=0.1, relheight=0.12)

        self.bt_buscar = Button(self.frames_1, text="Buscar Topico", bd=2,bg="#FFFAFA", fg="#107db2", font=("verdana", 8, "bold"),
                                )#command=self.buscar_topicos)
        self.bt_buscar.place(relx=0.16, rely=0.75, relwidth=0.18, relheight=0.12)

        self.bt_buscar = Button(self.frames_1, text="Buscar email",bd=2, bg="#FFFAFA", fg="#107db2", font=("verdana", 8, "bold"),
                                )#command=self.buscar_endpoints)
        self.bt_buscar.place(relx=0.35, rely=0.75, relwidth=0.18, relheight=0.12)

        self.bt_novo = Button(self.frames_1, text="Adicionar", bd=2,bg="#FFFAFA", fg="#107db2", font=("verdana", 8, "bold"),
                                )#command=self.adicionar_usuario)
        self.bt_novo.place(relx=0.60, rely=0.75, relwidth=0.13, relheight=0.12)

        self.bt_apagar = Button(self.frames_1, text="Excluir", bd=2,bg="#FFFAFA", fg="#107db2", font=("verdana", 8, "bold"),
                                )#command=self.excluir_usuario)
        self.bt_apagar.place(relx=0.74, rely=0.75, relwidth=0.12, relheight=0.12)


        self.lb_topico = Label(self.frames_1, text="topico", bg="#DCDCDC", fg="#393939", font=("verdana", 10, "bold"))
        self.lb_topico.place(relx=0.05, rely=0.1)

        self.topico_entry = Entry(self.frames_1)
        self.topico_entry.place(relx=0.05, rely=0.2, relwidth=0.8, relheight=0.07)

        self.lb_endpoint= Label(self.frames_1, text="email", bg="#DCDCDC", fg="#393939", font=("verdana", 10, "bold"))
        self.lb_endpoint.place(relx=0.05, rely=0.35)

        self.endpoint_entry = Entry(self.frames_1)
        self.endpoint_entry.place(relx=0.05, rely=0.45, relwidth=0.4, relheight=0.07)

        self.lb_protocolo = Label(self.frames_1, text="protocolo", bg="#DCDCDC", fg="#393939", font=("verdana", 10, "bold"))
        self.lb_protocolo.place(relx=0.55, rely=0.35)

        self.protocolo_entry = Entry(self.frames_1)
        self.protocolo_entry.place(relx=0.55, rely=0.45, relwidth=0.18, relheight=0.07)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frames_2, height=3, columns=("col1"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Clique 2 vezes")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=590)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        #
        self.scroolLista = Scrollbar(self.frames_2,orient="vertical")
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96,rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)


Application()
