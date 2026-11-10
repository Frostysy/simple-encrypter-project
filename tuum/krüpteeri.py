from tuum.võti import tähestik
from time import sleep


def krüpteeri(password, key):
    """Seob parooli ja võtme iga tähe indexid ning leiab tähestikust uue vastava tähe sellele"""

    krüpteeritud_parool = ""

    for i in range(len(password)):

        password_index_tähestikus = tähestik.index(password[i])
        key_index_tähestikus = tähestik.index(key[i])

        uue_tähe_index = (password_index_tähestikus +
                          key_index_tähestikus) % len(tähestik)

        krüpteeritud_parool += tähestik[uue_tähe_index]

    sleep(1)
    print("- Krüpteerisin parooli")

    return krüpteeritud_parool
