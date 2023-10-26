import Pyro4 as pyro
import sys
import os
@pyro.expose
class Math(object):
    def pow(self,a,b):
        print('{} ^ {} '.format(a,b))
        return pow(int(a),int(b))
def main():
    server = Math()
    daemon = pyro.Daemon()
    ns = pyro.locateNS(host="localhost",
                       port=9090)
    uri = daemon.register(server)
    ns.register('Mathar',uri)
    print('Object Remote : ',uri)
    daemon.requestLoop()
if __name__ == '__main__':
    main()