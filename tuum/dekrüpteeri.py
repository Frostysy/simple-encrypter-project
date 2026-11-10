from tuum.võti import tähestik
from time import sleep


def dekrüpteeri(encrypted_pass, key):
    """Otsib tähestikust vastava võtme ja krüpteeritud parooli indexi abil üles parooli originaaltähe"""
    originaal_parool = ""

    for i in range(len(encrypted_pass)):

        krüpteeritud_parooli_index = tähestik.index(encrypted_pass[i])
        võtme_index = tähestik.index(key[i])

        uue_tähe_index = (krüpteeritud_parooli_index -
                          võtme_index) % len(tähestik)

        originaal_parool += tähestik[uue_tähe_index]

    sleep(1)
    print("- Dekrüpteerisin parooli")
    return originaal_parool
