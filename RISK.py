import flask as f
r = f.request

#saving
import json

def save(name:str, save:dict):
    with open(name, "w") as file:
        saving = json.dumps(save)
        file.write(str(saving))

def load(name:str):
    with open(name, "r") as file:
        return json.loads(file.read())

class Cowinit:
        def __init__(self, brdr:list, con:int):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=brdr
            self.con=con


if "Classes".isalpha():
    # classes
    # asia (id:3)

    class Yakutsk:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Kamchatka,
                Irkutsk,
                Siberia
            ]
            self.con=3

    class Siberia:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Yakutsk,
                Irkutsk,
                Mongolia,
                China,
                Ural
            ]
            self.con=3

    class Ural:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Siberia,
                China,
                Afghanistan,
                Russia
            ]
            self.con=3

    class Irkutsk:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Kamchatka,
                Mongolia,
                Yakutsk,
                Siberia
            ]
            self.con=3

    class Mongolia:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Kamchatka,
                Japan,
                China,
                Siberia,
                Irkutsk
            ]
            self.con=3

    class China:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Afghanistan,
                India,
                SouthEastAsia,
                Mongolia,
                Siberia,
                Ural
            ]
            self.con=3

    class SouthEastAsia:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                China,
                India,
                Indonesia
            ]
            self.con=3

    class Japan:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Kamchatka,
                Mongolia
            ]
            self.con=3

    class India:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Afghanistan,
                China,
                MiddleEast,
                SouthEastAsia
            ]
            self.con=3

    class MiddleEast:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Afghanistan,
                EastAfrica,
                India,
                Egypt,
                SouthernEurope,
                Russia
            ]
            self.con=3

    class Afghanistan:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                China,
                India,
                Russia,
                MiddleEast,
                Ural
            ]
            self.con=3

    # europe (id:2)

    class Russia:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Afghanistan,
                NorthernEurope,
                Scandanavia,
                SouthernEurope,
                MiddleEast,
                Ural
            ]
            self.con=2

    class Scandanavia:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                GreatBritain,
                Iceland,
                NorthernEurope,
                Russia
            ]
            self.con=2

    class NorthernEurope:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                GreatBritain,
                Scandanavia,
                SouthernEurope,
                WesternEurope,
                Russia
            ]
            self.con=2

    class SouthernEurope:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Egypt,
                NorthAfrica,
                MiddleEast,
                Russia,
                NorthernEurope,
                WesternEurope
            ]
            self.con=2

    class WesternEurope:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                GreatBritain,
                NorthernEurope,
                SouthernEurope,
                NorthAfrica
            ]
            self.con=2

    class Iceland:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                GreatBritain,
                Scandanavia,
                Greenland
            ]
            self.con=2

    class GreatBritain:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Iceland,
                Scandanavia,
                NorthernEurope,
                WesternEurope
            ]
            self.con=2

    # africa (id:5)

    class NorthAfrica:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                CentralAfrica,
                EastAfrica,
                Egypt,
                WesternEurope,
                SouthernEurope,
                Brazil
            ]
            self.con=5

    class Egypt:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                EastAfrica,
                NorthAfrica,
                SouthernEurope,
                MiddleEast
            ]
            self.con=5

    class EastAfrica:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                CentralAfrica,
                Egypt,
                Madagascar,
                NorthAfrica,
                SouthAfrica
            ]
            self.con=5

    class CentralAfrica:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                EastAfrica,
                NorthAfrica,
                SouthAfrica
            ]
            self.con=5

    class SouthAfrica:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                CentralAfrica,
                EastAfrica,
                Madagascar
            ]
            self.con=5

    class Madagascar:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                EastAfrica,
                SouthAfrica
            ]
            self.con=5

    # oceania (id:6)

    class Indonesia:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                SouthEastAsia,
                NewGuinea,
                WesternAustralia
            ]
            self.con=6

    class NewGuinea:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                EasternAustralia,
                Indonesia,
                WesternAustralia
            ]
            self.con=6

    class WesternAustralia:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                EasternAustralia,
                Indonesia,
                NewGuinea
            ]
            self.con=6

    class EasternAustralia:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                NewGuinea,
                WesternAustralia
            ]
            self.con=6

    # south america (id:4)

    class Brazil:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Argentina,
                Peru,
                Venezuela,
                NorthAfrica
            ]
            self.con=4

    class Venezuela:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Brazil,
                Peru,
                CentralAmerica
            ]
            self.con=4

    class Peru:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Argentina,
                Brazil,
                Venezuela
            ]
            self.con=4

    class Argentina:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Brazil,
                Peru
            ]
            self.con=4

    # north america (id:1)

    class CentralAmerica:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Venezuela,
                EasternUSA,
                WesternUSA
            ]
            self.con=1

    class EasternUSA:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                WesternUSA,
                CentralAmerica,
                EasternCanada,
                Ontario
            ]
            self.con=1

    class WesternUSA:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                EasternUSA,
                Alberta,
                CentralAmerica,
                Ontario
            ]
            self.con=1

    class EasternCanada:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                EasternUSA,
                Greenland,
                Ontario
            ]
            self.con=1

    class Ontario:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Alberta,
                EasternUSA,
                Greenland,
                NorthwestTerritory,
                EasternCanada,
                WesternUSA
            ]
            self.con=1

    class Alberta:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Alaska,
                NorthwestTerritory,
                Ontario,
                WesternUSA
            ]
            self.con=1

    class NorthwestTerritory:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Alaska,
                Greenland,
                Alberta,
                Ontario
            ]
            self.con=1

    class Alaska:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                Alberta,
                NorthwestTerritory
            ]
            self.con=1

    class Greenland:
        def __init__(self):
            self.trps={
                "red":0,
                "org":0,
                "ylw":0,
                "grn":0,
                "blu":0,
                "ppl":0
            }
            self.king=""
            self.brdr=[
                NorthwestTerritory,
                Ontario,
                EasternCanada
            ]
            self.con=1

    class cows:
        Kamchatka = Country([Alaska,Yakutsk,Irkutsk,Japan,Mongolia],3)
        Yakutsk = Yakutsk


kingnum = {
    "red":0,
    "org":0,
    "ylw":0,
    "grn":0,
    "blu":0,
    "ppl":0
}

# end of the file

app = f.Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def game():
    for cow in cows:
        for key, value in cow.trps.items():
            if value != 0:
                countries[countries.index(country)].king = key
                kingnum[key] += 1
    args=[
    countries,
    kingnum,
    r.args
    ]
    return f.render_template("board.html", args=args)