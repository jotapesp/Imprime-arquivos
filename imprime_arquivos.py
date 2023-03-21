import sys

if len(sys.argv) < 2:
    print("Usagem: imprime_arquivos.py [arquivo 1] [arquivo 2] ... [arquivo n]")

try:
    for i in range(1, len(sys.argv)):
        with open(sys.argv[i], "r") as arquivo:
            print(f" {sys.argv[i]} ".center(80, "="))
            print(arquivo.read())
except FileNotFoundError:
    print("".center(80, "="))
    print(f"Erro: arquivo {sys.argv[i]} não foi encontrado.")
