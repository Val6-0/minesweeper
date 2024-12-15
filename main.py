import random
import copy
def creerGrille(N, M, v = 0):
    li = []
    res = []
    for i in range(M):
        li.append(v)
    for i in range(N):
        res.append(li.copy())
    return res

def placerMines(grille, X):
    for i in range(X):
        co1 = random.randint(0, len(grille) - 1)
        co2 = random.randint(0, len(grille[0]) - 1)
        while grille[co1][co2] != 0:
            co1 = random.randint(0, len(grille) - 1)
            co2 = random.randint(0, len(grille[0]) - 1)
        grille[co1][co2] = 1

def testMine(grille, i, j):
    if grille[i][j] == 1:
        return True
    else:
        return False

def nbrCasesVoisines(grille, i, j):
    if (i == 0 or i == len(grille) - 1) and (j == 0 or j == len(grille[0]) - 1):
        return 3
    elif i == 0 or i == len(grille) - 1 or j == 0 or j == len(grille[0]) - 1:
        return 5
    else :
        return 8

def casesVoisines(grille, i, j):
    res = []
    nbr = nbrCasesVoisines(grille, i, j)
    if nbr == 3:
        if j == 0 and i == 0:
            res.append(grille[0][1])
            res.append(grille[1][0])
            res.append(grille[1][1])
        elif j == len(grille[0]) - 1 and i == 0:
            res.append(grille[0][len(grille[0]) - 2])
            res.append(grille[1][len(grille[0]) - 1])
            res.append(grille[1][len(grille[0]) - 2])
        elif j == 0 and i == len(grille):
            res.append(grille[len(grille) - 1][1])
            res.append(grille[len(grille) - 2][0])
            res.append(grille[len(grille) - 2][1])
        elif j == len(grille[0]) - 1 and i == len(grille) - 1:
            res.append(grille[len(grille) - 1][len(grille[0]) - 2])
            res.append(grille[len(grille) - 2][len(grille[0]) - 1])
            res.append(grille[len(grille) - 2][len(grille[0]) - 2])
    elif nbr == 5:
        if i == 0:
            res.append(grille[0][j + 1])
            res.append(grille[0][j - 1])
            res.append(grille[1][j])
            res.append(grille[1][j + 1])
            res.append(grille[1][j - 1])
        elif i == len(grille) - 1:
            res.append(grille[len(grille) - 1][j + 1])
            res.append(grille[len(grille) - 1][j - 1])
            res.append(grille[len(grille) - 2][j])
            res.append(grille[len(grille) - 2][j + 1])
            res.append(grille[len(grille) - 2][j - 1])
        elif j == 0:
            res.append(grille[i + 1][0])
            res.append(grille[i - 1][0])
            res.append(grille[i][1])
            res.append(grille[i + 1][1])
            res.append(grille[i - 1][1])
        elif j == len(grille[0]) - 1:
            res.append(grille[i + 1][len(grille[0]) - 1])
            res.append(grille[i - 1][len(grille[0]) - 1])
            res.append(grille[i][len(grille[0]) - 2])
            res.append(grille[i + 1][len(grille[0]) - 2])
            res.append(grille[i - 1][len(grille[0]) - 2])
    elif nbr == 8:
        res.append(grille[i][j + 1])
        res.append(grille[i][j - 1])
        res.append(grille[i - 1][j])
        res.append(grille[i - 1][j + 1])
        res.append(grille[i - 1][j - 1])
        res.append(grille[i + 1][j])
        res.append(grille[i + 1][j + 1])
        res.append(grille[i + 1][j - 1])
    return res
def compteMinesVoisines(grille, i, j):
    li = casesVoisines(grille, i, j)
    res = 0
    for elem in li:
        if elem == 1:
            res += 1
    return res

def afficheSolution(grillePos):
    for i in range(len(grillePos)):
        for elem in grillePos[i]:
            if elem == 0:
                print("-", end="")
            elif elem == 1:
                print("*", end="")
        print("")

def afficheJeu(grille, cases):
    n = 0
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if cases[n] == False:
                print("?", end="")
            elif grille[i][j] == 0:
                print(compteMinesVoisines(grille, i, j), end="")
            elif grille[i][j] == 1:
                print("*", end="")
            n += 1
        print("")

def getNbMines(grille):
    res = int(input("nbr de mines:   "))
    while res < 0 or res > (len(grille) * len(grille[0])):
        print("nombre de mines incorrect")
        res = int(input("nbr de mines:   "))
    return res

def getCoord(grille_dev, grille_sol):
    print("a toi de jouer")
    i = int(input("ligne:   "))
    while i < 0 or i > len(grille_sol) - 1:
        i = int(input("incorrect, recommence:   "))
    j = int(input("colonne:   "))
    while j < 0 or i > len(grille_sol[0]) - 1:
        j = int(input("incorrect, recommence:   "))
    while grille_sol[i][j] == "?":
        i = int(input("ligne:   "))
        while i < 0 or i > len(grille_sol) - 1:
            i = int(input("incorrect, recommence:   "))
        j = int(input("colonne:   "))
        while j < 0 or i > len(grille_sol[0]) - 1:
            j = int(input("incorrect, recommence:   "))
    grille_bool[i * len(grille_sol) + j] = True
    return i, j


print("début du jeu")
a = int(input("nbr de lignes:   "))
b = int(input("nbr de colonnes:   "))

grille_sol = creerGrille(a, b)
mines = getNbMines(grille_sol)
placerMines(grille_sol, mines)
grille_bool = (a*b) * [False]
playing = True
count = 0
while playing and count < (a*b) - mines:
    afficheJeu(grille_sol, grille_bool)
    x, y = getCoord(grille_bool, grille_sol)
    oui = testMine(grille_sol, x, y)
    if oui :
        playing = False
        print("perdu")
        afficheJeu(grille_sol, grille_bool)
        print("la solution était")
        afficheSolution(grille_sol)
    else :
        count += 1

if playing :
    print("tu as gagné")
    