import rpyc
from rpyc.utils.server import ThreadedServer
class Math(rpyc.Service):
    def on_connect(self,conn):
        pass
    def on_disconnect(self,conn):
        pass
    def exposed_pow(self,base,exp):
        return pow(base, exp)
if __name__ == '__main__':
    ts = ThreadedServer(Math,port=4040)
    print('Service started on port 4040')
    ts.start()
