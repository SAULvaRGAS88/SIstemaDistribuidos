import Pyro4 as pyro

if __name__ == '__main__':
    uri = "PYRONAME:Cantina@localhost:9090"
    a = int(input("""
    Menu:
    1-Hamburguer.
    2-Refrigerante.
    3-Batata frita.
    """ ).strip())
    
    math = pyro.Proxy(uri) 
    result = math.cardapio(a) 
    print('Pedido: {}'.format(result))