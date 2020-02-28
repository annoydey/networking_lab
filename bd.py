import socket
bds = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
bds.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host, port = '127.0.0.1', 6001

bds.bind((host, port))
print("BD Server connected on {}:{} ...".format(host, port))
bds.listen(2)
try:
	ds, addr = bds.accept()
	print("Client connected on {}".format(addr))
	while True:
		x = ds.recv(512).decode()
		print("First Number : {}".format(x))
		y = ds.recv(512).decode()
		print("Second Number : {}".format(y))
		a = int(x)
		b = int(y)
		temp = a + b
		ds.send(str(temp).encode())
		print("Sent")
		break
except KeyboardInterrupt:
	cs.close()
