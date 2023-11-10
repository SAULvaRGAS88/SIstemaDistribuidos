import rpyc

class Servidor(rpyc.Service):
    def on_connect(self, conn):
        self.matricula = 123
        self.senha = 123

    def on_disconnect(self, conn):
        pass

    def exposed_validacao(self, matricula, senha):
        if self.matricula == matricula and self.senha == senha:
            return True
        return False

    def exposed_conta(self, pedido):
        saldo = 100
        if pedido == 1:
            compra = 10
            if saldo >= compra:
                resultado = saldo - compra
                return f"Saldo atual: {resultado}"
        elif pedido == 2:
            compra = 3
            if saldo >= compra:
                resultado = saldo - compra
                return f"Saldo atual: {resultado}"
        elif pedido == 3:
            compra = 2
            if saldo >= compra:
                resultado = saldo - compra
                return f"Saldo atual: {resultado}"

    def exposed_menu(self):
        return """
            1-Hamburger - R$ 10,00.
            2-Refrigerante - R$ 3,00.
            3-Batata Frita - R$ 2,00.
            Digite sua escolha: """

    def exposed_pedido(self, escolha):
        if escolha == 1:
            return "Você selecionou a opção 1: Hamburguer"
        elif escolha == 2:
            return "Você selecionou a opção 2: Refrigerante"
        elif escolha == 3:
            return "Você selecionou a opção 3: Batata frita"
        else:
            return "Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3)"

def main():
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(Servidor, port=4040)
    t.start()

if __name__ == '__main__':
    main()

