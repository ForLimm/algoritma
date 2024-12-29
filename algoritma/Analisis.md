1.Bubble Sort:
Kompleksitas:
- Waktu: O(n²) karena dua loop bersarang.
- Ruang: O(1) karena menggunakan sorting in-place.
Proses: Mengiterasi array, membandingkan elemen berpasangan, dan menukar jika tidak sesuai urutan. Ulangi hingga array terurut.

2.Merge Sort:
Kompleksitas:
- Waktu: O(n log n) karena pembagian array berulang dan penggabungan.
- Ruang: O(n) karena menggunakan array tambahan (rekursi).
Proses: Rekursif membagi array hingga tersisa elemen tunggal, lalu menggabungkannya kembali dalam urutan terurut.

Perbandingan Waktu Eksekusi:
- Bubble Sort lebih lambat untuk dataset besar karena O(n²).
- Merge Sort lebih efisien untuk dataset besar karena O(n log n).