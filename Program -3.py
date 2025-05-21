def generate_series(a: int):
    
    if a % 2 == 0:
        a -= 1
    series = [i for i in range(1, a + 1, 2)]
    return seri
a = int(input("Enter a number: "))
result = generate_series(a)
print("Output:", ", ".join(map(str, result)))