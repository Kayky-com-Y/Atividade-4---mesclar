class no():
    def __init__(self, item, posterior = None, anterior = None):
        self.item = item
        self.posterior = posterior
        self.anterior = anterior
    
class fila():
    def __init__(self, primeiro = None,):
        self.__lista = primeiro
        self.__valor_atual = primeiro

    def Reset(self):
        self.__valor_atual = self.__lista
        return

    def ObterValor(self):
        return (self.__valor_atual)

    def ObterProximo(self, nó):
        if nó.posterior == None:
            return
        self.__valor_atual = nó.posterior
        return (self.__valor_atual)

    def AvançarProximo(self):
        if self.__valor_atual.posterior == None:
            return None
        self.__valor_atual = self.__valor_atual.posterior
        return (self.__valor_atual)
    
    def Buscar(self, nó):
        if self.__lista == None:
            return False
        else:
            self.__valor_atual = self.__lista
        while True:
            if self.__valor_atual == nó:
                return True
            if self.__valor_atual.posterior != None:
                self.__valor_atual = self.__valor_atual.posterior
            else:
                break
        return False

    def Tamanho(self):
        quantidade:int = 0
        if self.__lista == None:
            return 0
        else:
            self.__valor_atual = self.__lista
        while True:
            quantidade+=1
            if self.__valor_atual.posterior != None:
                self.__valor_atual = self.__valor_atual.posterior
            else:
                break
        return quantidade
    def MostrarALL(self):
        print("[", end="")
        self.__valor_atual = self.__lista
        if self.__lista == None:
            return print("]")
        else:
            self.__valor_atual = self.__lista
        quantidade:int = 0
        while True:
            quantidade +=1
            print(f"{self.__valor_atual.item}", end="")
            if self.__valor_atual.posterior != None:
                print(", ", end="")
                self.__valor_atual = self.__valor_atual.posterior
            else:
                break
        self.__valor_atual = self.__lista
        print("]")
        return

    def InserirAgrupado(self, nó):
        if self.__lista == None:
            self.__lista = nó
            return ("Nó adicionado como primeiro da fila")
        if self.Buscar(nó):
            return("Esse Nó ja foi adicionado a fila")
        self.__valor_atual = self.__lista 
        while True:
            if self.__valor_atual.item >= nó.item and self.__valor_atual.posterior == None:
                self.__valor_atual.posterior = nó
                return ("Nó adicionado ao final da fila")
            elif self.__valor_atual.item < nó.item and self.__valor_atual.posterior == None:
                nó.posterior = self.__lista
                self.__lista = nó
                return ("Nó adicionado ao inicio da fila")
            elif self.__valor_atual.item < nó.item and self.__lista == self.__valor_atual:
                nó.posterior = self.__lista
                self.__lista = nó
                return ("Nó adicionado ao inicio da fila")
            elif self.__valor_atual.item == nó.item:
                nó.posterior = self.__valor_atual.posterior
                self.__valor_atual.posterior = nó
                return ("Nó adicionado a fila")
            elif self.__valor_atual.posterior.item < nó.item:
                nó.posterior = self.__valor_atual.posterior
                self.__valor_atual.posterior = nó
                return ("Nó adicionado a fila")
            else:
                self.__valor_atual = self.__valor_atual.posterior

    def Destrutor(self, nó):
        if self.Buscar(nó) == False:
            return ("Nó não existe")
        self.__valor_atual = self.__lista
        item = nó.item
        if self.__valor_atual == nó:
            self.__lista = nó.posterior
            self.__valor_atual = self.__lista
            del(nó)
            return (f"O nó com os valores {item} foi excluido")
        while True:
            if self.__valor_atual.posterior == None:
                return ("Nó nao foi encontrado")
            elif self.__valor_atual.posterior == nó:
                self.__valor_atual.posterior = nó.posterior
                del(nó)
                break
            else:
                self.__valor_atual = self.__valor_atual.posterior
        return (f"O nó com o valor {item} foi excluido")

class Mesclar(fila):
    def __init__(self):
        super().__init__()
    def merge_two_lists(self, lista1: fila, lista2: fila):
        lista1.Reset()
        lista2.Reset()
        lista1ValorAtual = lista1.ObterValor()
        if lista1ValorAtual != None:
            while True:
                self.InserirAgrupado(no(lista1.ObterValor().item))
                proximo = lista1.ObterProximo(lista1ValorAtual)
                if proximo != None:
                    lista1ValorAtual = proximo
                else:
                    break
        lista1.Reset()
        lista2ValorAtual = lista2.ObterValor()
        if lista2ValorAtual == None:
            return
        while True:
            self.InserirAgrupado(no(lista2.ObterValor().item))
            proximo = lista2.ObterProximo(lista2ValorAtual)
            if proximo != None:
                lista2ValorAtual = proximo
            else:
                break
        lista2.Reset()
        return

lista1 = fila()
lista2 = fila()
mesclagem = Mesclar()


while True:
    print("--------Essa é a primeira lista, crie seus conponentes------")
    print(f"Vc tem uma lista com {lista1.Tamanho()} nós")
    escolha = int(input("Digite 1 para continuar ou 0 para parar: "))
    if lista1.Tamanho() >= 50:
        print("Sua lista já exedeu o limite de 50 nós")
        input("Tecle enter para continuar")
        break 
    if escolha == 1:
        numero = int(input("digite um numero para ser adicionado a sua lista. Lembrese. Ele não pode ser menor que -100 ou maior que 100 e vc tem o limite de 50 nós para sua lista"))
        if numero < -100 or numero > 100:
            print(f"O numero {numero} não é aceito segundos as regras")
            input("Tecle enter para continuar")
        else:
            NovoNo = no(numero)
            lista1.InserirAgrupado(NovoNo)
    else:
        input("Tecle enter para continuar")
        break
while True:
    print("--------Essa é a segunda lista, crie seus conponentes------")
    print(f"Vc tem uma lista com {lista2.Tamanho()} nós")
    escolha = int(input("Digite 1 para continuar ou 0 para parar: "))
    if lista2.Tamanho() >= 50:
        print("Sua lista já exedeu o limite de 50 nós")
        input("Tecle enter para continuar")
        break 
    if escolha == 1:
        numero = int(input("digite um numero para ser adicionado a sua lista. Lembrese. Ele não pode ser menor que -100 ou maior que 100 e vc tem o limite de 50 nós para sua lista"))
        if numero < -100 or numero > 100:
            print(f"O numero {numero} não é aceito segundos as regras")
            input("Tecle enter para continuar")
        else:
            NovoNo = no(numero)
            lista2.InserirAgrupado(NovoNo)
    else:
        input("Tecle enter para continuar")
        break

mesclagem.merge_two_lists(lista1, lista2)
print("Na Primeira lista voce colocou:")
lista1.MostrarALL()
print("Na Segunda lista voce colocou:")
lista2.MostrarALL()
print("Mesclando as duas listas, ficou assim:")
mesclagem.MostrarALL()
    