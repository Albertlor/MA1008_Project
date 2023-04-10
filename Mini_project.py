# Author: Lor Wen Sin
# Done at 15/4/2022 , 21:40

import time
import turtle
import math

s = turtle.Screen()
s.setup(width = 1.0, height = 1.0)
s.setworldcoordinates(-30, -30, 30, 30)
t = turtle
t.hideturtle()
L = []
newL = []
vertexClick = 0
vertexType = 0
add = 0
delete = 0
edit = 0


### Draw the coordinate system
def grid():
    t.speed(0)
    for i in range(0,60,1):
          t.pencolor('grey')
          t.penup()
          t.setpos(-30+i,-30)
          if i==0:
             t.left(90)
          t.pendown()
          t.forward(60)
          t.backward(60)
    for i in range(0,60,1):
          t.pencolor('grey')
          t.penup()
          t.setpos(-30,-30+i)
          if i==0:
             t.right(90)
          t.pendown()
          t.forward(60)
          t.backward(60)
    t.penup()
    t.home()
    t.pendown()
    t.pencolor('black')
    t.backward(30)
    t.forward(60)
    t.backward(30)
    t.left(90)
    t.forward(30)
    t.backward(60)
    t.penup()
    t.setpos(0.25, -1)
    t.pendown()
    t.write(0)
    t.penup()
    t.setpos(29,0.25)
    t.pendown()
    t.write("x")
    t.penup()
    t.setpos(0.25,29)
    t.pendown()
    t.write("y")
    t.penup()

    for i in range(0, 55, 5):
        t.pencolor('black')
        t.penup()
        t.setpos(-25+i-0.25, -1)
        if -25+i != 0:
            t.pendown()
            t.write(-25+i)

    t.left(90)

    for j in range(0, 55, 5):
        t.pencolor('black')
        t.penup()
        t.setpos(0.25, -25+j-0.5)
        if -25+j != 0:
            t.pendown()
            t.write(-25+j)


### checking intersection for clicking method
def checkClick(x,y):
    global vertexClick
    global L
    global add
    Intersect1 = 0
    Intersect2 = 0
    last = len(L) -1

    if len(L) > 2:
        try:
            for k in range(len(L)-2):
                xp = L[k][0]
                yp = L[k][1]
                xq = L[k + 1][0]
                yq = L[k + 1][1]
                xn = L[last][0]
                yn = L[last][1]
                t2 = ((yp - yn) * (x - xn) - (xp - xn) * (y - yn)) / ((xq - xp) * (y - yn) - (yq - yp) * (x - xn))
                t1 = ((xp - xn) / (x - xn)) + t2 * ((xq - xp) / (x - xn))
                if (t1 >= 0 and t1 <= 1) and (t2 >= 0 and t2 <= 1):
                    Intersect1 += 1

            if len(L) == vertexClick - 1 or add == 1:
                for i in range(0, len(L) - 2):
                    xa = L[0][0]
                    ya = L[0][1]
                    xb = L[i + 1][0]
                    yb = L[i + 1][1]
                    xc = L[i + 2][0]
                    yc = L[i + 2][1]
                    t4 = ((yb - ya) * (x - xa) - (xb - xa) * (y - ya)) / (
                                (xc - xb) * (y - ya) - (yc - yb) * (x - xa))
                    t3 = ((xb - xa) / (x - xa)) + t4 * ((xc - xb) / (x - xa))
                    if (t3 >= 0 and t3 <= 1) and (t4 >= 0 and t4 <= 1):
                        Intersect2 += 1

            if Intersect1 != 0 or Intersect2 != 0:
                t.penup()
                t.goto(-5, -20)
                t.pendown()
                t.write("Invalid input, try again.", font=('Arial', 14, 'bold'))
                time.sleep(1.25)
                t.undo()
                t.penup()
            else:
                clicking(x,y)

        except ZeroDivisionError:
            t.penup()
            t.goto(-5, -20)
            t.pendown()
            t.write("Invalid input, try again.", font=('Arial', 14, 'bold'))
            time.sleep(1.25)
            t.undo()
            t.penup()
    else:
        clicking(x,y)


