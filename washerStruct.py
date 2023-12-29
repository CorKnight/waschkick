import copy

dictOfWasher = {
    "washer1": {
        "temperature": 0,
        "program": "",
        "category": "",
        "softener": False,
        "comments": [],
        "clothes": {
            "": []
        },
        "detergent": "",
    }
}


def getDetergent(conclusion: str):
    match conclusion:
        case "blue" | "red" | "green" | "yellow" | "dark":
            return "Color-Waschmittel"
        case "white":
            return "Voll-Waschmittel"
        case "Wolle":
            return "Woll-Waschmittel"
        case _:
            return "Waschmittel"


def createNewWasher(newDictOfWasher: dict, instructions: dict, cloth: str, color: str):
    name = "Waschmaschine " + str(len(newDictOfWasher) + 1)
    newDictOfWasher[name] = copy.deepcopy(dictOfWasher["washer1"])
    newDictOfWasher[name]["temperature"] = instructions.get("temperature")
    newDictOfWasher[name]["category"] = sortColorToColorCategory(cloth, color)
    newDictOfWasher[name]["program"] = instructions.get("program")
    newDictOfWasher[name]["softener"] = instructions.get("softener")
    newDictOfWasher[name]["comments"] = [instructions.get("comment")]
    newDictOfWasher[name]["clothes"][cloth] = [color]
    newDictOfWasher[name]["detergent"] = getDetergent(color) \
        if cloth != "Wolle" else getDetergent(cloth)


def flattenDictAtColors(dictToFlatten: dict):
    newDict = {}
    for cloth, clothData in dictToFlatten.items():
        colors = clothData.get("colors")
        if len(colors) == 0:
            continue
        instructions = clothData.get("washingInstructions")
        iconPath = clothData.get("iconPath")
        i = 0
        for color in colors:
            newDict[cloth + ":" + str(i)] = {
                "washingInstructions": instructions,
                "iconPath": iconPath,
                "color": color
            }
            i += 1
    return newDict


def sortColorToColorCategory(cloth: str, color: str):
    if cloth != "Sportkleidung":
        match color:
            case "red" | "yellow":
                return "Color"
            case "white":
                return "White"
            case _:
                return "Dark"
    else:
        return "Sport"


def createWasherDictByClothes(clothesDict: dict):
    clothesDict = flattenDictAtColors(clothesDict)
    newDictOfWasher = {}
    tempWasherDict = {}
    for cloth, clothData in clothesDict.items():
        instructions = clothData.get("washingInstructions")
        clothColor = clothData.get("color")
        clothTemp = instructions.get("temperature")
        clothProgram = instructions.get("program")
        clothSoftener = instructions.get("softener")
        clothComment = instructions.get("comment")
        cloth = cloth.split(":")[0]

        if len(newDictOfWasher) == 0:
            createNewWasher(tempWasherDict, instructions, cloth, clothColor)
            newDictOfWasher = copy.deepcopy(tempWasherDict)
            continue

        containsCloth = False
        for washer, washerData in newDictOfWasher.items():
            washerTemp = washerData.get("temperature")
            washerProgram = washerData.get("program")
            washerSoftener = washerData.get("softener")
            washerComments = washerData.get("comments")

            containsColor = False
            for washerCloth, washerColors in washerData["clothes"].items():
                if sortColorToColorCategory(cloth, clothColor) == washerData.get("category"):
                    containsColor = True
                    break
            if (washerTemp == clothTemp and
                    washerProgram == clothProgram and
                    washerSoftener == clothSoftener and
                    containsColor):
                containsCloth = True
                if cloth not in washerData["clothes"]:
                    tempWasherDict[washer]["clothes"][cloth] = [clothColor]
                elif clothColor not in washerData["clothes"][cloth]:
                    tempWasherDict[washer]["clothes"][cloth].append(clothColor)
        if not containsCloth:
            createNewWasher(tempWasherDict, instructions, cloth, clothColor)
        newDictOfWasher = copy.deepcopy(tempWasherDict)
    return newDictOfWasher
