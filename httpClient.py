import socket
from bs4 import BeautifulSoup as bs
import re
from http import cookies

#(TODO) anadir 100 status handler

methods = ["OPTIONS", "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "CONNECT"]

generalHeaders = ["Cache-Control", "Connection", "Date", "Pragma", "Trailer", "Transfer-Enconding", "Upgrade", "Via", "Warning"]
requestHeaders = ["Accept","Accept-Charset","Accept-Encoding","Accept-Language", "Authorization", "Expect", "From", "Host", "If-Match", "If-Modified-Since", "If-None-Match", "If-Range", "If-Unmodified-Since", "Max-Forwards", "Proxy-Authorization","Range", "Referer", "TE", "User-Agent" ]
entityHeaders = ["Allow", "Content-Encoding", "Content-Language","Content-Length", "Content-Location", "Content-MD5", "Content-Range", "Content-Type", "Expires", "Last-Modified"]

def request(method, URL, headers, body):
    #process URL
    host, port, URI = parseURL(URL) 
    
    #create and connect the socket to host
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(20)
    sock.connect((host, int(port)))
    
    #build the request
    request = f"{method} {URI} HTTP/1.1\r\nHost: {host + ":" + port}\r\n"
    
    for key, value in headers:
        request += f"{key}: {value}\r\n"
    if len(headers) == 0:
        request += "\r\n"
            
    print(f"[Request] {request}")
    
    #send the entire request
    bytesSend = 0
    while bytesSend < len(request):
        bytesSend += sock.send(request[bytesSend:].encode(errors="strict"))
    
    status, respHeaders, body, headersDict = "error", [], "", {}
    
    
    status, respHeaders, body, headersDict = receiveResponse(sock)
    #except:
     #   print("[error] check the url, or the intenet conection")
    
    #print(response)
    
    sock.close()
    return status, respHeaders, body

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

def receiveResponse(sock):
    
    headers = ""
    body = ""
    
    #receive the headers section of the response
    while True:
        buff = sock.recv(1)
        if not buff:
            break
        if headers.endswith('\r\n\r\n'):
            break
        headers += buff.decode()
        
    #get status code and reason phrase
    endOfStatus = headers.find("\r\n")
    status = headers[9:endOfStatus]

    #process headers
    headers = headers[endOfStatus+2:-4].split("\r\n")
    headersDic = {}
    
    for header in headers:
        key, value = header.split(": ", 1)
        key = key.lower()
        # if key == "Set-Cookie":  
        headersDic[key] = value

    headers = [header.split(": ", 1) for header in headers]
    print(headers)
    #case when no enconded
    if 'content-length' in headersDic:
        remaining = int(headersDic['content-length']) - len(body)
        
        while remaining > 0:
            print(remaining)
            data = sock.recv(min(remaining, 1024))
            if not data:
                break
            body += data.decode("ISO-8859-1")
            remaining -= len(data)
            
            print(len(data))
            
    else:
        try:
            body = ""
            while True:
                buff = sock.recv(1024)
                print(buff)
                if not buff:
                    break
                body += buff.decode("ISO-8859-1")
                
        except TimeoutError:
            print("TimeOut!")
                
    #print(headersDic)
    
    return status, headers, body, headersDic

"""
def parseCookie(cookieString):
    print(cookieString)
    splitedCookie = cookieString.split(";")
    cookie = []
    cookie += [splitedCookie[0].split("=")[0], splitedCookie[0].split("=")[0]]
    for parameter in splitedCookie:
        cookie += [parameter.split("=")[1]]
        
    print(cookie)
"""

def parseResponse(response):
    endOfStatus = response.find("\r\n")
    endOfHeaders = response.find("\r\n\r\n")
    
    status = response[9:endOfStatus]
    
    rawHeaders = response[endOfStatus+2:endOfHeaders]
    rawHeaders = rawHeaders.split("\r\n")
    headers = [rawHeader.split(":") for rawHeader in rawHeaders]
    
    body = response[endOfHeaders+4: ]
    body = bs(body).prettify()
    
    print("[Response] status:",status)

    return status, headers, body