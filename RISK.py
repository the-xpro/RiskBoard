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
        def onclick():
            pass



class Cowss:
    def __init__(self):
        self.Kamchatka = Cown([self.Alaska,self.Yakutsk,self.Irkutsk,self.Japan,self.Mongolia],3)
        self.Yakutsk = Cown([self.Kamchatka,self.Irkutsk,self.Siberia],3)
        self.Siberia = Cown([self.Yakutsk,self.Irkutsk,self.Mongolia,self.China,self.Ural],3)
        self.Ural = Cown([self.Siberia,self.China,self.Afghanistan,self.Russia],3)
        self.Irkutsk = Cown([self.Kamchatka,self.Mongolia,self.Yakutsk,self.Siberia],3)
        self.Mongolia = Cown([self.Kamchatka,self.Japan,self.China,self.Siberia,self.Irkutsk],3)
        self.China = Cown([self.Afghanistan,self.India,self.SouthEastAsia,self.Mongolia,self.Siberia,self.Ural],3)
        self.SouthEastAsia = Cown([self.China,self.India,self.Indonesia],3)
        self.Japan = Cown([self.Kamchatka,self.Mongolia],3)
        self.India = Cown([self.Afghanistan,self.China,self.MiddleEast,self.SouthEastAsia],3)
        self.MiddleEast = Cown([self.Afghanistan,self.EastAfrica,self.India,self.Egypt,self.SouthernEurope,self.Russia],3)
        self.Afghanistan = Cown([self.China,self.India,self.Russia,self.MiddleEast,self.Ural],3)
            # europe (id:2))
        self.Russia = Cown([self.Afghanistan,self.NorthernEurope,self.Scandanavia,self.SouthernEurope,self.MiddleEast,self.Ural],2)
        self.Scandanavia = Cown([self.GreatBritain,self.Iceland,self.NorthernEurope,self.Russia],2)
        self.NorthernEurope = Cown([self.GreatBritain,self.Scandanavia,self.SouthernEurope,self.WesternEurope,self.Russia],2)
        self.SouthernEurope = Cown([self.Egypt,self.NorthAfrica,self.MiddleEast,self.Russia,self.NorthernEurope,self.WesternEurope],2)
        self.WesternEurope = Cown([self.GreatBritain,self.NorthernEurope,self.SouthernEurope,self.NorthAfrica],2)
        self.Iceland = Cown([self.GreatBritain,self.Scandanavia,self.Greenland],2)
        self.GreatBritain = Cown([self.Iceland,self.Scandanavia,self.NorthernEurope,self.WesternEurope],2)
            # africa (id:5))
        self.NorthAfrica = Cown([self.CentralAfrica,self.EastAfrica,self.Egypt,self.WesternEurope,self.SouthernEurope,self.Brazil],5)
        self.Egypt = Cown([self.EastAfrica,self.NorthAfrica,self.SouthernEurope,self.MiddleEast],5)
        self.EastAfrica = Cown([self.CentralAfrica,self.Egypt,self.Madagascar,self.NorthAfrica,self.SouthAfrica],5)
        self.CentralAfrica = Cown([self.EastAfrica,self.NorthAfrica,self.SouthAfrica],5)
        self.SouthAfrica = Cown([self.CentralAfrica,self.EastAfrica,self.Madagascar],5)
        self.Madagascar = Cown([self.EastAfrica,self.SouthAfrica],5)
            # oceania (id:6))
        self.Indonesia = Cown([self.SouthEastAsia,self.NewGuinea,self.WesternAustralia],6)
        self.NewGuinea = Cown([self.EasternAustralia,self.Indonesia,self.WesternAustralia],6)
        self.WesternAustralia = Cown([self.EasternAustralia,self.Indonesia,self.NewGuinea],6)
        self.EasternAustralia = Cown([self.NewGuinea,self.WesternAustralia],6)
            # south america (id:4))
        self.Brazil = Cown([self.Argentina,self.Peru,self.Venezuela,self.NorthAfrica],4)
        self.Venezuela = Cown([self.Brazil,self.Peru,self.CentralAmerica],4)
        self.Peru = Cown([self.Argentina,self.Brazil,self.Venezuela],4)
        self.Argentina = Cown([self.Brazil,self.Peru],4)
            # north america (id:1)
        self.CentralAmerica = Cown([self.Venezuela,self.EasternUSA,self.WesternUSA],1)
        self.EasternUSA = Cown([self.WesternUSA,self.CentralAmerica,self.EasternCanada,self.Ontario],1)
        self.Alberta = Cown([self.Alaska,self.NorthwestTerritory,self.Ontario,self.WesternUSA],1)
        self.WesternUSA = Cown([self.EasternUSA,self.Alberta,self.CentralAmerica,self.Ontario],1)
        self.EasternCanada = Cown([self.EasternUSA,self.Greenland,self.Ontario],1)
        self.Ontario = Cown([self.Alberta,self.EasternUSA,self.Greenland,self.NorthwestTerritory,self.EasternCanada,self.WesternUSA],1)
        self.NorthwestTerritory = Cown([self.Alberta,self.Ontario,self.Greenland,self.Alaska])
        self.Greenland = Cown([self.NorthwestTerritory,self.Ontario,self.EasternCanada],1)
        self.Alaska = Cown([self.Alberta,self.NorthwestTerritory],1)

Cows = Cowss()
     
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
    for Cow in Cows.__dir__():
        if not Cows.__getattribute__(Cow).startswith("_"):
            prevking = Cows.__getattribute__(Cow).king
            for key, value in Cows.__getattribute__(Cow).trps.items():
                if value != 0:
                    Cows.__getattribute__(Cow).king = key
                    kingnum[key] += 1
                    kingnum[prevking] -= 1
    
    if r.method == "POST":
        pass

    args=[
    Cows,
    kingnum,
    r.args
    ]
    return f.render_template("board.html", args=args)