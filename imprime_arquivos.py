import sys

if len(sys.argv) < 2:
    print("Usagem: imprime_arquivos.py [arquivo 1] [arquivo 2] ... [arquivo n]")
    return 1
for i in range(1, len(sys.argv)):
    with open("sys.argv[i]", "r") as arquivo:
        print(arquivo.read())
