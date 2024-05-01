meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
            
word = input("Anlamadığın kelimeyi benimle paylaş")            

if word in meme_dict:
    meaning = meme_dict[word]
    print(f"{word} kelimesi şu anlama gelir)
