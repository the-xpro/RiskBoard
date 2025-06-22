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

class Cown:
        def __init__(self, brdr:list, con:int):
            self.trps={
                "red":0,"org":0,"ylw":0,"grn":0,"blu":0,"ppl":0
            }
            self.king=""
            self.brdr=brdr
            con



class Cows:
    def __init__(self):
        global Kamchatka
        Kamchatka = Cown([Alaska,Yakutsk,Irkutsk,Japan,Mongolia],3)
        Yakutsk = Cown([Kamchatka,Irkutsk,Siberia],3)
        Siberia = Cown([Yakutsk,Irkutsk,Mongolia,China,Ural],3)
        Ural = Cown([Siberia,China,Afghanistan,Russia],3)
        Irkutsk = Cown([Kamchatka,Mongolia,Yakutsk,Siberia],3)
        Mongolia = Cown([Kamchatka,Japan,China,Siberia,Irkutsk],3)
        China = Cown([Afghanistan,India,SouthEastAsia,Mongolia,Siberia,Ural],3)
        SouthEastAsia = Cown([China,India,Indonesia],3)
        Japan = Cown([Kamchatka,Mongolia],3)
        India = Cown([Afghanistan,China,MiddleEast,SouthEastAsia],3)
        MiddleEast = Cown([Afghanistan,EastAfrica,India,Egypt,SouthernEurope,Russia],3)
        Afghanistan = Cown([China,India,Russia,MiddleEast,Ural],3)
            # europe (id:2))
        Russia = Cown([Afghanistan,NorthernEurope,Scandanavia,SouthernEurope,MiddleEast,Ural],2)
        Scandanavia = Cown([GreatBritain,Iceland,NorthernEurope,Russia],2)
        NorthernEurope = Cown([GreatBritain,Scandanavia,SouthernEurope,WesternEurope,Russia],2)
        SouthernEurope = Cown([Egypt,NorthAfrica,MiddleEast,Russia,NorthernEurope,WesternEurope],2)
        WesternEurope = Cown([GreatBritain,NorthernEurope,SouthernEurope,NorthAfrica],2)
        Iceland = Cown([GreatBritain,Scandanavia,Greenland],2)
        GreatBritain = Cown([Iceland,Scandanavia,NorthernEurope,WesternEurope],2)
            # africa (id:5))
        NorthAfrica = Cown([CentralAfrica,EastAfrica,Egypt,WesternEurope,SouthernEurope,Brazil],5)
        Egypt = Cown([EastAfrica,NorthAfrica,SouthernEurope,MiddleEast],5)
        EastAfrica = Cown([CentralAfrica,Egypt,Madagascar,NorthAfrica,SouthAfrica],5)
        CentralAfrica = Cown([EastAfrica,NorthAfrica,SouthAfrica],5)
        SouthAfrica = Cown([CentralAfrica,EastAfrica,Madagascar],5)
        Madagascar = Cown([EastAfrica,SouthAfrica],5)
            # oceania (id:6))
        Indonesia = Cown([SouthEastAsia,NewGuinea,WesternAustralia],6)
        NewGuinea = Cown([EasternAustralia,Indonesia,WesternAustralia],6)
        WesternAustralia = Cown([EasternAustralia,Indonesia,NewGuinea],6)
        EasternAustralia = Cown([NewGuinea,WesternAustralia],6)
            # south america (id:4))
        Brazil = Cown([Argentina,Peru,Venezuela,NorthAfrica],4)
        Venezuela = Cown([Brazil,Peru,CentralAmerica],4)
        Peru = Cown([Argentina,Brazil,Venezuela],4)
        Argentina = Cown([Brazil,Peru],4)
            # north america (id:1)
        CentralAmerica = Cown([Venezuela,EasternUSA,WesternUSA]1)
        EasternUSA = Cown([WesternUSA,CentralAmerica,EasternCanada,Ontario],1)
        Alberta = Cown([Alaska,NorthwestTerritory,Ontario,WesternUSA],1)
        WesternUSA = Cown([EasternUSA,Alberta,CentralAmerica,Ontario],1)
        EasternCanada = Cown([EasternUSA,Greenland,Ontario],1)
        Ontario = Cown([Alberta,EasternUSA,Greenland,NorthwestTerritory,EasternCanada,WesternUSA],1)


Cowss = Cows

Cowis = [
    Cows.Kamchatka,
    Cows.Yakutsk,
    Siberia,
    Ural,
    Irkutsk,
    Mongolia,
    China,
    SouthEastAsia,
    Japan,
    India,
    MiddleEast,
    Afghanistan,
    Russia,
    Scandanavia,
    NorthernEurope,
    SouthernEurope,
    WesternEurope,
    Iceland,
    GreatBritain,
    NorthAfrica,
    Egypt,
    EastAfrica,
    CentralAfrica,
    SouthAfrica,
    Madagascar,
    Indonesia,
    NewGuinea,
    WesternAustralia,
    EasternAustralia,
    Brazil,
    Venezuela,
    Peru,
    Argentina,
    CentralAmerica,
    EasternUSA,
    WesternUSA,
    EasternCanada,
    Ontario,
    Alberta,
    NorthwestTerritory,
    Alaska,
    Greenland
]

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
    for Cow in Cowis:
        for key, value in Cow.trps.items():
            if value != 0:
                Cowis[Cowis.index(Cow)].king = key
                kingnum[key] += 1
    args=[
    Cowis,
    kingnum,
    r.args
    ]
    return f.render_template("board.html", args=args)