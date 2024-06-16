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
    print("start")
