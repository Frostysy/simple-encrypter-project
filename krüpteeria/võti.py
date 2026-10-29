import secrets
from time import sleep


def loo_võti():

    tähestik = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"

    võti = ""

    for i in range(64):
        täht = secrets.choice(tähestik)
        võti += täht

    sleep(1)
    print("- Genereerisin unikaalse võtme")

    return võti
