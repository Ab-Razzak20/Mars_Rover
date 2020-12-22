import socket, thread

IP = socket.gethostname()
PORT = 5010

r = socket.socket()
r.bind((IP, 5001))
r.listen(5)
print "r"

s = socket.socket()
s.bind((IP, 5002))
s.listen(5)
print "s"

# while 1:
#
#     data = client_s.recv(1000)
#     print data
#
#     inp = raw_input("enter something--- ")
#     client_s.sendall(inp)


def R():
    client_r, client_addr = r.accept()
    print "connected r"

    while 1:
        data = client_r.recv(1000)
        print data


def S():

    client_s, client_addr = s.accept()
    print "connected s"

    while 1:
        inp = raw_input("enter something--- ")
        client_s.sendall(inp)


thread.start_new_thread(R, ())
thread.start_new_thread(S, ())


while 1:
    None