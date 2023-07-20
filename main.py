from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import boto3

client = boto3.client('sns')

root = Tk()

class Funcs():
    def limpar_tela(self):

    def limpar_campos(self):
        self.endpoint_entry.delete(0, END)
        self.protocolo_entry.delete(0, END)

    def add_cliente(self):
        topico = self.topico_entry.get()
        endpoint = self.endpoint_entry.get()
        protocolo = self.protocolo_entry.get()

        if topico == "" or endpoint == "":
            msg = "Para incluir um novo email é necessario \n"
            msg += "ter todos os campos preenchidos"

            messagebox.showinfo("AVISO DE CAMPO VAZIO", msg)

        else:
            res = client.subscribe(
                TopicArn=topico,
                Protocol=protocolo,
                Endpoint=endpoint,

                ReturnSubscriptionArn=True
            )

            if res['ResponseMetadata']['HTTPStatusCode'] == 200:
                msg = "O email ", endpoint, " foi cadastrado com sucesso"
                messagebox.showinfo("Aviso", msg)

            else:
                msg= "Erro no cadastro do email ", endpoint
                messagebox.showinfo("AVISO", msg)

            self.limpar_campos()

    def select_list(self, lista):
        self.listCli.delete(*self.listCli.get_children())

        for i in lista:
            self.listaCli.insert("", END, values=i)

    def buscar_topicos(self):
        lista_topicos = client.list_topics()
        list_arn = []

        for i in lista_topicos['Topics']:
            list_arn.append(i['TopicArn'])

        self.select_lista(list_arn)

    def buscar_endpoints(self):
        topico = self.topico_entry.get()
        if topico == "":
            msg = "Para fazer a busca de emails é necessario \n"
            msg += "ter o topico selecionado"

            messagebox.showinfo("AVISO", msg)

        else:
            topico = self.topico_entry.get()
            protocol = ""
            Subscriptio_arn = []
            response = client.list_subscriptions_by_topic(
                TopicArn=topico
            )

            for i in response['Subscriptions']:
                Subscriptio_arn.append(i['Endpoint'])
                protocol = i['Protocol']

            self.protocol_entry.insert(END, protocol)
            self.select_lista(Subscriptio_arn)

    def OnDoubleClick(self, event):
        self.listaCli.selection()

        if self.topico_entry.get() == "":
            for n in self.listaCli.selection():
                col1 = self.listaCli.item(n, 'values')
                self.topico_entry.insert(END, col1)
        else:
            for n in self.listaCli.selection():
                col1 = self.listaCli.item(n, 'values')
                self.endpoint_entry.insert(END, col1)

    def delete_cliente(self):
        topico_arn = str(self.topico_entry.get())
        endpoint = self.endpoint_entry.get()
        protocolo = self.protocolo_entry.get()

        if topico_arn == "" or endpoint == "" or protocolo =="":
            msg = "Para excluir um mail é necessario \n"
            msg = "ter todos os campos preenchidos"

            messagebox.showinfo("AVISO", msg)
        else:
            ok_cancel = messagebox.askokcancel("Tem certeza?")

            if ok_cancel:
                response = client.list_subscriptions_by_topic(
                    TopicArn=topico_arn
                )
                for i in response['Subscriptons']:
                    if i['Endpoint'] == endpoint:
                        subscription_arn = i['SubscriptionArn']

                response = client.unsubscribe(
                    SubscriptionArn=subscription_arn
                )

                if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                    msg = "O email ", endpoint, " foi excluido com sucesso"
                    messagebox.showinfo("AVISO", msg)

                else:
                    msg = "Erro na exclusao do email ", endpoint
                    messagebox.showerror("AVISO", msg)

                self.limpar_campos()

            else:
                self.limpar_campos()


class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.list_frame2
        root.mainloop()

    def tela(self):
        self.root.title("cadastrar email")
        self.root.configure(background="#393939")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.minsize = self.root.minsize(width=500, height=500)

    def frames_da_tela(self):
        self.frames1 = Frame(self.root, border=4, bg="#DCDCDC",highlightbackground="#808080",highlightthickness=3)
        self.frames1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frames2 = Frame(self.root, border=4, bg="#DCDCDC", highlightbackground="#808080", highlightthickness=3)
        self.frames2.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):












