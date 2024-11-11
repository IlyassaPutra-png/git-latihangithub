#uts6
#menambahkan rumus prima
N = int(input("Masukkan nilai N = "))
numbers = []
for i in range(N):
    number = int(input(f"Masukkan bilangan ke-{i + 1} = "))
    numbers.append(number)

angka = 0

for num in numbers:
    if num > 1:  
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            angka += num
        else:
            print("tidak ada bilangan prima")
print(f"jumlah bilangan prima adalah{angka}")

