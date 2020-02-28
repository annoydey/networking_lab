import socket
import time
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host, port = '127.0.0.1', 5555

ss.bind((host, port))
print("Agent listening on %s:%s ..."%(host, port))
ss.listen(2)
try:
	cs, addr = ss.accept()
	print("client connected on {}".format(addr))
	while True:
		c = cs.recv(512).decode()
		print("Choosen Country {}".format(c))
		x = cs.recv(512).decode()
		y = cs.recv(512).decode()
		
		data = str(c)
		data1 = int(x)
		data2 = int(y)

		ds = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
		ds.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		
		if data == "bd":
			print("For BD")
			ds.connect((host, 6001))
			print("Client listening on %s:%s ..."%(host, 6001))
			ds.send(repr(data1).encode('utf-8'))
			time.sleep(0.1)   
			ds.send(repr(data2).encode('utf-8'))
			data = ds.recv(512).decode()		
			cs.send(str(data).encode())
		elif data == "sl":
			print("For SL")
			ds.connect((host, 6002))
			print("Client listening on %s:%s ..."%(host, 6002))
			ds.send(repr(data1).encode('utf-8'))
			time.sleep(0.1)   
			ds.send(repr(data2).encode('utf-8'))
			data = ds.recv(512).decode()		
			cs.send(str(data).encode())
		elif data== "pk":
			print("For PK")
			ds.connect((host, 6003))
			print("Client listening on %s:%s ..."%(host, 6003))
			ds.send(repr(data1).encode('utf-8'))
			time.sleep(0.1)   
			ds.send(repr(data2).encode('utf-8'))
			data = ds.recv(512).decode()		
			cs.send(str(data).encode())
		ds.close()
		print("Operation Done")

except KeyboardInterrupt:
	cs.close()




