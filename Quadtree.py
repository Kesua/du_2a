from turtle import speed, exitonclick, hideturtle, penup, setposition, dot, pendown, goto, setup, Screen, Turtle
import json
X = []
Y = []
features = []
def nahrani_dat():

    with open('export.geojson') as f:
        data = json.load(f)
    for feature in data ['features']:
        X.append(feature['geometry']['coordinates'][0])
        Y.append(feature['geometry']['coordinates'][1])
        features.append(feature['geometry']['coordinates'])

    return (X,Y,features)

def oblast():
    X_data = sorted(X)
    Y_data = sorted(Y)
    print(X_data)
    print(Y_data)
    pocet_prvku = len(X_data)
    UL_point = [X_data[0],Y_data[pocet_prvku-1]]
    UR_point = [X_data[pocet_prvku-1],Y_data[pocet_prvku-1]]
    LL_point = [X_data[0],Y_data[0]]
    LR_point = [X_data[pocet_prvku-1],Y_data[0]]
    print(UL_point)
    print(UR_point)
    print(LR_point)
    print(LL_point)
    pendown()
    goto(UL_point)
    goto(UR_point)
    goto(LR_point)
    goto(LL_point)
    goto(UL_point)
    penup()
    return(UL_point, UR_point, LL_point, LR_point)

nahrani_dat()
print(X)
print(Y)
print(features)
speed(1)
oblast()

#ukaz_data()


exitonclick()