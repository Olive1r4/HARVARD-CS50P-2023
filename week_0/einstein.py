def main():
    # Recebe um numero inteiro
    m = int(input("m: "))
    print(f"E: {emc2(m)}")

def emc2(m):
    # Retorna o valor da energia
    return m * (pow(300000000, 2))
main()