### Checking intersection for typing method
def checkType(x,y):
    global vertexType
    global L
    global edit

    Intersect1 = 0
    Intersect2 = 0
    last = len(L) -1
    if len(L) > 2:
        try:
            if edit != 1:
                for k in range(len(L)-2):
                    xp = L[k][0]
                    yp = L[k][1]
                    xq = L[k + 1][0]
                    yq = L[k + 1][1]
                    xn = L[last][0]
                    yn = L[last][1]
                    t2 = ((yp - yn) * (x - xn) - (xp - xn) * (y - yn)) / ((xq - xp) * (y - yn) - (yq - yp) * (x - xn))
                    t1 = ((xp - xn) / (x - xn)) + t2 * ((xq - xp) / (x - xn))
                    if (t1 >= 0 and t1 <= 1) and (t2 >= 0 and t2 <= 1):
                        Intersect1 += 1

                if len(L) == vertexType - 1  :
                    for i in range(0, len(L) - 2):
                        xa = L[0][0]
                        ya = L[0][1]
                        xb = L[i + 1][0]
                        yb = L[i + 1][1]
                        xc = L[i + 2][0]
                        yc = L[i + 2][1]
                        t4 = ((yb - ya) * (x - xa) - (xb - xa) * (y - ya)) / (
                                (xc - xb) * (y - ya) - (yc - yb) * (x - xa))
                        t3 = ((xb - xa) / (x - xa)) + t4 * ((xc - xb) / (x - xa))
                        if (t3 >= 0 and t3 <= 1) and (t4 >= 0 and t4 <= 1):
                            Intersect2 += 1
            else:
                for i in range(len(L)-3):
                    xa = L[i][0]
                    ya = L[i][1]
                    xb = L[i+1][0]
                    yb = L[i+1][1]
                    xc = L[last-1][0]
                    yc = L[last-1][1]
                    xn = L[last][0]
                    yn = L[last][1]
                    t2 = ((yc - ya) * (xb - xa) - (xc - xa) * (yb - ya)) / ((xn - xc) * (yb - ya) - (yn - yc) * (xb - xa))
                    t1 = ((xc - xa) / (xb - xa)) + t2 * ((xn - xc) / (xb - xa))
                    if (t1 >= 0 and t1 <= 1) and (t2 >= 0 and t2 <= 1):
                        Intersect1 += 1



            if Intersect1 != 0 or Intersect2 != 0:
                t.penup()
                t.goto(-5, -20)
                t.pendown()
                t.write("Invalid input, try again.", font=('Arial', 14, 'bold'))
                time.sleep(1.25)
                t.undo()
                t.penup()
            else:
                typing(x,y)

        except ZeroDivisionError:
            t.penup()
            t.goto(-5, -20)
            t.pendown()
            t.write("Invalid input, try again.", font=('Arial', 14, 'bold'))
            time.sleep(1.25)
            t.undo()
            t.penup()
    else:
        typing(x,y)


### Check whether the point lies in the polygon
def checkPoint(x, y):
    Intersect = 0
    global L

    for i in range(len(L) - 2):
        p = 9999999999999999 ### the line is extended to infinity
        q = 9999999999999999
        xa = L[i][0]
        ya = L[i][1]
        xb = L[i + 1][0]
        yb = L[i + 1][1]

        t2 = ((q - y) * (ya - y) - (p - x) * (xa - x)) / ((p - x) * (xb - xa) - (q - y) * (yb - ya))
        t1 = ((xa - x) / (q - y)) + t2 * ((xb - xa) / (q - y))
        if (t1 >= 0 and t1 <= 1) and (t2 >= 0 and t2 <= 1):
            Intersect += 1

    if Intersect % 2 != 0:  #inside the polygon
        move()


### To save the file before closing
def saveFile():
    global L
    save = t.textinput("Do you want to save your polygon?", "Y / N: ")
    if save == 'Y' or save == 'y':
        while True:
            try:
                new_filename = t.textinput("Enter a file name", "File Name: ")
                newFile = open(new_filename, 'a')
                break
            except OSError:
                print("File does not exist, please try again!")
        print(L, file=newFile)
        try:
            t.bye()
        except turtle.Terminator:
            pass
    if save == 'N' or 'n':
        try:
            t.bye()
        except turtle.Terminator:
            pass


