from flask import Flask, render_template, request
from clothingStruct import getWashingInstructionsForClothes
from washerStruct import createWasherDictByClothes, flattenDictAtColors

app = Flask(__name__)


@app.route('/')
def index():
    clothes = None
    if request.method == 'GET':
        clothes = request.args.to_dict(False)
    newDict = getWashingInstructionsForClothes(clothes)
    return render_template('index.html', list=newDict)


@app.route('/washing/')
def washing():
    newDict = {}
    washingDict = {}
    if request.method == 'GET':
        clothes = request.args.to_dict(False)
        newDict = getWashingInstructionsForClothes(clothes)
        washingDict = createWasherDictByClothes(newDict)
    return render_template('washing.html', list=newDict, washingDict=washingDict)


if __name__ == '__main__':
    app.run()
