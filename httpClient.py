import socket
import os
import re

methods = ["OPTIONS", "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "CONNECT"]

generalHeaders = ["Cache-Control", "Connection", "Date", "Pragma", "Trailer", "Transfer-Enconding", "Upgrade", "Via", "Warning"]
requestHeaders = ["Accept","Accept-Charset","Accept-Encoding","Accept-Language", "Authorization", "Expect", "From", "Host", "If-Match", "If-Modified-Since", "If-None-Match", "If-Range", "If-Unmodified-Since", "Max-Forwards", "Proxy-Authorization","Range", "Referer", "TE", "User-Agent" ]
entityHeaders = ["Allow", "Content-Encoding", "Content-Language","Content-Length", "Content-Location", "Content-MD5", "Content-Range", "Content-Type", "Expires", "Last-Modified"]
"""
def start():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        os.system("cls")
        print("Pick a method: ")

        i = 1
        for method in methods:
            print(i, "-", method)
            i+=1    
            
        option = int(input("Enter the Method: "))
        
        if option < 1 or option > 8:
            print(f"Not a valid option: {option}")
            input("Enter to continue")
            continue
        
        method = methods[option]

        address = input("Enter the address: ")

        #address parsing
        firstSlash = len(address) if (address.find("/") == -1) else address.find("/")
        firstColon = firstSlash if (address.find(":") == -1) else address.find(":")

        host = address[:firstColon]
        port = "80" if(firstColon ==  firstSlash) else address[firstColon + 1:firstSlash]
        URI = "/" if(firstSlash == len(address)) else address[firstSlash:] 

        print("host:", host, " port:", port, " URI:", URI)

#        try:
        sock.connect((host, int(port)))
#        except:
#            print("\n\nCould not connect to server :-(.\nPlease verify the URL and the internet.\nThen connection and try again.")
            
#            input("Enter to continue")
#            continue
        
        request = f"{method} {URI} HTTP/1.1\r\nHost: {host + ":" + port}\r\nConnection: close\r\n"
        print(sock.send(request.encode(errors="strict")))
        
        # response = b''
        # while True:
        #     buf = sock.recv(4096) 
        #     if not buf:
        #         break
        #     response += buf
            
        print(sock.recv(4096).decode())
        sock.close()

        input("Enter to continue")
        # Sun, 06 Nov 1994 08:49:37 GMT debo devolver esta fecha
        # pero debo aceptar tambien
        # Sunday, 06-Nov-94 08:49:37 GMT
        # Sun Nov  6 08:49:37 1994
"""
def request(method, URL, headers, body):
    host, port, URI = parseURL(URL)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    request = f"{method} {URI} HTTP/1.1\r\nHost: {host + ":" + port}\r\n"
    
    for key, value in headers:
        request += f"{key}: {value}\r\n"
    
    if len(headers) == 0:
        request += "\r\n"    
    
    print(sock.send(request.encode(errors="strict")))
    
    print(sock.recv(4096).decode())
    sock.close()

def parseURL(URL): #(TODO) ver si se peude parsear con urllib.parse
    if(re.match("^http://[a-zA-Z0-9.-]+:[0-9]+/?", URL)):
        host, port = URL.split("/", 3)[2].split(":")
        URI = URL.split("/", 3)[3]
        return host, port, URI
    if(re.match("^http://[a-zA-Z0-9.-]+/?", URL)):
        host = URL.split("/", 3)[2]
        port = "80"
        URI = URL.split("/", 3)[3] if len(URL.split("/", 3)) == 4 else "/"
        return host, port, URI
    
    firstSlash = len(URL) if (URL.find("/") == -1) else URL.find("/")
    firstColon = firstSlash if (URL.find(":") == -1) else URL.find(":")

    host = URL[:firstColon]
    port = "80" if(firstColon ==  firstSlash) else URL[firstColon + 1:firstSlash]
    URI = "/" if(firstSlash == len(URL)) else URL[firstSlash:] 
    
    return host, port, URI

parseURL("http://www.google.com:80/adwd/ad/awd/aw")