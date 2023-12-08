import Pyro4 as pyro
@pyro.expose

class Servidor():
    def __init__(self):
        self.matricula = 123
        self.senha = 123
        self.saldo = 100
        self.produtos_escolhidos = []

    def validacao(self, matricula, senha):
        if self.matricula == matricula and self.senha == senha:
            return True
        return False
    
    def consulta_saldo(self):
        return f"Saldo atual: R${self.saldo}"
    
    def menu(self):
        return """
            1-Hamburger - R$ 10,00.
            2-Refrigerante - R$ 3,00.
            3-Batata Frita - R$ 2,00.
            0-Finalizar.
            Digite sua escolha: """

    def conta(self, escolha):
        if escolha == 0:
            resultado = [f"Pedido finalizado. Seu saldo é: R$ {self.saldo}"]
            if self.produtos_escolhidos:
                resultado.append("Produtos adquiridos: ")
                for produto in self.produtos_escolhidos:
                    resultado.append(produto)
            return resultado
        
        resultados = []
        if escolha in [1, 2, 3]:
            produto, preco = self.produtos(escolha)
            compra = preco
            if self.saldo >= compra:
                self.saldo -= compra
                self.produtos_escolhidos.append(f"{produto} - R$ {preco:.2f}")
                resultados.append(f"{produto} - R$ {preco:.2f} - Saldo atual: R$ {self.saldo}")
            else:
                resultados.append(f"Saldo insuficiente")
        else:
            resultados.append("Opção inválida. Por favor, escolha uma opção válida.")
        
        return resultados
    
    def produtos(self, escolha):
        produtos = {
            1: ("Hamburguer", 10.00),
            2: ("Refrigerante", 3.00),
            3: ("Batata frita", 2.00),
        }
        return produtos[escolha]

def main():
    server = Servidor()
    daemon = pyro.Daemon()
    ns = pyro.locateNS(host="localhost",port=9090)
    uri = daemon.register(server)
    ns.register('Cantina',uri)
    print('Object Remote : ',uri)
    daemon.requestLoop()
if __name__ == '__main__':
    main()