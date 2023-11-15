# Potenciação Remota - Exemplo Pyro

Este exemplo é voltado para trabalhar com objetos distribuídos para a disciplina Sistemas Distribuídos. 
Nesse exemplo, criamos um objeto distribuído (Math) com um método voltado para realizar a potenciação (pow). 
Esse método contém dois parâmetros: base e expoente.

Para iniciar a execução, instale primeiro a biblioteca Pyro:
> pip3 install pyro4

*Nota: Se não tiver acesso a administrador na máquina, adicione no final "--user"*

Em seguida, instancie o Name Server. O Name Server é o responsável por acessar a referência do objeto remoto (lembram da analogia: serviço com tabelão com nome e referência dos objetos distribuídos).
Para instanciá-lo, precisamos:
> python -m Pyro4.naming -n 0.0.0.0

Por fim, em outros terminais, instanciamos o servidor e o cliente:
> python server.py

> python client.py