import json
import requests

INPUTFILE = "metadata.json"
OUTPUTDIRECTORY = "metadata/"

class FullMD(list):
    pass

class Metadata(dict):
    def __init__(self, mdid, name, filetype=".jpg"):
        self["mdid"] = mdid
        self["name"] = name
        self["image"] = f"ipfs://QmXsEyW6vNFrjLmiBcJFCA2LDy53jnPRLFPnib8Z5HYqXd/{mdid}{filetype}"
        self["description"] = self.getdescriptionfromname(name)

    @staticmethod
    def getdescriptionfromname(name):
        r = requests.post(
            "https://api.deepai.org/api/text-generator",
            data={
                'text': name,
            },
            headers={'api-key': 'd60d0680-40dc-4dcf-a61d-9dc7a697ce4e'}
        )
        return r.json()['output']

md = FullMD()

def generatemd(md):
    with open(INPUTFILE) as jsonfile:
        metadatainfo = json.load(jsonfile)
        for mdnum in range(len(metadatainfo["nfts"])):
            md.append(Metadata(mdnum, metadatainfo["nfts"][mdnum]["name"]))

generatemd(md)

for mdnft in md:
    with open(f"{OUTPUTDIRECTORY}{str(mdnft['mdid'])}.json", 'w') as file:
        json.dump(md[mdnft['mdid']],file,indent=4)