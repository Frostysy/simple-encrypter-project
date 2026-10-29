"""
Infoallikad: 
            https://www.staysafeonline.org/articles/passwords
"""


def hindaja(password):
    skoor = 0

    # Hinda parooli pikkust
    if len(password) < 16:
        print("⚠️ Salasõna pikkus võiks olla vähemalt 16 tähemärki!")
        skoor += 1

    # Tuvasta, kas paroolis esineb sümboleid
    sümbolid = ["!", "#", "€", "%", "&", "/", "=", "?", "@", "£", "$"]
    sümbolid_password = []

    for i in sümbolid:
        for j in password:
            if j == i:
                sümbolid_password.append(i)

    if len(sümbolid_password) == 0:
        print("⚠️ Salasõna ei sisalda ühtegi sümbolit!")
        skoor += 1

    # Tuvasta, kas paroolis esineb numbreid või kas parool ainult koosnebgi numbritest
    nr_lugeja = 0
    for i in password:
        try:
            arv = int(i)
            nr_lugeja += 1
        except:
            continue

    if nr_lugeja == 0:
        print("⚠️ Salasõna ei sisalda ühtegi numbrit!")
        skoor += 1
    if nr_lugeja == len(password):
        print("⚠️ Salasõna koosneb ainult numbritest!")
        skoor += 1

    # Tuvasta, kas paroolis on nii SUURI kui ka väikeseid tähti
    väike_lugeja = 0
    suur_lugeja = 0
    for i in password:
        if i.isupper():
            suur_lugeja += 1
        elif i.islower():
            väike_lugeja += 1

    if väike_lugeja == 0:
        print("⚠️ Salasõna ei sisalda ühtegi väikest tähte!")
        skoor += 1
    if suur_lugeja == 0:
        print("⚠️ Salasõna ei sisalda ühtegi suurt tähte!")
        skoor += 1

    return skoor
