def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Тек сан болуы қажет")
    return a * b

import random
if __name__ == "__main__":
    input_a = random.uniform(1, 10)  # Бірінші санды кездейсоқ генерациялау
    input_b = random.uniform(1, 10)  # Екінші санды кездейсоқ генерациялау
    print("Нәтиже:", add(input_a, input_b))