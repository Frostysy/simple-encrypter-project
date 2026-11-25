from parool.hindaja import hindaja
from parool.parooli_muutja import parooli_muutja
from tuum.võti import loo_võti
from tuum.krüpteeri import krüpteeri
from tuum.dekrüpteeri import dekrüpteeri

input_pass = str(input("Sisesta oma parool: "))

while True:
    if input_pass == "":
        print("⚠️ Sisesta parool")
        input_pass = str(input("Sisesta oma parool: "))
    else:
        break


skoor, hoiatused = hindaja(input_pass)

for hoiatus in hoiatused:
    print(hoiatus)

parool = parooli_muutja(skoor, input_pass)


while True:

    input_kinnitus = str(
        input(f'Kas soovid parooli "{parool}" krüpteerida | (y / n): ')).lower()

    if input_kinnitus == "y" or input_kinnitus == "yes":
        break
    elif input_kinnitus == "n" or input_kinnitus == "no":
        print("Krüpteerimine katkestatud")
        exit()

print("---------------------------------------------------------------------------\n\nALUSTAN KRÜPTEERIMISEGA\n")
võti = loo_võti()
krüpteering = krüpteeri(parool, võti)

print("\nKRÜPTEERIMINE ON LÕPULE VIIDUD\n\n---------------------------------------------------------------------------")
print(
    """
KOKKUVÕTE:
""")
