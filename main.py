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