### To close the file
def closeFile(x,y):
    t.penup()
    t.goto(-5, -20)
    t.pendown()
    t.pencolor('black')
    t.write("Press key 'S' to save file", font=('Arial', 14, 'bold'))
    s.onkeypress(saveFile, 's')
    s.listen()


### Construct the polygons by clicking method
def clicking(x,y):
    global L
    global add
    global edit
    global vertexClick

    t.goto(x, y)
    t.write(str(round(x, 2)) + ", " + str(round(y, 2)))
    L.append([x, y])

    if len(L) == vertexClick:
        t.begin_fill()
        for point in range(len(L)):
            t.pendown()
            t.goto(L[point][0], L[point][1])
        t.end_fill()
        s.onclick(closeFile)

    if add == 1:
        t.begin_fill()
        for point in range(len(L)):
            t.pendown()
            t.goto(L[point][0], L[point][1])
        t.end_fill()

        edit = t.textinput("Continue edit?", "Y / N")
        if edit == 'Y' or edit == 'y':
            s.onclick(editing)
        else:
            t.penup()
            t.goto(-10, -20)
            t.pendown()
            t.write("Press key 'M' to move your polygon, Click on the screen to close", font=('Arial', 14, 'bold'))
            s.onclick(closeFile)
            s.onkeypress(move, 'm')
            s.listen()


### Construct the polygon by typing method
def typing(x,y):
    global L
    global vertexType
    global delete
    global edit
    t.goto(x, y)
    t.write(str(round(x, 2)) + ", " + str(round(y, 2)))

    if edit != 1 and delete != 1:
        L.append([x, y])
        if len(L) == vertexType:
            t.begin_fill()
            for point in range(len(L)):
                t.pendown()
                t.goto(L[point][0], L[point][1])
            t.end_fill()
            s.onclick(closeFile)

    if edit != 1 and delete == 1:
        t.begin_fill()
        for i in range(len(L) + 1):
            pt = i % len(L)
            t.goto(L[pt][0], L[pt][1])
            t.pendown()
        t.end_fill()

        edit = t.textinput("Continue edit?", "Y / N")
        if edit == 'Y' or edit == 'y':
            s.onclick(editing)
        else:
            t.penup()
            t.goto(-10, -20)
            t.pendown()
            t.write("Press key 'M' to move your polygon, Click on the screen to close", font=('Arial', 14, 'bold'))
            s.onclick(closeFile)
            s.onkeypress(move, 'm')
            s.listen()


    if edit == 1 and delete != 1:
        t.begin_fill()
        for i in range(len(L) + 1):
            pt = i % len(L)
            t.goto(L[pt][0], L[pt][1])
            t.pendown()
        t.end_fill()

        edit = t.textinput("Continue edit?", "Y / N")
        if edit == 'Y' or edit == 'y':
            s.onclick(editing)
        else:
            t.penup()
            t.goto(-10, -20)
            t.pendown()
            t.write("Press key 'M' to move your polygon, Click on the screen to close", font=('Arial', 14, 'bold'))
            s.onclick(closeFile)
            s.onkeypress(move, 'm')
            s.listen()


