komentar = input("Masukkan komentar Anda tentang produk yang baru dibeli: ")

kata_positif = ["bagus", "puas", "cepat", "terjangkau", "memuaskan", "suka", "baik"]
kata_negatif = ["buruk", "kecewa", "lambat", "mahal", "mengecewakan", "tidak sesuai", "kurang", "kritik"]

def analisis_sentimen_berbasis_aturan(komentar):
    kata_kata = komentar.lower().split()

    jumlah_positif = sum(1 for kata in kata_kata if kata in kata_positif)
    jumlah_negatif = sum(1 for kata in kata_kata if kata in kata_negatif)

    if jumlah_positif > jumlah_negatif:
        return "Positif"
    elif jumlah_negatif > jumlah_positif:
        return "Negatif"
    else:
        return "Netral"

hasil_sentimen = analisis_sentimen_berbasis_aturan(komentar)
print(f"Hasil analisis sentimen untuk komentar Anda: {hasil_sentimen}")
#
# Fungsi ini adalah *analisis sentimen berbasis aturan* sederhana yang mengevaluasi apakah komentar pengguna tentang produk cenderung positif, negatif, atau netral berdasarkan kata-kata tertentu dalam komentar tersebut.

# Mari kita bedah:
#
# 1. **Input Komentar**:
#    - Pengguna memasukkan komentar tentang produk yang baru dibeli melalui `input("Masukkan komentar Anda tentang produk yang baru dibeli: ")`.
#
# 2. **Daftar Kata Positif dan Negatif**:
#    - Dua daftar, `kata_positif` dan `kata_negatif`, berisi kata-kata yang diasosiasikan dengan sentimen positif (misalnya, "bagus", "puas") dan negatif (misalnya, "buruk", "kecewa").
#
# 3. **Fungsi `analisis_sentimen_berbasis_aturan`**:
#    - Fungsi ini menerima `komentar` dan:
#      - Mengonversi semua kata dalam komentar menjadi huruf kecil dan memisahkannya menjadi daftar kata menggunakan `komentar.lower().split()`.
#      - Menghitung jumlah kata positif dan negatif dengan memeriksa setiap kata dalam komentar, lalu menambahkan jumlah kemunculan kata yang sesuai dalam daftar kata positif atau negatif.
#    - Jika jumlah kata positif lebih banyak daripada negatif, fungsi mengembalikan "Positif". Sebaliknya, jika kata negatif lebih dominan, fungsi mengembalikan "Negatif". Jika jumlahnya sama, fungsi mengembalikan "Netral".
#
# 4. **Hasil Analisis Sentimen**:
#    - Hasil dari fungsi `analisis_sentimen_berbasis_aturan` disimpan dalam `hasil_sentimen`.
#    - Program mencetak hasilnya: `Hasil analisis sentimen untuk komentar Anda: Positif/Negatif/Netral`.
#
# Secara keseluruhan, ini adalah fungsi sederhana yang mengukur sentimen berdasarkan kata-kata kunci tanpa menggunakan teknik analisis yang kompleks.
