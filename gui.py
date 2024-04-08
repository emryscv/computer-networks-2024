#from tkinter import *
from customtkinter import *
from CTkTable import CTkTable
import httpClient
    
#CTk configs
window = CTk()

window.geometry("900x630")
window.resizable(False, False)
window.config(padx=20, pady=20)
window.title("HTTP client")

statusCode = StringVar()
responseHeaders = [["Key", "Value"]]

statusCode.set("Status: none")

#Handlers
def sendBtnHandler():
    global responseHeaders
    
    status, headers, body = httpClient.request(methodMenu.get(), URL.get(), [], "")
    responseHeaders = [["Key", "Value"]] + headers
    
    statusCode.set("Status: " + status)
    
    headersResTable.delete_rows([i for i in range(0,headersResTable.rows)])
    
    for header in responseHeaders:
        headersResTable.add_row(header, headersResTable.rows)

    print(body)

    bodyResFrame.delete(0.0, 'end')
    bodyResFrame.insert(0.0, body)

#request section
methodMenu = CTkComboBox(window, values=httpClient.methods)
URL = CTkEntry(window, placeholder_text="URL", width=630, font=("",11))
sendBtn = CTkButton(window, width=100, font=("",11), text="Send", command=sendBtnHandler)

requestDataFields = CTkTabview(window, width=870, height=200, anchor="nw")

headersReqTab = requestDataFields.add("Headers")
bodyReqTab = requestDataFields.add("Body")
headersReqFrame = CTkScrollableFrame(headersReqTab, width=830, height=190)
bodyReqFrame = CTkTextbox(bodyReqTab, width=850, height=210)
headersReqTable = CTkTable(headersReqFrame, column=2, values=[["Key", "Value"]])

methodMenu.grid(row=0, column=0)
URL.grid(row=0, column=1)
sendBtn.grid(row=0, column=2)
requestDataFields.grid(row=1, column=0, columnspan=3)

headersReqFrame.pack(fill="both", expand=True)
bodyReqFrame.pack(fill="both", expand=True)
headersReqTable.pack(fill="both", expand=True)

#response section

responseLabel = CTkLabel(window, text="Response", anchor="w")
statusCodeLabel = CTkLabel(window, textvariable=statusCode)

responseDataFields = CTkTabview(window, width=870, height=200, anchor="nw")

headersResTab = responseDataFields.add("Headers")
bodyResTab = responseDataFields.add("Body")
cookiesResTab = responseDataFields.add("Cookies")

headersResFrame = CTkScrollableFrame(headersResTab, width=830, height=200)
bodyResFrame = CTkTextbox(bodyResTab, width=850, height=210)
cookiesResFrame = CTkScrollableFrame(cookiesResTab, width=830, height=200)

headersResTable = CTkTable(headersResFrame, column=2, values=responseHeaders)
cookiesResTable = CTkTable(cookiesResFrame, column=7, values=[["Name", "Value", "Domain", "Path", "Expires", "HttpOnly", "Secure"]])

responseLabel.grid(row=2, column=0)
statusCodeLabel.grid(row=2, column=1, columnspan=2)

responseDataFields.grid(row=3, column=0, columnspan=3)

headersResFrame.pack(fill="both", expand=True)
bodyResFrame.pack(fill="both", expand=True)
cookiesResFrame.pack(fill="both", expand=True)

headersResTable.pack(fill="both", expand=True)
cookiesResTable.pack(fill="both", expand=True)

window.mainloop()

