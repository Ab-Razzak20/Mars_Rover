import socket, time, thread

IP = socket.gethostname()
PORT = 5010

s = socket.socket()
r = socket.socket()
s.connect((IP, 5001))
r.connect((IP, 5002))


# while 1:
#
#     inp = raw_input("Enter== ")
#     s.sendall(inp)
#
#     data = s.recv(1000)
#     print data


def R():
    while 1:
        data = r.recv(1000)
        print data


def S():
    while 1:
        inp = raw_input("Enter== ")
        s.sendall(inp)


thread.start_new_thread(R, ())
thread.start_new_thread(S, ())


while 1:
    None
