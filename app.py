def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Тек сан болуы қажет")
    return a * b

if __name__ == "__main__":
    input_a = float(input("Бірінші санды енгізіңіз: "))
    input_b = float(input("Екінші санды енгізіңіз: "))  
    print("Нәтиже:", add(input_a, input_b))