### Edit the vertices of polygon by clicking
def editing(x, y):
    global L
    global add
    global delete
    global edit

    t.undo()
    minList = []
    for i in L:
        dist = math.sqrt((x - i[0]) ** 2 + (y - i[1]) ** 2)     # Find the distances of each polygon's coordinate to the point we click
        minList.append(dist)    # Store the distances in a new list
    coorMin = L[minList.index(min(minList))]    # Since the distances will be stored in sequence as the coordinates therefore the minimum distance will have same index of the corresponding coordinate
    xcor = float(coorMin[0])
    ycor = float(coorMin[1])

    minDist = min(minList)
    if minDist < 0.3:   # For the coordinate of polygon which has minimum distance to the point we click, if the minimum distance is small enough, then it is clicking the vertex of polygon
        t.penup()
        t.goto(xcor, ycor)
        t.pendown()
        t.write(str(round(xcor, 2)) + ", " + str(round(ycor, 2)))

        choice = t.textinput("Edit, Insert or Delete this vertex?", "E / I / D")
        if choice == 'E' or choice == 'e':
            edit = 1
            add = 0
            delete = 0
            coorMin[0] = float(t.textinput("Edit the x coordinate", "x = "))
            coorMin[1] = float(t.textinput("Edit the y coordinate", "y = "))
            t.clear()
            t.penup()
            last = len(L) - 1
            t.penup()
            t.goto(L[last][0], L[last][1])
            checkType(coorMin[0], coorMin[1])

        if choice == 'I' or choice == 'i':
            add = 1
            edit = 0
            delete = 0
            t.clear()
            t.penup()
            for i in range(len(L)):
                t.goto(L[i][0], L[i][1])
                t.write(str(round(L[i][0], 2)) + ", " + str(round(L[i][1], 2)))
            s.onclick(checkClick)

        if choice == 'D' or choice == 'd':
            delete = 1
            edit = 0
            add = 0
            if len(L) > 3:
                L.remove(coorMin)
                t.clear()
                t.penup()
                last = len(L) - 1
                t.goto(L[last][0], L[last][1])
                typing(L[0][0],L[0][1])

            else:
                t.penup()
                t.goto(-5, -20)
                t.pendown()
                t.write("No such polygon!", font = ("Arial", 14, "bold"))
                time.sleep(1.25)
                t.undo()
                s.onclick(editing)

    else:
        s.onclick(editing) # If the minimum distance is not small enough, means that it's not clicking the vertex, then click again.


### Pass the edit command to function 'editing'
def startEdit():
    t.penup()
    t.goto(0, -20)
    t.pencolor('black')
    t.pendown()
    t.write("Start editing", font=("Arial", 14, "bold"))
    time.sleep(1.25)
    t.undo()
    s.onclick(editing)


### Movement of polygon
def goUp():
    dy = 0.2
    for i in range(len(L)):
        L[i][1] += dy
    t.clear()
    t.penup()
    for j in range(len(L) + 1):
        i = j % len(L)
        t.goto(L[i][0], L[i][1])
        t.pendown()
        t.write(str(round(L[i][0], 2)) + ', ' + str(round(L[i][1], 2)))


def goDown():
    dy = 0.2
    for i in range(len(L)):
        L[i][1] -= dy
    t.clear()
    t.penup()
    t.begin_fill()
    for j in range(len(L) + 1):
        i = j % len(L)
        t.goto(L[i][0], L[i][1])
        t.pendown()
        t.write(str(round(L[i][0], 2)) + ', ' + str(round(L[i][1], 2)))
    t.end_fill()


def goRight():
    dx = 0.2
    for i in range(len(L)):
        L[i][0] += dx
    t.clear()
    t.penup()
    t.begin_fill()
    for j in range(len(L) + 1):
        i = j % len(L)
        t.goto(L[i][0], L[i][1])
        t.pendown()
        t.write(str(round(L[i][0], 2)) + ', ' + str(round(L[i][1], 2)))
    t.end_fill()


def goLeft():
    dx = 0.2
    for i in range(len(L)):
        L[i][0] -= dx
    t.clear()
    t.penup()
    t.begin_fill()
    for j in range(len(L) + 1):
        i = j % len(L)
        t.goto(L[i][0], L[i][1])
        t.pendown()
        t.write(str(round(L[i][0], 2)) + ', ' + str(round(L[i][1], 2)))
    t.end_fill()


def rotateCCW():
    theta = -5 * math.pi / 180
    for i in range(len(L)):
        L[i][0] = (math.cos(theta)) * (L[i][0]) + (math.sin(theta)) * (L[i][1])
        L[i][1] = (-math.sin(theta)) * (L[i][0]) + (math.cos(theta)) * (L[i][1])
    t.clear()
    t.penup()
    t.begin_fill()
    for j in range(len(L) + 1):
        i = j % len(L)
        t.goto(L[i][0], L[i][1])
        t.pendown()
        t.write(str(round(L[i][0], 2)) + ', ' + str(round(L[i][1], 2)))
    t.end_fill()


