import secrets
from time import sleep
import string

tähestik = string.ascii_letters + string.digits + \
    string.punctuation + "õäöüÕÄÖÜšžŠŽ€£"


def loo_võti():
    """Loob suvalise 64 tähemärgi pikkuse stringi, lähtudes tähestikust"""

    võti = ""

    for i in range(64):
        täht = secrets.choice(tähestik)
        võti += täht

    sleep(1)
    print("- Genereerisin unikaalse võtme")

    return võti
