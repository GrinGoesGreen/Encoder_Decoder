# Encoder
alph = "abcdefghijklmnopqrstuvwxyz"
     #  0123456789

inputStroka = str(input('Enter message to encode: '))
sdvig = int(input('Enter encoder offset: '))
finalStroka = ""
for a in inputStroka:
    if a in alph:
        encMesto = alph.find(a)
        new_encMesto = encMesto + sdvig
    if new_encMesto > 26:
        new_encMesto = new_encMesto - 26
        print(alph[new_encMesto], new_encMesto)
    finalStroka += alph[new_encMesto]
print(finalStroka)

# Decoder
decInput = str(input('Enter message to decode: '))
decSdvig = int(input('Enter decoder offset: '))
decFinal = ""
for i in decInput:
    if i in alph:
        decMesto = alph.find(i)
        new_decMesto = decMesto - decSdvig
    decFinal += alph[new_decMesto]
print(decFinal)
