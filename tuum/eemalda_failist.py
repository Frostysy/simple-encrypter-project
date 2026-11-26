from pathlib import Path

parooli_kaust = Path.home() / "Documents" / "Krüpteeria" / \
    "Programmi Failid" / "krüpteeringud.txt"

võtme_kaust = Path.home() / "Documents" / "Krüpteeria" / \
    "Programmi Failid" / "võtmed.txt"


def kustuta_parool(krüpteeritud_parool, võti):
    with open(parooli_kaust, "r", encoding="utf-8") as fail:
        read = fail.readlines()

    with open(parooli_kaust, "w", encoding="utf-8") as fail:
        for rida in read:
            if rida.strip().split(" - ", 1)[0] != krüpteeritud_parool:
                fail.write(rida)

    with open(võtme_kaust, "r", encoding="utf-8") as fail:
        read = fail.readlines()

    with open(võtme_kaust, "w", encoding="utf-8") as fail:
        for rida in read:
            if rida.strip() != võti:
                fail.write(rida)


