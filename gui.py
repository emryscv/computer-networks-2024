#from tkinter import *
from customtkinter import *
import tkinter.ttk as ttk
import httpClient

methods =[ "a", "v"]

def vwcon(percentage):
    print(int(percentage * vw / 100))
    return int(percentage * vw / 100)
    
def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')


def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')
          
window = CTk()

window.geometry("900x630")
window.resizable(False, False)
window.config(padx=20, pady=20)
window.title("HTTP client")

selectedMethod = StringVar()
statusCode = StringVar()
selectedMethod.set(httpClient.methods[0])
statusCode.set("Status code: 200")

#request section
methodMenu = CTkComboBox(window, values=httpClient.methods)
methodMenu.grid(column=0, row=0)

URL = CTkEntry(window, placeholder_text="URL", width=630, font=("",11))
URL.grid(column=1, row=0)

sendBtn = CTkButton(window, width=100, font=("",11), text="Send")
sendBtn.grid(row=0, column=2)

requestDataFields = CTkTabview(window, width=870, height=200)
requestDataFields.grid(row=1, column=0, columnspan=3)

headersReqTab = requestDataFields.add("Headers")
bodyReqTab = requestDataFields.add("Body")

headersReqFrame = CTkScrollableFrame(headersReqTab, width=830, height=190)
bodyReqFrame = CTkTextbox(bodyReqTab, width=850, height=210)

headersReqFrame.pack(fill="both", expand=True)
bodyReqFrame.pack(fill="both", expand=True)

#response section

responseLabel = CTkLabel(window, text="Response")
statusCodeLabel = CTkLabel(window, text=statusCode.get())

responseLabel.grid(row=2, column=0, padx = (0, 50))
statusCodeLabel.grid(row=2, column=2)

responseDataFields = CTkTabview(window, width=870, height=200)
responseDataFields.grid(row=3, column=0, columnspan=3)

headersResTab = responseDataFields.add("Headers")
bodyResTab = responseDataFields.add("Body")
cookiesResTab = responseDataFields.add("Cookies")

headersResFrame = CTkScrollableFrame(headersResTab, width=830, height=200)
bodyResFrame = CTkScrollableFrame(bodyResTab, width=830, height=200)
cookiesResFrame = CTkScrollableFrame(cookiesResTab, width=830, height=200)

headersResFrame.pack(fill="both", expand=True)
bodyResFrame.pack(fill="both", expand=True)
cookiesResFrame.pack(fill="both", expand=True)

# def show(): 
#     label.config( text = clicked.get() ) 
  
# # Dropdown menu options 
# options = [ 
#     "Monday", 
#     "Tuesday", 
#     "Wednesday", 
#     "Thursday", 
#     "Friday", 
#     "Saturday", 
#     "Sunday"
# ] 
  
# # datatype of menu text 
# clicked = StringVar() 
  
# # initial menu text 
# clicked.set( "Monday" ) 
  
# # Create Dropdown menu 
# drop = OptionMenu( window , clicked , *options ) 
# drop.pack() 
  
# # Create button, it will change label text 
# button = Button( window , text = "click Me" , command = show ).pack() 
  
# # Create Label 
# label = Label( window , text = " " ) 
# label.pack() 

window.mainloop()