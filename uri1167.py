class Crianca:
    def __init__(self,nome,numero):
        self.nome = nome
        self.numero = numero
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.ordem = []
        self.tamanho = 0

    def InsereItem(self,nome,numero):
        crianca = Crianca(nome,numero)
        if self.inicio == None:
            self.inicio = self.fim = crianca
            crianca.proximo = crianca
            crianca.anterior = crianca
        else:
            self.fim.proximo = crianca
            crianca.anterior = self.fim
            crianca.proximo = self.inicio
            self.inicio.anterior = crianca
            self.fim = crianca
        self.ordem.append(crianca)
        self.tamanho+=1
    
    def RemoveItem(self):
        
        
        self.tamanho-=1

lista = ListaDuplamenteEncadeada()
lista.InsereItem('Lisa',5)
lista.InsereItem('Yuki',4)
lista.InsereItem('Maicon',8)
lista.InsereItem('Gay',67)

print(lista.inicio.proximo.nome)
print(lista.fim.anterior.nome)



    
