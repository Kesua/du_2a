from turtle import speed, exitonclick, hideturtle, penup, setposition, dot, pendown, forward, left, goto, setup,setworldcoordinates, Turtle, tracer, update
from operator import itemgetter
import json


def ukaz_data():
    """
    Vykresluje data
    :return:
    """
    setworldcoordinates(min(X), min(Y), max(X), max(Y))
    penup()
    hideturtle()

    tracer(0, 0)
    for a in range(len(X)):
        goto(X[a], Y[a])
        dot()
    update()


def vykresli_oblast(bound):
    """
    Vykresluje ctverce, respektive obdelniky podle charakteru dat
    :param bound: boundary box
    :return:
    """
    tracer(0,0)
    hideturtle()
    penup()
    goto(bound[0], bound[1])
    pendown()
    forward(abs(bound[2]-bound[0]))
    left(90)
    forward(abs(bound[3]-bound[1]))
    left(90)
    forward(abs(bound[2]-bound[0]))
    left(90)
    forward(abs(bound[3]-bound[1]))
    left(90)
    penup()
    update()


def body_v_oblasti(body, bound, quad):
    """
    definuje body, ktere se nachazeji v danem bounding boxu
    :param body: vstupni list s daty geojson
    :param bound: bounding box
    :param oblast:
    :return:body v bounding boxu
    """
    B = []
    for a in range(len(body)):

        ID = body[a][0]
        x = body[a][1]
        y = body[a][2]
        ex_kod = body[a][3]
        novy_kod = ex_kod + str(quad)
        if bound[0] <= x <= bound[2] and bound[1] <= y <= bound[3]:
            B.append([ID, x, y, novy_kod])
        else:
            continue
    return B

def quadtree(body_v, body_mimo, bound, quad=0, velikost = 10):
    """
    Vlastni quadtree
    :param body_v: vstupni data
    :param body_mimo: vystupni data + ID  bounding boxu, ve kterem se nachazi
    :param bound: bounding box
    :param quad: cislo bounding boxu
    :param velikost: maximalni pocet clenu skupiny
    :return: vysledne body
    """
    if len(body_v) <= velikost:  # ukonceni rekurze
        vykresli_oblast(bound)
        for point in body_v:
            body_mimo.append(point)  # vystupni seznam bodu
        return
    else:
        stred = [(bound[0] + bound[2]) / 2, (bound[1] + bound[3]) / 2]
        quad_1 = [stred[0], stred[1], bound[2], bound[3]]
        quad_2 = [stred[0], bound[1], bound[2], stred[1]]
        quad_3 = [bound[0], bound[1], stred[0], stred[1]]
        quad_4 = [bound[0], stred[1], stred[0], bound[3]]
        B1 = body_v_oblasti(body_v, quad_1, 1)
        B2 = body_v_oblasti(body_v, quad_2, 2)
        B3 = body_v_oblasti(body_v, quad_3, 3)
        B4 = body_v_oblasti(body_v, quad_4, 4)
        vykresli_oblast(bound)
        quadtree(B1, body_mimo, quad_1, 1, numclen)  # rekurze fce v danem bounding boxu
        quadtree(B2, body_mimo, quad_2, 2, numclen)
        quadtree(B3, body_mimo, quad_3, 3, numclen)
        quadtree(B4, body_mimo, quad_4, 4, numclen)
    return body_mimo



X = []
Y = []
body = []
numclen = int(input("Zadejte pozadovany pocet clenu ve skupine")) # definice velikosti skupiny
with open('export.geojson') as f: # nahrani souboru geojson
    data = json.load(f)
for i, feature in enumerate(data['features']): # vytvoreni vstupnich seznamu
    X.append(feature['geometry']['coordinates'][0])
    Y.append(feature['geometry']['coordinates'][1])
    features = feature['geometry']['coordinates']
    body.append([i, features[0], features[1], ""])
bound=[min(X), max(X), min(Y), max(Y)] # vytvoreni zakladniho boundin boxu
ukaz_data()
body_mimo = [] # vytvoreni seznamu pro vysledne body
body_mimo = quadtree(body, body_mimo, bound, velikost = numclen)
ID_body_mimo = (sorted(body_mimo,key=itemgetter(0)))

for i, value in enumerate(data['features']):
    value['properties']['cluster_id'] = ID_body_mimo[3]


with open('import.geojson', 'w') as out:  #ulozeni vystupniho souboru jako import.geojson
    json.dump(data, out)


exitonclick()