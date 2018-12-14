from turtle import speed, exitonclick, hideturtle, penup, setposition, dot, pendown, goto, setup, Screen, Turtle, tracer, update
import json
X = []
Y = []
features = []
scale_X = []
scale_Y = []


def nahrani_dat():

    with open('export.geojson') as f:
        data = json.load(f)
    for feature in data ['features']:
        X.append(feature['geometry']['coordinates'][0])
        Y.append(feature['geometry']['coordinates'][1])
        features.append(feature['geometry']['coordinates'])

    return (X, Y, features)





def oblast():
    UL_point = [min(X),max(Y)]
    UR_point = [max(X),max(Y)]
    LL_point = [min(X),min(Y)]
    LR_point = [max(X),min(Y)]
    return (UL_point, UR_point, LL_point, LR_point)



def preskalovani_X():
    stred_X = (max(X) + min(X)) / 2

    for a in range(len(X)):
        b = (X[a] - stred_X) * 10000
        scale_X.append(b)
    return(scale_X, stred_X)


def preskalovani_Y():
    stred_Y = (max(Y) + min(Y)) / 2
    for a in range(len(Y)):
        b = (Y[a] - stred_Y) * 10000
        scale_Y.append(b)
    return(scale_Y, stred_Y)


def ukaz_data():
    penup()
    hideturtle()
    tracer(0,0)
    for a in range(len(scale_X)):
        goto(scale_X[a],scale_Y[a])
        dot()
    update()
nahrani_dat()
oblast()
preskalovani_X()
preskalovani_Y()

print(X)
print(Y)
print(scale_X)
print(scale_Y)

ukaz_data()
#ukaz_data()


exitonclick()