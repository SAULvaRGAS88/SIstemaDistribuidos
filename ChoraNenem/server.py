import Pyro4 as pyro
@pyro.expose
class Menu():
     def cardapio(self, valor):
        if valor == 1:
            print("Você selecionou a opção 1: Hamburguer")
        elif valor == 2:
            print("Você selecionou a opção 2: Refrigerante")
        elif valor == 3:
            print("Você selecionou a opção 3: Batata frita")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3)")
        return valor

def main():
    server = Menu()
    daemon = pyro.Daemon()
    ns = pyro.locateNS(host="localhost",
                       port=9090)
    uri = daemon.register(server)
    ns.register('Cantina',uri)
    print('Object Remote : ',uri)
    daemon.requestLoop()
if __name__ == '__main__':
    main()