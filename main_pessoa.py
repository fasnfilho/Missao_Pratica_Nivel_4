# main_pessoa.py
from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

# Cria e imprime a instância da Pessoa
pessoa1 = Pessoa("Ana", "123456", "2023-09-01")
pessoa1.mostrarResultado()

# Cria e imprime a instância da PessoaFisica
pessoa_fisica = PessoaFisica("Carlos", "654321", "2023-09-01", "111.222.333-44", "MG-123456", True)
pessoa_fisica.mostrarResultado()

# Cria e imprime a instância da PessoaJuridica
pessoa_juridica = PessoaJuridica("Empresa X", "789012", "2023-09-01", "12.345.678/0001-99", "2023-01-01", True)
pessoa_juridica.mostrarResultado()
