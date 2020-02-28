import socket
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
cs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host, port = '127.0.0.1', 5555

cs.connect((host, port))
print("Clint connected on {}:{} ...".format(host, port))
try:
	while True:
		msg1 = raw_input("Choose Country:")
		cs.send(str(msg1).encode())

		msg2 = input("First Number:")
		cs.send(repr(msg2).encode('utf-8'))
		
		msg3 = input("Second Number:")
		cs.send(repr(msg3).encode('utf-8'))

		data = cs.recv(512).decode()
		print("Result >>> {}".format(data))

except KeyboardInterrupt:
	cs.close()
