from tkinter import *
from tkinter import messagebox
from regex.python_regex import *

window = Tk()
#karmany[at]email[dot]net
# button action
def clicked():
    """ This function get the data and send to module 
    python_regex.assess to validate the data
    """
    form= {
        'name': txt_name.get(),
        'last_name': txt_last_name.get(),
        'address': txt_address.get(),
        'email': txt_email.get(),
        'birthday': txt_birthday.get(),
        'mobile': txt_mobile.get(),
        'phone': txt_phone.get(),
        'postal_code': txt_postal_code.get()
    }    
    messagebox.showinfo('Alerta',assess(form))
    

# Title and size of window
window.title("Registrese Gratis")
window.geometry('500x500')
#window.resizable(width=False, height=False)

# labels
lbl_title = Label(window, text="Bienvenido al Sistema", font=("Arial Bold", 12))
lbl_info = Label(window, text="Por favor llene los siguientes campos")
lbl_name = Label(window, text="Nombres: ")
lbl_last_name = Label(window, text="Apellidos: ")
lbl_address = Label(window, text="Dirección: ")
lbl_email = Label(window, text="Email: ")
lbl_birthday = Label(window, text="Fecha de Nacimiento: ")
lbl_mobile = Label(window, text="Celular: ")
lbl_phone = Label(window, text="Telefono fijo: ")
lbl_postal_code = Label(window, text="Codigo Postal : ")

# text inputs
txt_name = Entry(window,width=20)
txt_last_name = Entry(window,width=20)
txt_address = Entry(window,width=20)
txt_email = Entry(window,width=20)
txt_birthday = Entry(window,width=20)
txt_mobile = Entry(window,width=20)
txt_phone = Entry(window,width=20)
txt_postal_code = Entry(window,width=20)

# button
btn = Button(window, text="Enviar", command=clicked)

# position
lbl_title.grid(column=1, row=0)


lbl_name.grid(column=1, row=4)
lbl_last_name.grid(column=1, row=5)
lbl_address.grid(column=1, row=6)
lbl_email.grid(column=1, row=7)
lbl_birthday.grid(column=1, row=8)
lbl_mobile.grid(column=1, row=9)
lbl_phone.grid(column=1, row=10)
lbl_postal_code.grid(column=1, row=11)

txt_name.grid(column=2, row=4)
txt_last_name.grid(column=2, row=5)
txt_address.grid(column=2, row=6)
txt_email.grid(column=2, row=7)
txt_birthday.grid(column=2, row=8)
txt_mobile.grid(column=2, row=9)
txt_phone.grid(column=2, row=10)
txt_postal_code.grid(column=2, row=11)

btn.grid(column=2, row=12)

lbl_title.config(padx=10, pady=10)
lbl_name.config(padx=10, pady=10)
lbl_last_name.config(padx=10, pady=10)
lbl_address.config(padx=10, pady=10)
lbl_email.config(padx=10, pady=10)
lbl_birthday.config(padx=10, pady=10)
lbl_mobile.config(padx=10, pady=10)
lbl_phone.config(padx=10, pady=10)
lbl_postal_code.config(padx=10, pady=10)


window.mainloop()