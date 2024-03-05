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

fila_de_pesquisa = deque()
fila_de_pesquisa += grafo["voce"]

def pessoa_e_vendedor(nome):
    return nome[-1] == "m"

encontrou_vendedor = False

while fila_de_pesquisa:
    pessoa = fila_de_pesquisa.popleft()
    if pessoa_e_vendedor(pessoa):
        print(pessoa + " é um vendedor de manga!")
        encontrou_vendedor = True
        break
    else:
        fila_de_pesquisa += grafo[pessoa]

if not encontrou_vendedor:
    print("Não foi encontrado um vendedor de manga na rede de contatos.")

