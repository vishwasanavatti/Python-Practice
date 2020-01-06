import threading

class Message(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x=Message(name='Send out Message')
y=Message(name='Receive a Message')
z=Message(name='Nothing')

x.start()
y.start()
z.start()