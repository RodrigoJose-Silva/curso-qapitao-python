# Este programa demonstra Programação Orientada a Objetos (POO) em Python
# POO permite criar classes que representam objetos do mundo real
# Classes são como moldes que definem características (atributos) e ações (métodos)

# Classe base (classe pai) que representa uma conta bancária genérica
class ContaBancaria:
    # Construtor: método especial executado automaticamente ao criar uma nova instância
    # __init__ inicializa os atributos da classe
    def __init__(self, titular, saldo):
        # self refere-se à instância atual do objeto
        self.titular = titular  # Armazena o nome do titular da conta
        self.saldo = saldo      # Armazena o saldo inicial da conta

    # Método para depositar dinheiro na conta
    def depositar(self, valor):
        # Soma o valor depositado ao saldo atual
        self.saldo = self.saldo + valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    # Método para consultar o saldo atual da conta
    def consultar_saldo(self):
        # Exibe o saldo atual formatado com 2 casas decimais
        print(f"Saldo atual de {self.titular} é de R$ {self.saldo:.2f}")
        
    
# Classe filha que herda de ContaBancaria (herança)
# ContaCorrente herda todos os atributos e métodos de ContaBancaria
class ContaCorrente(ContaBancaria):
    # Método específico para conta corrente: saque com taxa
    def sacar(self, valor):
        taxa = 2  # Taxa fixa de R$ 2,00 para cada saque
        total = valor + taxa  # Calcula o valor total a ser debitado

        # Verifica se há saldo suficiente para o saque com a taxa
        if total > self.saldo:
            print("Saldo insuficiente para saque.")
        else:
            # Subtrai o valor total (saque + taxa) do saldo
            self.saldo = self.saldo - total
            print(f"Saque de R$ {valor:.2f} realizado com sucesso, com a taxa de R$ {taxa:.2f} de saque aplicada.")


# Outra classe filha que também herda de ContaBancaria
# ContaPoupanca também herda atributos e métodos, mas tem comportamento diferente
class ContaPoupanca(ContaBancaria):
    # Método específico para conta poupança: saque sem taxa
    def sacar(self, valor):
        # Verifica se há saldo suficiente
        if valor > self.saldo:
            print("Saldo insuficiente para saque.")
        else:
            # Subtrai apenas o valor do saque, sem taxa
            self.saldo = self.saldo - valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

# Criando instâncias (objetos) das classes
# Instanciar significa criar um objeto real a partir da classe

# Criando uma conta poupança para Ana com saldo inicial de R$ 1000,00
conta1 = ContaPoupanca("Ana", 1000)

# Criando uma conta poupança para Bruno com saldo inicial de R$ 500,00
conta2 = ContaPoupanca("Bruno", 500)

# Testando operações na conta de Ana
conta1.consultar_saldo()  # Consulta o saldo atual
conta1.depositar(250)     # Deposita R$ 250,00
conta1.consultar_saldo()  # Consulta o saldo após o depósito
conta1.sacar(1000)        # Tenta sacar R$ 1000,00
conta1.consultar_saldo()  # Consulta o saldo após o saque

# Testando operações na conta de Bruno
conta2.consultar_saldo()  # Consulta o saldo atual
conta2.sacar(600)         # Tenta sacar R$ 600,00 (mais que o saldo disponível)
conta2.consultar_saldo()  # Consulta o saldo após tentativa de saque

# Repetindo testes para demonstrar o comportamento
conta1.consultar_saldo()
conta1.depositar(250)
conta1.consultar_saldo()
conta1.sacar(1000)
conta1.consultar_saldo()

conta2.consultar_saldo()
conta2.sacar(600)  
conta2.consultar_saldo() 