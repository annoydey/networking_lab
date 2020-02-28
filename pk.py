import socket
pks = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
pks.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host, port = '127.0.0.1', 6003

pks.bind((host, port))
print("sl Server connected on {}:{} ...".format(host, port))
pks.listen(2)
try:
	ds, addr = pks.accept()
	print("Client connected on {}".format(addr))
	while True:
		x = ds.recv(512).decode()
		print("First Number : {}".format(x))
		y = ds.recv(512).decode()
		print("Second Number : {}".format(y))
		a = int(x)
		b = int(y)
		temp = a/b
		ds.send(str(temp).encode())
		print("Sent")
		break
except KeyboardInterrupt:
	cs.close()
