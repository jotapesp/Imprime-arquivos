import sys
import os.path

if len(sys.argv) < 2:
    print("Usagem: imprime_arquivos.py [arquivo 1] [arquivo 2] ... [arquivo n]")

for i in range(1, len(sys.argv)):
    try:
        with open(sys.argv[i], "r") as arquivo:
            if os.path.isdir(sys.argv[i]):
                raise IsADirectoryError
            print(f" {sys.argv[i]} ".center(80, "="))
            print(arquivo.read())
    except FileNotFoundError:
        #print("".center(80, "="))
        print(f"Erro: arquivo '{sys.argv[i]}' não foi encontrado.")
    except IsADirectoryError:
        #print("".center(80, "="))
        print(f"Erro: '{sys.argv[i]}' é um diretório/pasta.")
    finally:
        print("".center(80, "="))
        #print("Programa encerrado.")
