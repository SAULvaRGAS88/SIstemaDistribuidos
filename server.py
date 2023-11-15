import Pyro4 as pyro
@pyro.expose

class Servidor():
    def __init__(self):
        self.matricula = 123
        self.senha = 123

    def validacao(self, matricula, senha):
        if self.matricula == matricula and self.senha == senha:
            return True
        return False

    def conta(self, pedido):
        saldo = 100
        if pedido == 1:
            compra = 10
            if saldo >= compra:
                resultado = saldo - compra
                return f"Saldo atual: {resultado}"
        if pedido == 2:
            compra = 3
            if saldo >= compra:
                resultado = saldo - compra
                return f"Saldo atual: {resultado}"
        if pedido == 3:
            compra = 2
            if saldo >= compra:
                resultado = saldo - compra
                return f"Saldo atual: {resultado}"

    def menu(self):
        return """
            1-Hamburger - R$ 10,00.
            2-Refrigerante - R$ 3,00.
            3-Batata Frita - R$ 2,00.
            Digite sua escolha: """
    
    def pedido(self, escolha):
        if escolha == 1:
            return "Você selecionou a opção 1: Hamburguer"
        elif escolha == 2:
            return "Você selecionou a opção 2: Refrigerante"
        elif escolha == 3:
            return "Você selecionou a opção 3: Batata frita"
        else:
            return "Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3)"
       

def main():
    server = Servidor()
    daemon = pyro.Daemon()
    ns = pyro.locateNS(host="localhost",port=4040)
    uri = daemon.register(server)
    ns.register('Cantina',uri)
    print('Object Remote : ',uri)
    daemon.requestLoop()
if __name__ == '__main__':
    main()