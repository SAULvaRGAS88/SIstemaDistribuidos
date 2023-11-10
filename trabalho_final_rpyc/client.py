import rpyc

if __name__ == '__main__':
    conn = rpyc.connect('localhost', 4040)  # Altere a porta conforme necessário
    math = conn.root

    print("Digite sua Matrícula e Senha")
    matricula = int(input("Matrícula: ").strip())
    senha = int(input("Senha: ").strip())

    if math.exposed_validacao(matricula, senha):
        menu = math.exposed_menu()
        print(menu)

        resp = int(input())
        verificaSaldo = math.exposed_conta(resp)
        result = math.exposed_pedido(resp)
        print(result)
        print(verificaSaldo)
    else:
        print("Login incorreto")
        exit()
