class Pessoa():
    def __init__(self, nome, idade, peso):
        self.comida = None
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.acao = "None"

    def comer(self):
        if self.acao == "None":
            self.comida = input("Digite a comida que pode comer. \n- ")
            print(f'{self.nome} está comendo {self.comida}.')
            self.acao = "Comendo"
        else:
            print(f"Não pode realizar essa ação pois {self.nome} ainda está {self.acao}.")

    def falar(self):
        if self.acao == "None":
            frase = input("Digite a frase que ele quer falar.\n-")
            print(f"{self.nome} disse: {frase}")
            self.acao = "Falando"
        else:
            print(f"Não pode realizar essa ação pois {self.nome} ainda está {self.acao}.")

    def dormir(self):
        if self.acao == "None":
            print(f'{self.nome} foi pra cama dormir.')
            self.acao = "Dormindo"
        else:
            print(f"Não pode realizar essa ação pois {self.nome} ainda está {self.acao}.")

    def andar(self):
        if self.acao == "None":
            self.lugar = input("Para onde ele vai? \n-")
            print(f'{self.nome} está caminhando para {self.lugar}.')
            self.acao = "Andando"
        else:
            print(f"Não pode realizar essa ação pois {self.nome} ainda está {self.acao}.")

    def pararacao(self):
        if self.acao == "Comendo":
            print(f"{self.nome} terminou de comer {self.comida}")
        elif self.acao == "Dormindo":
            print(f"{self.nome} acordou depois de 8 longas horas de sono.")
        elif self.acao == "Falando":
            print(f"{self.nome} terminou de falar.")
        elif self.acao == "Andando":
            print(f"{self.nome} chegou a {self.lugar}.")
        self.acao = "None"

    def opcoes(self):
        print(f"LIFE BASICS"
              f"\n comer - Fazer {self.nome} comer uma comida da escolha."
              f"\n falar - Fazer {self.nome} comer uma comida da escolha."
              f"\n dormir - Fazer {self.nome} ir pra cama dormir."
              f"\n andar - Fazer {self.nome} ir para algum lugar"
              f"\n terminar - Fazer {self.nome} terminar a ação desejada."
              f"\n Personagem - Mostra as características do personagem."
              f"\n opcoes - Mostrar as suas opções"
              f"\n Sair - Sair do desafio."
              f"\n{self.nome} É um cara muito simples, portanto ele só faz 1 coisa de cada vez.")

    def personagem(self):
        print(f"Nome: {self.nome}"
              f"\nIdade: {self.idade} anos"
              f"\nPeso: {self.peso}KG.")

    def menu(self, choice):
        if choice in "comer,Comer":
            print()
            self.comer()
            print()
        elif choice in "falar,Falar":
            print()
            self.falar()
            print()
        elif choice in "Dormir" or choice == "dormir":
            print()
            self.dormir()
            print()
        elif choice in "Andar, andar":
            self.andar()
        elif choice in "Terminar,terminar":
            print()
            self.pararacao()
            print()
        elif choice in "Opcoes,opcoes,Opçoes,opçoes,Opcões,opcões,Opções,opções":
            self.opcoes()
        elif choice in ("personagem,Personagem,perso,Perso"):
            self.personagem()
        elif choice in "sair,Sair":
            print("Obrigado por Jogar!")
        else:
            print("Não reconheço esse comando.")
