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

#country troop counter
if True:
    NorthernEuropeTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    SouthernEuropeTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    WesternEuropeTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    IcelandTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    GreatBritainTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    #Africa
    NorthAfricaTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    EgyptTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    EastAfricaTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    CentralAfricaTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    SouthAfricaTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    #Oceania
    IndonesiaTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    NewGuineaTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    WesternAustraliaTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    EasternAustraliaTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    #South America
    BrazilTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    VenezuelaTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    PeruTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    ArgentinaTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    #North America
    CentralAmericaTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    EasternUnitedStatesTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    WesternUnitedStatesTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    EasternCanadaTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    OntarioTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    AlbertaTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    NorthwestTerritoryTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    AlaskaTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }
    GreenlandTrps={
        red:0,
        org:0,
        ylw:0,
        grn:0,
        blu:0,
        ppl:0
    }