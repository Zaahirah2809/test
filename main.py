meme_dict ={
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH":"sedikit ketidaksetujuan",
            "CREEPY" :"menakutkan, tidak menyenangkan",
            "AGGRO" :"untuk menjadi agresif/marah",
            }
for i in range(5):
    word = input("Ketik bahasa gaul yang ingin kamu ketahui!(gunakan huruf kapital semua!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
