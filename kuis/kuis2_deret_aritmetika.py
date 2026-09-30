# Kuis 2: Menghitung Deret Aritmetika
print("Deret Aritmetika")
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

# Validasi input n harus positif menggunakan while
while n <= 0:
    print("n harus bilangan bulat positif.")
    n = int(input("Banyak suku n: "))

total = 0
for i in range(n):
    suku = a + (i * d)
    total += suku
    print(f"Suku ke-{i + 1}: {suku:.2f}")

print(f"Jumlah = {total:.2f}")