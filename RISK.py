import pygame

red=0
org=0
ylw=0
grn=0
blu=0
ppl=0

#saving
import json

def save(name:str, save:dict):
    with open(name, "w") as file:
        saving = json.dumps(save)
        file.write(str(saving))

def load(name:str):
    with open(name, "r") as file:
        return json.loads(file.read())

# classes
class Kamchatka:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            Alaska,
            Yakutsk,
            Irkutsk,
            Japan,
            Mongolia
        ]

class Yakutsk:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            Kamchatka,
            Irkutsk,
            Siberia
        ]

class Siberia:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            Yakutsk,
            Irkutsk,
            Mongolia,
            China,
            Ural
        ]

class Ural:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            Siberia,
            China,
            Afghanistan,
            Russia
        ]

class Irkutsk:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            Kamchatka,
            Mongolia,
            Yakutsk,
            Siberia
        ]

class Mongolia:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            Kamchatka,
            Japan,
            China,
            Siberia,
            Irkutsk
        ]

class China:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            Afghanistan,
            India,
            Siam,
            Mongolia,
            Siberia,
            Ural
        ]

class China:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            Afghanistan,
            India,
            Siam,
            Mongolia,
            Siberia,
            Ural
        ]

class Siam:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            China,
            India,
            Indonesia
        ]

class Japan:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            Kamchatka,
            Mongolia
        ]

class India:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            Afghanistan,
            China,
            MiddleEast,
            Siam
        ]

class MiddleEast:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            Afghanistan,
            EastAfrica,
            India,
            Egypt,
            SouthernEurope,
            Russia
        ]

class Afghanistan:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            China,
            India,
            Russia,
            MiddleEast,
            Ural
        ]

class Russia:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            Afghanistan,
            NorthernEurope,
            Scandanavia,
            SouthernEurope,
            MiddleEast,
            Ural
        ]

class Scandanavia:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            GreatBritain,
            Iceland,
            NorthernEurope,
            Russia
        ]

class NorthernEurope:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            GreatBritain,
            Scandanavia,
            SouthernEurope,
            WesternEurope,
            Russia
        ]

class SouthernEurope:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            Egypt,
            NorthAfrica,
            MiddleEast,
            Russia,
            NorthernEurope,
            WesternEurope
        ]

class WesternEurope:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            GreatBritain,
            NorthernEurope,
            SouthernEurope,
            NorthAfrica
        ]

class Iceland:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            GreatBritain,
            Scandanavia,
            Greenland
        ]

class GreatBritain:
    def __init__(self):
        self.trps={
            red:0,
            org:0,
            ylw:0,
            grn:0,
            blu:0,
            ppl:0
        }
        self.king={
            red:False,
            org:False,
            ylw:False,
            grn:False,
            blu:False,
            ppl:False
        }
        self.brdr=[
            Iceland,
            Scandanavia,
            NorthernEurope,
            WesternEurope
        ]

#country troop counter
if True:
    NorthAfrica={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    Egypt={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    EastAfrica={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    CentralAfrica={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    SouthAfrica={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    #Oceania
    Indonesia={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    NewGuinea={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    WesternAustralia={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    EasternAustralia={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    #South America
    Brazil={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    Venezuela={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    Peru={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    Argentina={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    #North America
    CentralAmerica={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    EasternUnitedStates={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    WesternUnitedStates={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    EasternCanada={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    Ontario={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    Alberta={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    NorthwestTerritory={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    Alaska={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    Greenland={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }