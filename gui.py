import PySimpleGUI as sg
from parool.hindaja import hindaja
from tuum.võti import loo_võti, tähestik
from tuum.krüpteeri import krüpteeri
from tuum.dekrüpteeri import dekrüpteeri
from tuum.kirjuta_faili import parooli_fail, võtme_fail
from tuum.eemalda_failist import kustuta_parool

sg.theme("DarkBlue2")

# layout on põhiakna paigutus, 1 rida = 1 element
layout = [
    [sg.Text("KRÜPTEERIMINE", font=("Arial", 14, "bold"))],
    [sg.Text("Sisesta oma parool:")],
    [sg.Input(key="-PAROOL-", password_char="*")],
    [sg.Text("Sisesta keskkond, kus parooli kasutad:")],
    [sg.Input(key="-KESKKOND-")],
    [sg.Button("Hinda parooli"), sg.Button("Krüpteeri"), sg.Button("Välju")],
    [sg.Text("Parooli hinnang:")],
    [sg.Text("", key="-HINNANG-", size=(60, 6))],
    [sg.Text("Krüpteeritud parool:")],
    [sg.Input(key="-KRÜPTEERING-", readonly=True)],
    [sg.Text("Genereeritud võti:")],
    [sg.Input(key="-VÕTI-", readonly=True)],

    [sg.HorizontalSeparator()],
    [sg.Text("DEKRÜPTEERIMINE", font=("Arial", 14, "bold"))],
    [sg.Text("Sisesta krüpteeritud parool:")],
    [sg.Input(key="-DEKRÜPTEERI-")],
    [sg.Text("Sisesta võti:")],
    [sg.Input(key="-SISENDVÕTI-")],
    [sg.Button("Dekrüpteeri")],
    [sg.Text("Dekrüpteeritud parool:")],
    [sg.Input(key="-TULEMUS-", readonly=True)],

    [sg.HorizontalSeparator()],
    [sg.Text("PAROOLIHALDUR", font=("Arial", 14, "bold"))],
    [sg.Text("Saa ülevaade oma paroolidest")],
    [sg.Text("Krüpteeritud Parool 1"),
     sg.Button("Võti"), sg.Button("Kustuta")],
]

# sg.window loob akna
window = sg.Window("Paroolide krüpteerija", layout)


while True:
    # event on sündmus nt nupu vajatus, values sõnastik kus sisestusväljade väärtused võtme järgi
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Välju":
        break

    # PAROOLI HINDAMINE
    if event == "Hinda parooli":
        parool = values["-PAROOL-"]
        keskkond = values["-KESKKOND-"]
        # tühi väli = hoiatus
        if keskkond == "":
            sg.popup("Sisesta keskkond!")
        if parool == "":
            sg.popup("Sisesta parool!")
        else:
            # hindaja funist skoor ja hoiatused
            skoor, hoiatused = hindaja(parool)
            if skoor == 0:
                window["-HINNANG-"].update(
                    "Parool vastab kõigile tingimustele!", text_color="lightgreen"
                )
            else:
                window["-HINNANG-"].update("\n".join(hoiatused),
                                           text_color="orange")

    # PAROOLI KRÜPTEERIMINE
    if event == "Krüpteeri":
        parool = values["-PAROOL-"]
        keskkond = values["-KESKKOND-"]

        if parool == "":
            sg.popup("Sisesta parool!")
        # kuna võti 64 tähemärki, siis piirab parooli pikkuse
        elif len(parool) > 64:
            sg.popup("Parooli maksimaalne pikkus võib olla 64 tähemärki!")
        # kontrollib kas paroolis lubamatud tähemärgid
        elif any(märk not in tähestik for märk in parool):
            sg.popup("Parool sisaldab lubamatuid tähemärke!")
        else:
            skoor, hoiatused = hindaja(parool)

            # kui on hoiatused, siis popup kus pakub kas parooli muuta või jätkata krüpteerimisega
            if skoor > 0:
                popup_layout = [
                    [sg.Text("\n".join(hoiatused), text_color="orange")],
                    [sg.Text("Kas soovid oma parooli muuta?",
                             text_color="white")],
                    [sg.Button("Muuda parooli"), sg.Button(
                        "Jätka krüpteerimisega")],
                ]

                popup_window = sg.Window(
                    "Parooli muutmine", popup_layout, modal=True)

                # salvestab valiku
                vastus, values = popup_window.read()

                popup_window.close()

                if vastus != "Jätka krüpteerimisega":
                    continue
            # geneb võtme loo_võti funiga
            võti = loo_võti()
            krüpteeritud_parool = krüpteeri(parool, võti)
            # salvestame genereeritud väärtused failidesse
            parooli_fail(krüpteeritud_parool, keskkond)
            võtme_fail(võti)
            # põhiaknasse genetud parool ja võti
            window["-KRÜPTEERING-"].update(krüpteeritud_parool)
            window["-VÕTI-"].update(võti)

    # PAROOLI DEKRÜPTEERIMINE
    if event == "Dekrüpteeri":
        krüpteeritud_parool = values["-DEKRÜPTEERI-"]
        võti = values["-SISENDVÕTI-"]

        # tühi väli = hoiatus
        if krüpteeritud_parool == "" or võti == "":
            sg.popup("Täida mõlemad väljad!")

        # kui kõik korras, siis dekrüpteerib ja kuvab tulemuse
        else:
            tulemus = dekrüpteeri(krüpteeritud_parool, võti)
            window["-TULEMUS-"].update(tulemus)

    # PAROOLIHALDUR
    if event == "Kustuta":
        popup_kustuta_layout = [
            [sg.Text("KUSTUTA PAROOL", text_color="red")],
            [sg.Text("Kas soovid oma parooli kustutada?", text_color="white")],
            [sg.Button("KUSTUTA")]
        ]

        popup_window = sg.Window(
            "Parooli kustutamine", popup_kustuta_layout, modal=True)

        kustuta_parool(
            "hju2MZO}UQe", 'öfcJxZx;GF6K1#}cA=,Šc)qü*pl_jmä7coÜ]CÕgä`~p2\\56}1">7,s;_6B4*ä!L{')


window.close()
