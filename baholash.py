def bahola(isimlar):
    baholar = {}
    while isimlar:
        ism = isimlar.pop()
        baho = input(f"Talaba {ism.title() } ning bahosi: ")
        baholar[ism] = int(baho)
    return baholar
talabalar = ["Shaxzod","fozil","sardor","Samiddin"]
baholari = bahola(talabalar[:])
print(baholari)

        