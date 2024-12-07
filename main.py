while True:
    meme_dict = {
                "gn": "forma de despedirse cuando es de noche",
                "ntp": "no te preocupes",
                "tkm": "para decir te quiero mucho",
                }
    
    word = input("Escribe una palabra que no entiendas (en minisculas): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("no existe esa palabra")
