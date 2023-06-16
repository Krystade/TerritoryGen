from random import randint
import sys, math

def printGrid():
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    gridStr = ""
    for i in range(height):
        gridStr += "\n"
        for j in range(width):
            if(grid[i][j] == " ##"):
                gridStr += str(grid[i][j])#print(grid[i][j], end = ' ')
            elif(grid[i][j] < 10 and grid[i][j] >= 0):
                gridStr += " 0" + str(grid[i][j])#color.write(" 0" + str(grid[i][j]) + " ", colors[int(grid[i][j])%len(colors)])
            else:
                gridStr += " " + str(grid[i][j])#color.write(" " + str(grid[i][j]) + " ", colors[int(grid[i][j])%len(colors)])
        #print()
        #print()
    print(gridStr)

    
def printGridColor():
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    gridStr = ""
    for i in range(height):
        gridStr += "\n"
        for j in range(width):
            if(grid[i][j] == " ##"):
                print(grid[i][j], end = ' ')
            elif(grid[i][j] < 10 and grid[i][j] >= 0):
                color.write(" 0" + str(grid[i][j]) + " ", colors[int(grid[i][j])%len(colors)])
            else:
                color.write(" " + str(grid[i][j]) + " ", colors[int(grid[i][j])%len(colors)])
        print("\n")
        

def printGridFast():
    prev = ""
    strings = [[]]
    count = -1
    for i in range(height):
        count += 1
        strings.append([""])
        strings[count] = ["\n"]
        prev = ""
        for j in range(width):
            if(prev == grid[i][j]):
                if(grid[i][j] < 10 and grid[i][j] >= 0):
                    strings[count].append(" 0" + str(grid[i][j]) + " ")
                else:
                    strings[count].append(" " + str(grid[i][j]) + " ")
            else:
                if(grid[i][j] < 10 and grid[i][j] >= 0):
                    strings.append([" 0" + str(grid[i][j]) + " "])
                else:
                    strings.append([" " + str(grid[i][j]) + " "])
                count += 1
            #print("\n", i, j, count, prev, grid[i][j], strings, "\n")
            prev = grid[i][j]
    for i in range(len(strings)):
        for j in range(len(strings[i])):
            print(strings[i][j], end = '')


def updateGrid():
    for i in range(len(factionPos)):
        for j in range(len(factionPos[i])):
            xPos = factionPos[i][j][0]
            yPos = factionPos[i][j][1]
            if [xPos, yPos] not in surrounded:
                openSpace = False
                if(xPos + 1 <= height - 1 and grid[xPos + 1][yPos] == " ##"):
                    if([xPos + 1, yPos] not in factionPos[i]):
                        skip = False
                        for k in range(len(factionPos)):
                            if([xPos + 1, yPos] in factionPos[k]):
                                       skip = True
                                       break
                        if not skip:
                            factionPos[i].append([xPos + 1, yPos])
                            grid[xPos + 1][yPos] = i
                            openSpace = True
                if(xPos - 1 >= 0 and grid[xPos - 1][yPos] == " ##"):
                    if([xPos - 1, yPos] not in factionPos[i]):
                        skip = False
                        for k in range(len(factionPos)):
                            if([xPos, yPos + 1] in factionPos[k]):
                                       skip = True
                                       break
                        if not skip:
                            factionPos[i].append([xPos - 1, yPos])
                            grid[xPos - 1][yPos] = i
                            openSpace = True
                if(yPos + 1 <= width - 1 and grid[xPos][yPos + 1] == " ##"):
                    if([xPos, yPos + 1] not in factionPos[i]):
                        skip = False
                        for k in range(len(factionPos)):
                            if([xPos, yPos + 1] in factionPos[k]):
                                       skip = True
                                       break
                        if not skip:
                            factionPos[i].append([xPos, yPos + 1])
                            grid[xPos][yPos + 1] = i
                            openSpace = True
                if(yPos - 1 >= 0 and grid[xPos][yPos - 1] == " ##"):
                    if([xPos, yPos - 1] not in factionPos[i]):
                        skip = False
                        for k in range(len(factionPos)):
                            if([xPos, yPos - 1] in factionPos[k]):
                                       skip = True
                                       break
                        if not skip:
                            factionPos[i].append([xPos, yPos - 1])
                            grid[xPos][yPos - 1] = i
                            openSpace = True
                if not openSpace:
                    surrounded.append([xPos, yPos])
            #grid[factionPos[i][j][0]][factionPos[i][j][1]] = factions[i]
            grid[factionPos[i][j][0]][factionPos[i][j][1]] = i
            

width = int(input("How many columns(x)? "))
height = int(input("How many rows(y)? "))
grid = []
#Array for all the spaces that dont need to be checked. surrounded area filled
surrounded = []
#7 different colors
colors = ["DEFINITION", "STRING", "COMMENT", "TODO", "KEYWORD", "console", "BUILTIN"]
#27 letters
factions = [" O ", " X ", " Z ", " R ", " A ", " B ", " C ", " D ", " E ", " F ", " G ", " H ", " I ", " J ", " K ", " L ", " M ", " N ", " P ", " Q ", " S ", " T ", " U ", " V ", " W ", " Y "]
#factions = [" / ", " \ ", " | ", " - ", " _ "]
numFactions = int(input("How many factions do you want? "))
while numFactions > 100:
    print("\nToo many factions! pick at most 100.")
    numFactions = int(input("How many factions do you want? "))
factionPos = []

for i in range(height):
    grid.append([" ##"])
    for j in range(width - 1):
        grid[i].append(" ##")


for i in range(numFactions):
    randW = randint(0, height - 1)
    randH = randint(0, width - 1)
    #Need this while loop and reset var to reset j to 0 so every previous pos gets checked when a dupe is found and changed
    reset = True
    while reset:
        reset = False
        #Check every already assigned starting position
        for j in range(i):
            #Generate a new value to try and get a non duplicate
            if([randW, randH] == factionPos[j][0]):
                reset = True
                randW = randint(0, height - 1)
                randH = randint(0, width - 1)
                break
    pos = [randW, randH]
    factionPos.append([pos])

for i in range(len(factionPos)):
    #print([factionPos[i][0][0], factionPos[i][0][1]], factions[i])
    grid[factionPos[i][0][0]][factionPos[i][0][1]] = i

run = True
updates = 0
printGrid()
while run:
    run = False
    #Check for open spaces
    for i in range(len(grid)):
        #If there is an open space, keep growing territories
        if " ##" in grid[i]:
            run = True
            break
    updateGrid()
    #total number of spaces filled
    total = 0
    for i in range(len(factionPos)):
        total += len(factionPos[i])
    if(updates%5 == 0):
        print()
    print("Step " + str(updates + 1) + ": " + str(total) + " Spaces Filled, " + str(math.floor(total*100/(width*height))) + "%.\t", end = '')
    if(total < 1000 or math.floor(total*100/(width*height)) < 10 or updates + 1 < 10):
        print("\t", end = '')
    updates += 1


try:
    color = sys.stdout.shell
    printGridColor()
except AttributeError:
    printGrid()
    input("Generation Complete. Press Enter to close.")
#printGridFast()
    
#for i in range(len(factionPos)):
#   print(factionPos[i])
    
