# Pertemuan 05 Perulangan Python

**Nama:** Eka Elsanti  
**NIM:** 2225250059  
**Kelas:** 3A  

---

## Tujuan
Menggunakan `for` dan `while` untuk menyelesaikan masalah iteratif, melakukan validasi input berulang, serta mengakulasi nilai pada deret bilangan.

---

## Cara Menjalankan
Jalankan perintah berikut di terminal:
```bash
python3 kuis/kuis2_deret_aritmetika.py

```

---

## Algoritma Kuis 2

1. Membaca input nilai suku pertama (`a`) dan beda (`d`) bertipe desimal.
2. Membaca input banyak suku (`n`) bertipe bulat.
3. Melakukan validasi berulang menggunakan `while` jika `n <= 0` hingga pengguna memasukkan `n` positif.
4. Menginisialisasi variabel `total = 0`.
5. Menggunakan `for` dengan `range(n)` untuk menghitung suku ke-`i` (`suku = a + i * d`), menampilkan setiap suku, dan menambahkan nilai suku ke `total`.
6. Menampilkan hasil penjumlahan seluruh suku (`total`) dengan format 2 desimal.

---

## Hasil Pengujian Kuis 2

| a | d | n | Suku | Jumlah Diharapkan | Jumlah Aktual | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 3 | 5 | 2.00, 5.00, 8.00, 11.00, 14.00 | 40.00 | 40.00 | Sesuai |
| 10 | -2 | 4 | 10.00, 8.00, 6.00, 4.00 | 28.00 | 28.00 | Sesuai |
| 1.5 | 0.5 | 3 | 1.50, 2.00, 2.50 | 6.00 | 6.00 | Sesuai |

---

## Refleksi

Kesalahan umum pada perulangan adalah menempatkan inisialisasi variabel akumulator (`total = 0`) di dalam badan *loop*. Hal tersebut membuat nilai total selalu ter-reset ke 0 setiap kali iterasi berjalan. Penempatan `total = 0` harus berada di luar (sebelum) perulangan agar akumulasi berjalan dengan benar.