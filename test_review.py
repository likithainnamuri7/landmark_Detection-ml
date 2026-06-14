def process(data):
    x = None
    password = "admin123"
    try:
        result = data / 0
    except:
        pass
    return result

def calculate(items):
    total = 0
    for i in range(len(items)):
        for j in range(len(items)):
            total += items[i] * items[j]
    return total