def rotateCW():
    theta = 5 * math.pi / 180
    for i in range(len(L)):
        L[i][0] = (math.cos(theta)) * (L[i][0]) + (math.sin(theta)) * (L[i][1])
        L[i][1] = (-math.sin(theta)) * (L[i][0]) + (math.cos(theta)) * (L[i][1])
    t.clear()
    t.penup()
    t.begin_fill()
    for j in range(len(L) + 1):
        i = j % len(L)
        t.goto(L[i][0], L[i][1])
        t.pendown()
        t.write(str(round(L[i][0], 2)) + ', ' + str(round(L[i][1], 2)))
    t.end_fill()


def scaleUp():
    scaleFac = 1.05
    for i in range(len(L)):
        L[i][0] *= scaleFac
        L[i][1] *= scaleFac
    t.clear()
    t.penup()
    t.begin_fill()
    for j in range(len(L) + 1):
        i = j % len(L)
        t.goto(L[i][0], L[i][1])
        t.pendown()
        t.write(str(round(L[i][0], 2)) + ', ' + str(round(L[i][1], 2)))
    t.end_fill()


def scaleDown():
    scaleFac = 1.05
    for i in range(len(L)):
        L[i][0] /= scaleFac
        L[i][1] /= scaleFac
    t.clear()
    t.penup()
    t.begin_fill()
    for j in range(len(L) + 1):
        i = j % len(L)
        t.goto(L[i][0], L[i][1])
        t.pendown()
        t.write(str(round(L[i][0], 2)) + ', ' + str(round(L[i][1], 2)))
    t.end_fill()


### Function to control the movement of polygon
def move():
    t.undo()
    t.penup()
    t.goto(-5, -24)
    t.pendown()
    t.write("Start to move your polygon!", font=("Arial", 14, "bold"))
    time.sleep(1.25)
    t.undo()

    s.onkeypress(goUp, 'Up')
    s.listen()

    s.onkeypress(goDown, 'Down')
    s.listen()

    s.onkeypress(goRight, 'Right')
    s.listen()

    s.onkeypress(goLeft, 'Left')
    s.listen()

    s.onkeypress(rotateCCW, '1')
    s.listen()

    s.onkeypress(rotateCW, '2')
    s.listen()

    s.onkeypress(scaleUp, 'u')
    s.listen()

    s.onkeypress(scaleDown, 'd')
    s.listen()

    s.onclick(closeFile)


### Calculate the perimeter of polygon
def peri():
    t.pencolor('black')
    perimeter = 0
    for i in range(len(L) - 1):
        length = math.sqrt((L[i + 1][0] - L[i][0]) ** 2 + (L[i + 1][1] - L[i][1]) ** 2)
        perimeter += length
        if i == len(L) -2:
            perimeter += math.sqrt((L[-1][0] - L[0][0]) ** 2 + (L[-1][1] - L[0][1]) ** 2)
    t.penup()
    t.goto(-6, -25)
    t.pendown()
    t.write("Perimeter is: ", font=("Arial", 14, "bold"))

    t.penup()
    t.goto(-1, -25)
    t.pendown()
    t.write(round(perimeter, 2), font=("Arial", 14, "bold"))


### Calculate the area of polygon
def area():
    t.pencolor('black')
    areaTot = 0
    for i in range(len(L)-2):
        A = [ L[i + 1][0] - L[0][0], L[i + 1][1] - L[0][1] ]
        B = [ L[i + 2][0] - L[0][0], L[i + 2][1] - L[0][1] ]
        areaTri =  1/2 * ( A[0] * B[1] - A[1] * B[0] )
        areaTot += areaTri

    t.penup()
    t.goto(3, -25)
    t.pendown()
    t.write("Area is: ", font=("Arial", 14, "bold"))

    t.penup()
    t.goto(6, -25)
    t.pendown()
    t.write(round(areaTot, 2), font=("Arial", 14, "bold"))

    s.onclick(closeFile)


### To pass the coordinate to function 'checkPoint' after selecting the polygon
def select():
    s.onclick(checkPoint)


