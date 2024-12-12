from faker import Faker
import pandas as pd
import random
fake = Faker()

Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Companies = ["Boeing","Intel Corp","Lockheed Martin","General Electric","GE Appliances","GlobalFoundries","TPI Composites","Johnson & Johnson","Microsoft","PepsiCo"]

def GetSerial():
    global Letters
    firstpart = (random.choice(Letters) + random.choice(Letters))
    secondpart = random.randrange(1,20,1)
    thirdpart = random.randrange(120,999,1)
    fourthpart = random.choice(Letters)
    final = firstpart + " " + str(secondpart) + "-" + str(thirdpart) + " " + fourthpart 
    return final

def GetRevision():
    return random.randrange(1,11,1)

def GetCompanies():
    global Manufacturer
    company = random.choice(Companies)
    return company

def GetBuships():
    return random.randrange(100000,400000,1)

def GetReel():
     return random.randrange(32000,38000,1)

def GetFrame():
    Frame = random.choice(Letters) + " " + str(random.randrange(1,100,1) )
    return Frame

def GetDrawing():
    Descriptor = ["SAFETY", "AXIAL", "ROTARY", "ELECTRICAL", "MECHANICAL","MAGNETIC","TURBO"]
    Thingy = ["HOOK","NUT","BEARING","SPACER","PIN","ROLLER","RATCHET","HOIST","BRAKE","RETAINER"]
    Level = ["CLASS A", "CLASS B", "CLASS C", "BOX", "UNIT", "DEVICE", "CHAIN", "FRAME"]
    OtherLevel = ["TWO TON", "ONE TON", "ASSEMBLY", "DRIVE", "CHART", "WHEEL"]

    DrawingName = str(random.choice(Descriptor) + " " + random.choice(Thingy) + " " + random.choice(Level) + " " + random.choice(OtherLevel))
    return DrawingName

def GetSubID():
    return random.randrange(100,200,1)


def GetDWG():
    bullshit = ["ANR","BBNY","KLD","RNSO","LBHW","OPR","TXG"]
    Level = ["CLASS A", "CLASS B", "CLASS C", "BOX", "UNIT", "DEVICE", "CHAIN", "FRAME"]
    Cabletype = ["FIBER OPTIC", "CAT 5", "CAT 4", "CAT 6", "COAXIAL CABLE", "ELECTRIC CABLE"]
    return "S/A" + " " + str(random.randrange(256,600,1)) + random.choice(Letters) + " " + random.choice(bullshit) + " " +  random.choice(Level) + " " + random.choice(Cabletype)

def GetHull():
    shiptype = ["DDG","CG", "CVN"]
    shipnumber = random.randrange(50,120,1)
    ship = random.choice(shiptype) + str(shipnumber)
    return ship

def GetLocation():
    global Letters
    return str(random.randrange(0,11,1)) + "-" + str(random.randrange(20,60,1)) + "-" + str(random.randrange(0,11,1)) + random.choice(Letters)

def GetDWGNO():
    return random.randrange(350000,850000,1)

def GetrevisionNo():
    return random.choice(Letters)

def GetSHT():
      return random.randrange(1,10,1)

def GetCBLSHT():
    global Letters
    return str(random.randrange(100,300,1)) + random.choice(Letters)

def GetWCL():
    return random.randrange(7000000, 8000000, 1)












def create_mfr_rows(num=1):
    output = [{
    "Manufacture":GetSerial(),
    "Rev":GetRevision(),
    "Buships":GetBuships(),
    "Manufacturer":GetCompanies(),
    "Reel":GetReel(),
    "Frame":GetFrame(),
    "DrawingTitle":GetDrawing(),
    "SubId":GetSubID()
    } for x in range(num)]
    return output


def create_cable_rows(num=1):
    output = [{
    "DWGTITLE":GetDWG(),
    "HULL":GetHull(),
    "CABLENO":GetSerial(),
    "LOCATION":GetLocation(),
    "DWG":GetDWGNO(),
    "REV":GetrevisionNo(),
    "MF":"N/A",
    "SHT":GetSHT(),
    "CBLSHTZN":GetCBLSHT(),
    "WCL":GetWCL(),
    "REMARKS": fake.catch_phrase(),
    "SubId":GetSubID()
    } for x in range(num)]
    return output


mfrdf = pd.DataFrame(create_mfr_rows(20000))
mfrdf.to_csv('mfr.csv', index=False)

cabledf = pd.DataFrame(create_cable_rows(20000))
cabledf.to_csv('cable.csv', index=False)


