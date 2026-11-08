from parool.hindaja import hindaja


def parooli_muutja(hinne, algne_parool):
    while True:

        if hinne >= 1:
            input_kinnitus = str(
                input("Lähtudes hoiatustest, kas soovid oma parooli muuta | (y / n): ")).lower()

            if input_kinnitus == "y" or input_kinnitus == "yes":
                input_pass = str(input("Sisesta uus parool: "))

                uus_hinne = hindaja(input_pass)

                if uus_hinne == 0:
                    return input_pass
                else:
                    continue

            elif input_kinnitus == "n" or input_kinnitus == "no":
                break
        else:
            return algne_parool

    return algne_parool
