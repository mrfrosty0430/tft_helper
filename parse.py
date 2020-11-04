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



def addChamp(data,i,champData):
    factor = 64
    limit = data.width//factor
    row = data.mousey//factor
    col = data.mousex // factor
    print(i,champData[int(row*limit+col)])




def redrawAll(canvas,data):
    champFile = open("champions.json")
    champData = json.load(champFile)
    photoList = []
    i = 0
    factor = 64
    limit = data.width//factor



    for champ in champData:
        champID = champ["championId"]
        photo = PhotoImage(file="champions/" + champID+".png" )
        b = Button(canvas, text = champID, height=factor, width =factor, image = photo, command=lambda: addChamp(data,i,champData))
        b.place(x=i%limit * factor, y=i // limit * factor)
        b.pack()
        label = Label(image=photo)
        label.image=photo
        photoList.append(photo)

        i += 1









def mousePressed(event,data):
	print(data.mousex,data.mousey)

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

    def set_motion(event,canvas, data):
        data.mousex=canvas.canvasx(event.x)
        data.mousey=canvas.canvasy(event.y)

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
##    def motion(event):
##    x, y = event.x, event.y
##    print('{}, {}'.format(x, y))

    root.bind('<Motion>', lambda event: set_motion(event,canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")











def start():
    apiKey = ### insert api key here ###
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



if __name__ == "__main__":
    start()
