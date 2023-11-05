import Pyro4 as pyro

if __name__ == '__main__':
    uri = "PYRONAME:Cantina@localhost:9090"
    math = pyro.Proxy(uri) 
    print("Digite sua Matrícula e Senha")
   
    matricula = int(input("Matrícula: " ).strip())
    senha = int(input("Senha: " ).strip())
    if math.validacao(matricula, senha):
        menu = math.menu()
        print(menu)

        resp = input()
   
    # result = math.validacao(matricula, senha)
    # print('Pedido: {}'.format(result))

