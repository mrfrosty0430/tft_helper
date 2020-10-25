import json
import string
from tkinter import *

def buildTraits(champs):
    champFile = open("champions.json")
    champData = json.load(champFile)
    traitFile = open("traits.json")
    traitData = json.load(traitFile)

    traits = dict()
    for user_champ in champs:

        for champ in champData:
            if champ["name"] == (user_champ).strip():
                traits[(user_champ).strip()] = champ["traits"]
                break
    return traits




def init(data):

	data.time = 0



def timerFired(data):

	# print(data.time)

	# data.time+=data.timerDelay

	pass



def addChamp(champ):
    print(champ)



def redrawAll(canvas,data):
    champFile = open("champions.json")
    champData = json.load(champFile)
    photoList = []
    i = 0
    factor = 32
    limit = data.width//factor

    
    
    for champ in champData:
        champID = champ["championId"]
        photo = PhotoImage(file="champions/" + champID+".png" )
        b = Button(canvas, text = champID, height=factor, width =factor, image = photo, command=lambda: addChamp(champ))
        b.pack()
        b.place(x=i%limit * factor, y=i // limit * factor)
        photoList.append(b)
##        print(photo)
        label = Label(image=photo)
        label.image=photo
        photoList.append(label.image)
##        label.pack()

        i += 1








def mousePressed(event,data):
	pass

def keyPressed(event,data):
	pass
    
def getChamp(apiKey):
	myChamp = input("choose your champion \n")
	yourChamp = input("choose your enemy chamipon \n")
	with open("data/champion/" + myChamp + ".json") as file:
		data = json.load(file)
	print(data["data"][myChamp]["stats"])
	baseSpeed = 0.625
	stats = data["data"][myChamp]["stats"]
	myASOffset = round(stats["attackspeedoffset"],3)
	myBaseAS = round(baseSpeed/(1+myASOffset),3)
	myASLevel = round(stats["attackspeedperlevel"],3)
	print(myASOffset,myBaseAS,myASLevel)



def run(width, height):

    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()



    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)



    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)



    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    # Set up data and call init

    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")











def start():
    apiKey = "RGAPI-9fa98d84-5df6-46d9-ae80-f8a1f71827a2"
    itemFile = open("items.json")
    itemData = json.load(itemFile)

    champFile = open("champions.json")
    champData = json.load(champFile)
    print(champData)

    traitFile = open("traits.json")
    traitData = json.load(traitFile)
    print(traitData)

    champ_input = input("choose champions, separated with a comma\n")
    print(champ_input)

    champs = champ_input.split(",")
    print(champs)
    champTraits = buildTraits(champs)
    print(champTraits)
    traitCount = dict()
    for champ in champTraits:
        print(champ)
        for trait in champTraits[champ]:
            traitCount[trait] = traitCount.get(trait, 0) + 1

    print(traitData[0])

    traitSynergy = dict()
    for user_trait in traitCount:
        for trait in traitData:
            if trait["key"] == user_trait:
                trait_val = traitCount[user_trait]
                trait_label = "n/a"
                for label in trait["sets"]:
                    label_min = label["min"]
                    if traitCount[user_trait] >= label_min:
                        trait_label = label["style"]
                traitSynergy[trait["name"]] = (trait_label,traitCount[user_trait])
    print(traitSynergy)
    run (500,500)



if _name_ == "_main_":
    start()
