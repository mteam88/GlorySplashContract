import json

INPUTFILE = "metadata.json"
OUTPUTDIRECTORY = "metadata/"

class FullMD(list):
    pass

class Metadata(dict):
    def __init__(self, mdid, name, description, filetype=".jpg"):
        self["mdid"] = mdid
        self["name"] = name
        self["image"] = f"ipfs://QmXsEyW6vNFrjLmiBcJFCA2LDy53jnPRLFPnib8Z5HYqXd/{mdid}{filetype}"
        self["description"] = description

md = FullMD()

def generatemd(md):
    with open(INPUTFILE) as jsonfile:
        metadatainfo = json.load(jsonfile)
        for mdnum in range(len(metadatainfo["nfts"])):
            md.append(Metadata(mdnum, metadatainfo["nfts"][mdnum]["name"], metadatainfo["nfts"][mdnum]["description"]))

generatemd(md)

for mdnft in md:
    with open(f"{OUTPUTDIRECTORY}{str(mdnft['mdid'])}.json", 'w') as file:
        json.dump(md[mdnft['mdid']],file,indent=4)