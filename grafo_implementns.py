from collections import deque

grafo = {}
grafo["voce"] = ["alice", "bob", "clarie"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["clarie"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []


def pessoa_e_vendedor(nome):
    return nome[-1] == "m"

encontrou_vendedor = False

def pesquisa(nome):
    fila_de_pesquisa = deque
    fila_de_pesquisa += grafo[nome]
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendendot(pessoa):
                print (pessoa + "é um vendedor de manga!")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
        
    return False


pesquisa("voce")

