import socket
import pickle

#PEGANDO DADOS DO LADO DO CLIENTE
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050
SERVER = "192.168.1.26"
ADDR = (SERVER, PORT)

client = socket.socket(socket.af_INET, socket.SOCK_STRAM)
client.connect(ADDR)

#definindo mensagem de comunicacao com o servidor
def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length),encode(FORMAT)
	send_length += " "* (HEADER - len(send_legth))
	client.send(send_legth)
	client.send(message)
	print(client.recv(2048)).decode(FORMAT)

send("HELLO WORD")
input()
send("HELLO EVERYONE")
send("HELLO MATHEUS")
input()
send(DISCONNECT_MESSAGE)

