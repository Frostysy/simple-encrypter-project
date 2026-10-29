from parool.hindaja import hindaja
from parool.parooli_muutja import parooli_muutja
from krüpteeria.võti import loo_võti
from krüpteeria.krüpteering import krüpteeri

input_pass = str(input("Sisesta oma parool: "))
parool = parooli_muutja(hindaja(input_pass), input_pass)


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
krüpteeri(parool, võti)
print("\nKRÜPTEERIMINE ON LÕPULE VIIDUD\n\n---------------------------------------------------------------------------")
print(
    """
KOKKUVÕTE:
""")
