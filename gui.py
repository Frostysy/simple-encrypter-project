import PySimpleGUI as sg
from parool.hindaja import hindaja
from tuum.võti import loo_võti, tähestik
from tuum.krüpteeri import krüpteeri
from tuum.dekrüpteeri import dekrüpteeri

sg.theme("DarkBlue3")

# layout on põhiakna paigutus, 1 rida = 1 element
layout = [
    [sg.Text("Sisesta oma parool:")],
    [sg.Input(key="-PAROOL-", password_char="*")],
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

        # tühi väli = hoiatus
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
                window["-HINNANG-"].update("\n".join(hoiatused), text_color="orange")

    # PAROOLI KRÜPTEERIMINE
    if event == "Krüpteeri":
        parool = values["-PAROOL-"]

        if parool == "":
            sg.popup("Sisesta parool!")
        # kuna võti 64 tähemärki, siis piirab parooli pikkuse
        elif len(parool) > 64:
            sg.popup("Parool on liiga pikk!")
        # kontrollib kas paroolis lubamatud tähemärgid
        elif any(märk not in tähestik for märk in parool):
            sg.popup("Parool sisaldab lubamatuid tähemärke!")
        else:
            skoor, hoiatused = hindaja(parool)

            # kui on hoiatused, siis popup kus pakub kas parooli muuta või jätkata krüpteerimisega
            if skoor > 0:
                popup_layout = [
                    [sg.Text("\n".join(hoiatused), text_color="orange")],
                    [sg.Text("Kas soovid oma parooli muuta?", text_color="white")],
                    [sg.Button("Muuda parooli"), sg.Button("Jätka krüpteerimisega")],
                ]

                popup_window = sg.Window("Parooli muutmine", popup_layout, modal=True)

                # salvestab valiku
                vastus, value = popup_window.read()

                popup_window.close()

                if vastus != "Jätka krüpteerimisega":
                    continue
            # geneb võtme loo_võti funiga
            võti = loo_võti()
            krüpteeritud = krüpteeri(parool, võti)
            # põhiaknasse genetud parool ja võti
            window["-KRÜPTEERING-"].update(krüpteeritud)
            window["-VÕTI-"].update(võti)

    # PAROOLI DEKRÜPTEERIMINE
    if event == "Dekrüpteeri":
        krüpteeritud = values["-DEKRÜPTEERI-"]
        võti = values["-SISENDVÕTI-"]

        # tühi väli = hoiatus
        if krüpteeritud == "" or võti == "":
            sg.popup("Täida mõlemad väljad!")

        # kui kõik korras, siis dekrüpteerib ja kuvab tulemuse
        else:
            tulemus = dekrüpteeri(krüpteeritud, võti)
            window["-TULEMUS-"].update(tulemus)
window.close()
