import Pyro4 as pyro
@pyro.expose

class Servidor():
    def __init__(self):
        self.matricula = 123
        self.senha = 123

    def validacao(self, matricula, senha):
        if self.matricula == matricula and self.senha == senha:
            return True
        

    def menu(self):
        return """
            1-Hamburger.
            2-Refrigerante.
            3-Batata Frita.
            Digite sua escolha: """
    

# class Cliente():
#     def __init__(self):
#         self.matricula = 123
#         self.senha = 123
#         self.menu = Menu()
#         self.menu = {
#             "1": "Pizza",
#             "2": "Hambúrguer",
#             "3": "Sushi"
#         }

#     def validacao(self, matricula, senha):
#         if self.matricula == matricula and self.senha == senha:
#             print("Validação ok!")
#             return self.menu
#         return "Senha Errada"
    

    
# class Menu():
#     def cardapio(self):
    
#         if escolha == 1:
#             return "Você selecionou a opção 1: Hamburguer"
#         elif escolha == 2:
#             return "Você selecionou a opção 2: Refrigerante"
#         elif escolha == 3:
#             return "Você selecionou a opção 3: Batata frita"
#         else:
#             return "Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3)"
       

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