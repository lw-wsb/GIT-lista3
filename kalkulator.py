def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b == 0:
        raise ValueError("nie mozna dzielic przez 0")
    return a / b

if __name__ == "__main__":
    print("Testowanie")
    print(dodawanie(5, 5))
    print(odejmowanie(10, 2))
    print(mnozenie(50, 3))
    print(dzielenie(25, 5))