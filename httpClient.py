import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

method = input("Enter the Method: ")
address = input("Enter the address: ")

firstSlash = len(address) if (address.find("/") == -1) else address.find("/")
firstColon = firstSlash if (address.find(":") == -1) else address.find(":")

host = address[:firstColon]
port = "80" if(firstColon ==  firstSlash) else address[firstColon + 1:firstSlash]
URI = "/" if(firstSlash == len(address)) else address[firstSlash:] 

print("host:", host, " port:", port, " URI:", URI)

sock.connect((host, int(port)))

# while True:
#         message = sock.recv(1024).decode()
#         print("Server:", message)

sock.send(message = f"{method} {URI} HTTP/1.1 Host: {host}")
sock.close()



# Sun, 06 Nov 1994 08:49:37 GMT debo devolver esta fecha
# pero debo aceptar tambien
# Sunday, 06-Nov-94 08:49:37 GMT
# Sun Nov  6 08:49:37 1994
# 
#
#
#