### To duplicate the polygon
def duplicate():
    global L
    global newL
    dx = float(t.textinput("Shift in x direction", "x-shifting"))
    dy = float(t.textinput("Shift in y direction", "y-shifting"))

    newL = L.copy()
    pen = t.textinput("Choose your pen color", "Pen Color")
    fill = t.textinput("Choose your fill color", "Fill Color")
    t.color(pen, fill)
    t.pensize(4)
    t.penup()
    t.begin_fill()
    for j in range(len(L) + 1):
        if j != len(L):
            newL[j][0] += dx
            newL[j][1] += dy
        i = j % len(L)
        t.goto(newL[i][0], newL[i][1])
        t.pendown()
        t.write(str(round(newL[i][0], 2)) + ', ' + str(round(newL[i][1], 2)))
    t.end_fill()
    t.pencolor('black')
    t.penup()
    t.goto(-5, -25)
    t.pendown()
    t.write("Polygon duplicated succesfully!", font=("Arial", 14, "bold"))
    time.sleep(1.25)
    t.undo()
    t.penup()

    s.onclick(buttonSelect)
    s.listen()


### Fucntions for choosing button 'Click'
def buttonClick(x,y):
    while True:
        try:
            global vertexClick
            vertexClick = int(t.textinput("Please enter the total vertices", "Vertices"))
            pen = t.textinput("Choose your pen color", "Pen Color")
            fill = t.textinput("Choose your fill color", "Fill Color")
            t.color(pen, fill)
            t.pensize(4)
            s.onclick(checkClick)
            break

        except ValueError:
            t.penup()
            t.goto(-10, -20)
            t.write("Invalid input, please try again!", font = ("Arial", 12, "bold"))
            time.sleep(1.25)
            t.undo()

        except turtle.TurtleGraphicsError:
            t.penup()
            t.goto(-10, -20)
            t.write("Invalid input, please try again!", font=("Arial", 12, "bold"))
            time.sleep(1.25)
            t.undo()


### Functions for choosing button 'Type'
def buttonType(x,y):
    while True:
        try:
            global vertexType
            vertexType = int(t.textinput("Please enter the total vertices", "Vertices"))
            pen = t.textinput("Choose your pen color", "Pen Color")
            fill = t.textinput("Choose your fill color", "Fill Color")
            t.color(pen, fill)
            t.pensize(4)
            while True:
                x = float(t.textinput("Enter an x coordinates", "x"))
                y = float(t.textinput("Enter a y coordinates", "y"))
                checkType(x, y)
                if len(L) == vertexType:
                    break
            break

        except ValueError:
            t.penup()
            t.goto(-10, -20)
            t.write("Invalid input, please try again!", font = ("Arial", 12, "bold"))
            time.sleep(1.25)
            t.undo()

        except turtle.TurtleGraphicsError:
            t.penup()
            t.goto(-10, -20)
            t.write("Invalid input, please try again!", font=("Arial", 12, "bold"))
            time.sleep(1.25)
            t.undo()

### Retrieve and edit polygons
def buttonEdit(x,y):
    global edit
    global L

    while True:
        try:
            filename = t.textinput("Enter a file name", "File Name: ")
            myFile = open(filename, 'r')
            break
        except OSError:
            t.penup()
            t.goto(-5, -25)
            t.pendown()
            t.pencolor('black')
            t.write("File does not exist, try again!", font=("Arial", 14, "bold"))
            time.sleep(1.25)
            t.undo()

    pen = t.textinput("Choose your pen color", "Pen Color")
    fill = t.textinput("Choose your fill color", "Fill Color")
    t.color(pen, fill)
    t.pensize(4)

    ### Construct button 'Select'
    t.pencolor('black')
    t.setheading(0)
    t.penup()
    t.goto(-30, 27)
    for i in range(2):
        t.pendown()
        t.speed(0)
        t.forward(3.5)
        t.left(90)
        t.forward(3)
        t.left(90)
    t.penup()
    t.goto(-29.3, 27.5)
    t.pendown()
    t.write("Select", font=('Arial', 14, 'bold'))
    t.penup()


    for line in myFile:
        t.pencolor(pen)
        ptList = line.strip("[[").strip(']]\r\n').split('], [')
        t.begin_fill()
        for i in range(len(ptList) + 1):
            t.penup()
            pt = i % len(ptList)
            formatted = ptList[pt].split(",")
            first = float(formatted[0])
            second = float(formatted[1])
            t.goto(first, second)
            t.pendown()
        t.end_fill()
        for pt in range(len(ptList)):
            formatted = ptList[pt].split(",")
            first = float(formatted[0])
            second = float(formatted[1])
            L.append([first, second])    #store the coordinates of polygon interested in a list

    t.penup()
    t.goto(-10, -20)
    t.pendown()
    t.pencolor('black')
    t.write("Press key 'E' to edit your polygon, Press key 'C' to duplicate", font=("Arial", 14, "bold"))
    time.sleep(2)
    t.undo()
    s.onkeypress(startEdit, 'e')  # click to select a vertex of the polygon
    s.listen()
    s.onkeypress(move, 'm')
    s.listen()
    s.onkeypress(duplicate, 'c')
    s.listen()
    s.onclick(buttonSelect)


