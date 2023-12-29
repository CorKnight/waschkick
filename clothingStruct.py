import copy
# dictOfClothes = {
#     # [[temperature, program, softener, comment], icon]
#     "Shirts": [[30, "Feinwäsche", True, "Eventuell 40° - siehe Etikett"], "fi fi-rr-shirt-long-sleeve", []],
#     "T-Shirts": [[30, "Feinwäsche", True, "Eventuell 40° - siehe Etikett"], "fi fi-rr-tshirt", []],
#     "Pullover": [[30, "Feinwäsche", True, "Eventuell 40° - siehe Etikett"], "fi fi-rr-shirt-long-sleeve", []],
#     "Hosen": [[30, "Feinwäsche", True, ""], "fi fi-rr-tshirt", []],
#     "Socken": [[60, "Baumwolle", True, "Vorher auseinander knüllen"], "fi fi-rr-socks", []],
#     "Handtücher": [[60, "Baumwolle", True, ""], "fi fi-rr-tshirt", []],
#     "Unterhosen": [[60, "Baumwolle", True, ""], "fi fi-rr-shirt-tank-top", []],
#     "Sportkleidung": [[30, "Feinwäsche", False, ""], "fi fi-rr-shirt-running", []],
#     "Hemden": [[30, "Feinwäsche", False, ""], "fi fi-rr-shirt-long-sleeve", []],
#     "Wolle": [[30, "Wolle", False, ""], "fi fi-rr-shirt-long-sleeve", []],
#     "Jeans": [[30, "Feinwäsche", False, ""], "fi fi-rr-tshirt", []],
# }

dictOfClothes = {
    "Shirts": {
        "washingInstructions": {
            "temperature": 30,
            "program": "Feinwäsche",
            "softener": True,
            "comment": "Eventuell 40° - siehe Etikett"
        },
        "iconPath": "fi fi-rr-shirt-long-sleeve",
        "colors": []
    },
    "T-Shirts": {
        "washingInstructions": {
            "temperature": 30,
            "program": "Feinwäsche",
            "softener": True,
            "comment": "Eventuell 40° - siehe Etikett"
        },
        "iconPath": "fi fi-rr-tshirt",
        "colors": []
    },
    "Pullover": {
        "washingInstructions": {
            "temperature": 30,
            "program": "Feinwäsche",
            "softener": True,
            "comment": "Eventuell 40° - siehe Etikett"
        },
        "iconPath": "fi fi-rr-shirt-long-sleeve",
        "colors": []
    },
    "Hosen": {
        "washingInstructions": {
            "temperature": 30,
            "program": "Feinwäsche",
            "softener": True,
            "comment": ""
        },
        "iconPath": "fi fi-rr-clothes-hanger",
        "colors": []
    },
    "Socken": {
        "washingInstructions": {
            "temperature": 60,
            "program": "Baumwolle",
            "softener": True,
            "comment": "Vorher auseinander knüllen"
        },
        "iconPath": "fi fi-rr-socks",
        "colors": []
    },
    "Handtücher": {
        "washingInstructions": {
            "temperature": 60,
            "program": "Baumwolle",
            "softener": True,
            "comment": ""
        },
        "iconPath": "fi fi-rr-clothes-hanger",
        "colors": []
    },
    "Unterhosen": {
        "washingInstructions": {
            "temperature": 60,
            "program": "Baumwolle",
            "softener": True,
            "comment": ""
        },
        "iconPath": "fi fi-rr-clothes-hanger",
        "colors": []
    },
    "Sportkleidung": {
        "washingInstructions": {
            "temperature": 30,
            "program": "Feinwäsche",
            "softener": False,
            "comment": ""
        },
        "iconPath": "fi fi-rr-shirt-running",
        "colors": []
    },
    "Hemden": {
        "washingInstructions": {
            "temperature": 40,
            "program": "Feinwäsche",
            "softener": False,
            "comment": ""
        },
        "iconPath": "fi fi-rr-shirt-long-sleeve",
        "colors": []
    },
    "Wolle": {
        "washingInstructions": {
            "temperature": 30,
            "program": "Wolle",
            "softener": False,
            "comment": ""
        },
        "iconPath": "fi fi-rr-uniform-martial-arts",
        "colors": []
    },
    "Jeans": {
        "washingInstructions": {
            "temperature": 30,
            "program": "Feinwäsche",
            "softener": False,
            "comment": ""
        },
        "iconPath": "fi fi-rr-clothes-hanger",
        "colors": []
    },
    "Jacken": {
        "washingInstructions": {
            "temperature": 30,
            "program": "Feinwäsche",
            "softener": False,
            "comment": ""
        },
        "iconPath": "fi fi-rr-uniform-martial-arts",
        "colors": []
    }
}


def getWashingInstructionsForClothes(clothes: dict | None):
    if clothes is None:
        return dictOfClothes
    newDict = copy.deepcopy(dictOfClothes)
    for cloth in clothes:
        if cloth not in newDict:
            continue
        newDict[cloth]["colors"] = clothes[cloth]
    return newDict
