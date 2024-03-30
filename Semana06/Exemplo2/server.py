import socket
import threading

#Pegando a porta do servidor
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050
#SERVER = "198.168.100.33"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#Definindo a funcao para conetar e iniciar o servidor
def handle_client(conn, addr):
	print("[NEW CONNECTION] {addr} connected.")
	connected = True
	while connected:
		msg_length = conn.recv(HEADER).decode(FORMAT)
		if msg_length: 
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)
			if msg == DISCONNECT_MESSAGE:
				connected = False
			print("[{addr}] {msg}")
			conn.send("Msg Received".encode(FORMAT))
	conn.close()

def start():
	server.listen()
	print("[LISTENING] Server is listening on {SERVER}"
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		print("[ACTIVE CONNECTIONS] {threading.activeCount() -1}")


print("[STARTING] server is starting....")
start()