### Functions for choosing the button 'Calculate'
def buttonCal(x,y):
    global L
    while True:
        try:
            filename = t.textinput("Enter a file name", "File Name: ")
            myFile = open(filename, 'r')
            break
        except OSError:
            t.penup()
            t.goto(-5, -25)
            t.pendown()
            t.pencolor('black')
            t.write("File does not exist, try again!", font=("Arial", 14, "bold"))
            time.sleep(1.25)
            t.undo()

    pen = t.textinput("Choose your pen color", "Pen Color")
    fill = t.textinput("Choose your fill color", "Fill Color")
    t.pensize(4)
    t.penup()
    for line in myFile:
        t.color(pen, fill)
        ptList = line.strip("[[").strip(']]\r\n').split('], [')
        t.begin_fill()
        for i in range(len(ptList) + 1):
            pt = i % len(ptList)
            formatted = ptList[pt].split(",")
            first = float(formatted[0])
            second = float(formatted[1])
            t.goto(first, second)
            t.pendown()
        t.end_fill()
        for pt in range(len(ptList)):
            formatted = ptList[pt].split(",")
            first = float(formatted[0])
            second = float(formatted[1])
            L.append([first, second])    #store the coordinates of polygon of interest in a list

    peri()
    area()


### Funtions for choosing the button 'Select'
def buttonSelect(x,y):
    if -30 < x < -26.5 and 27 < y < 30:
        t.penup()
        t.goto(-3, -25)
        t.pendown()
        t.pencolor('black')
        t.write("Select your polygon", font=("Arial", 14, "bold"))
        time.sleep(1.25)
        t.undo()
        select()


### Decide which button to click ('Click' , 'Type', 'Edit', or 'Calculate')
def choose(x, y):
    if x > -2 and x < 4 and y > -12 and y < -8.5:
        t.clear()
        grid()
        t.penup()
        buttonClick(x,y)

    if x > -2 and x < 4 and y > -15.5 and y < -12:
        t.clear()
        grid()
        t.penup()
        buttonType(x,y)

    if x > -2 and x < 4 and y > -19 and y < -15.5:
        t.clear()
        grid()
        buttonEdit(x,y)

    if x > -2 and x < 4 and y > -22.5 and y < -19:
        t.clear()
        buttonCal(x,y)


### Design
### Code from https://youtu.be/UjQrJu8wJbA, by Author: Geek Tutorials
t.speed(0)
t.bgcolor("skyblue")

# Grass
t.penup()
t.goto(-30, -7.5)
t.pendown()
t.color("limegreen")
t.begin_fill()
for i in range(2):
    t.forward(60)
    t.right(90)
    t.forward(30)
    t.right(90)
t.end_fill()

# Left Mountain
t.penup()
t.goto(-30, -7.5)
t.pendown()
t.color("dimgray")
t.begin_fill()
for i in range(3):
    t.forward(22.5)
    t.left(120)
t.end_fill()

# Right Mountain
t.penup()
t.goto(7.5, -7.5)
t.pendown()
t.begin_fill()
for i in range(3):
    t.forward(22.5)
    t.left(120)
t.end_fill()

# Middle Mountain
t.penup()
t.goto(-12, -7.5)
t.pendown()
t.color("gray")
t.begin_fill()
for i in range(3):
    t.forward(30)
    t.left(120)
t.end_fill()

# Middle Mountain Ice Cap
t.penup()
t.goto(-2.625, 9)
t.pendown()
t.color("white")
t.begin_fill()
t.left(35)
t.forward(4.5)
t.right(90)
t.forward(2.25)
t.left(100)
t.forward(3.375)
t.right(85)
t.forward(4.875)
t.left(160)
t.forward(11.25)
t.end_fill()

