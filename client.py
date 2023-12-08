import Pyro4 as pyro

if __name__ == '__main__':
    uri = "PYRONAME:Cantina@localhost:9090"
    math = pyro.Proxy(uri) 
    print("Digite sua Matrícula e Senha")
   
    matricula = int(input("Matrícula: " ).strip())
    senha = int(input("Senha: " ).strip())
    if math.validacao(matricula, senha):
        saldo_atual = math.consulta_saldo()
        print(saldo_atual)
        
        while True:
            menu = math.menu()
            print(menu)

            resp = int(input())
            resultados = math.conta(resp)
            
            for resultado in resultados:
                print(resultado)
            
            if resp == 0:
                break
    else:
        print("Login incorreto")
        exit()
    # result = math.validacao(matricula, senha)
    # print('Pedido: {}'.format(result))