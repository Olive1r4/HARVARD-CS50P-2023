def main():
    x = int(input("x = "))
    print(f"o quadrado de {x} é {quadrado(x)}")

def quadrado(x):
    return pow(x, 2)

main()