# Left Mountain Ice Cap
t.penup()
t.goto(-16.125, 7.5)
t.pendown()
t.color("snow")
t.begin_fill()
t.forward(5.25)
t.left(120)
t.forward(5.625)
t.left(150)
t.forward(3.375)
t.right(90)
t.forward(3.375)
t.left(120)
t.end_fill()

# Right Mountain Ice Cap
t.penup()
t.goto(15.225, 6)
t.pendown()
t.begin_fill()
t.forward(7.125)
t.right(120)
t.forward(6)
t.right(150)
t.forward(3.75)
t.left(70)
t.end_fill()

t.left(50)

# Sun
t.penup()
t.goto(-37.5, 26.25)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(9.375)
t.end_fill()


# Tree
def tree():
    # Tree trunk
    t.color("saddlebrown")
    t.begin_fill()
    for i in range(2):
        t.forward(3)
        t.left(90)
        t.forward(0.75)
        t.left(90)
    t.end_fill()

    # Turn the turtle around
    t.forward(0.75)
    t.left(90)
    t.forward(0.375)

    # Leaves on tree
    t.color("forestgreen")
    t.begin_fill()
    t.circle(1.875)
    t.end_fill()

    t.right(90)


# Plant the first tree
t.penup()
t.goto(15, -11.25)
t.pendown()
tree()

# Plant the second tree
t.penup()
t.goto(22.5, -18.75)
t.pendown()
tree()

# Plant the third tree
t.penup()
t.goto(-22.5, -18.75)
t.pendown()
tree()

# Plant the forth tree
t.penup()
t.goto(-15, -7.5)
t.pendown()
tree()
t.penup()

### Construct button 'Click'
t.home()
t.pencolor('black')
t.speed(0)
t.penup()
t.goto(-2,-12)
t.color('CornflowerBlue', 'AliceBlue')
t.pensize(3)
t.begin_fill()
for i in range(2):
    t.pendown()
    t.speed(0)
    t.forward(6)
    t.left(90)
    t.forward(3.5)
    t.left(90)
t.end_fill()
t.penup()
t.goto(-0.5, -11.6)
t.pendown()
t.write("Click", font=('Elephant', 20, 'bold'))
t.penup()


### Construct button 'Type'
t.penup()
t.goto(-2,-15.5)
t.color('CornflowerBlue', 'AliceBlue')
t.pensize(3)
t.begin_fill()
for i in range(2):
    t.pendown()
    t.speed(0)
    t.forward(6)
    t.left(90)
    t.forward(3.5)
    t.left(90)
t.end_fill()
t.penup()
t.goto(-0.5, -15.1)
t.pendown()
t.write("Type", font=('Elephant', 20, 'bold'))
t.penup()


### Construct button 'Edit'
t.penup()
t.goto(-2,-19)
t.color('CornflowerBlue', 'AliceBlue')
t.pensize(3)
t.begin_fill()
for i in range(2):
    t.pendown()
    t.speed(0)
    t.forward(6)
    t.left(90)
    t.forward(3.5)
    t.left(90)
t.end_fill()
t.penup()
t.goto(-0.2, -18.6)
t.pendown()
t.write("Edit", font=('Elephant', 20, 'bold'))
t.penup()

### Construct button 'Calculate'
t.penup()
t.goto(-2,-22.5)
t.color('CornflowerBlue', 'AliceBlue')
t.pensize(3)
t.begin_fill()
for i in range(2):
    t.pendown()
    t.speed(0)
    t.forward(6)
    t.left(90)
    t.forward(3.5)
    t.left(90)
t.end_fill()
t.penup()
t.goto(-1.7, -22.1)
t.pendown()
t.write("Calculate", font=('Elephant', 20, 'bold'))
t.penup()


###Theme
t.goto(-28, -2)
t.pendown()
t.pencolor('royalblue')
t.write("WELCOME TO POLYGON VILLAGE !", font=('Elephant', 50, 'bold'))



s.onclick(choose)
t.listen()
s.listen()
s.mainloop()

