from pathlib import Path


def parooli_fail(krüpteeritud_parool, keskkond):
    """Kirjutab krüpteeritud parooli ja vastava keskkonna ettenähtud faili"""

    kaust = Path.home() / "Documents" / "Krüpteeria" / "Programmi Failid"
    # loob kõik puuduvad kaustad failiteel. - kui kaustad juba eksisteerivad, ei anna veateadet ega loo neid uuesti.
    kaust.mkdir(parents=True, exist_ok=True)

    failitee = kaust / "krüpteeringud.txt"

    with open(failitee, "a", encoding="utf-8") as file:
        file.write(f"{krüpteeritud_parool} - {keskkond}\n")


def võtme_fail(võti):
    """Kirjutab võtme ettenähtud faili"""

    kaust = Path.home() / "Documents" / "Krüpteeria" / "Programmi Failid"
    # loob kõik puuduvad kaustad failiteel. - kui kaustad juba eksisteerivad, ei anna veateadet ega loo neid uuesti.
    kaust.mkdir(parents=True, exist_ok=True)

    failitee = kaust / "võtmed.txt"

    with open(failitee, "a", encoding="utf-8") as file:
        file.write(f"{võti}\n")
