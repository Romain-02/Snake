import pygame
import random
import time
pygame.init()

class Game:
    def __init__(self, matrice, head):
        self.matrice = matrice
        self.head = head
        self.corps = [head]

screen = pygame.display.set_mode((846, 1000))
pygame.display.set_caption('Snake')
compt = 0

tête = pygame.image.load('tête.png')
tête2 = pygame.image.load('carré bleu.xcf')
tête2 = pygame.transform.scale(tête2, (846, 154))
corps = pygame.image.load('corps.png')
corps2 = pygame.image.load('Sans titre.png')
corps2 = pygame.transform.scale(corps2, (1000, 1000))
pomme = pygame.image.load('pomme.png')
pomme2 = pygame.transform.scale(pomme, (118, 118))
carre_vert1 = pygame.image.load('carré vert.png')
carre_vert1_2 = pygame.transform.scale(carre_vert1, (780, 780))
carre_vert2 = pygame.image.load('carré vert foncé.png')
trophee = pygame.image.load('trophée.png')
trophee = pygame.transform.scale(trophee, (95, 95))
block = pygame.image.load('bloc.png')
block = pygame.transform.scale(block, (105, 105))

police = pygame.font.SysFont("monospace", 25)
play1 = pygame.image.load('play.png')
play1 = pygame.transform.scale(play1, (300, 150))
play1_rect = play1.get_rect()
play1_rect.x = 80
play1_rect.y = 500
texte1 = police.render('Facil', 0, (0, 0, 0))
play2 = play1
play2_rect = play2.get_rect()
play2_rect.x = 480
play2_rect.y = 500
texte2 = police.render('Moyen', 0, (0, 0, 0))
play3 = play1
play3_rect = play3.get_rect()
play3_rect.x = 280
play3_rect.y = 708
texte3 = police.render('Difficil', 0, (0, 0, 0))
play4 = play1
play4_rect = play4.get_rect()
play4_rect.x = 80
play4_rect.y = 500
texte4 = police.render('Bloc', 0, (0, 0, 0))
play5 = play1
play5_rect = play5.get_rect()
play5_rect.x = 480
play5_rect.y = 500
texte5 = police.render('No Bloc', 0, (0, 0, 0))
play6 = play1
play6_rect = play6.get_rect()
play6_rect.x = 270
play6_rect.y = 450

background = pygame.image.load('écran départ.jfif')
background = pygame.transform.scale(background, (846, 1000))

#Flag
running = True
depart = True
facil = False
moyen = False
difficil = False
choix_bloc = False
bloc = False
game = False
fin = False
record = 0
texte6 = police.render(str(record), 0, (0, 0, 0))
texte6 = pygame.transform.scale(texte6, (85, 145))
score = 0
texte7 = police.render(str(score), 0, (0, 0, 0))
texte7 = pygame.transform.scale(texte7, (85, 145))
nb_block = 0
blocs = []
texte8 = police.render(str(nb_block), 0, (0, 0, 0))
texte8 = pygame.transform.scale(texte8, (85, 145))
texte9 = police.render('Relancer', 0, (0, 0, 0))
texte9 = pygame.transform.scale(texte9, (200, 66))

def terrain(carreau):
    num = carre_vert1
    tab = []
    for i in range(carreau):
        tab2 = []
        for j in range(carreau):
            tab2.append((num, (i * (780/carreau) + 33, j * (780/carreau) + 187)))
            if num != carre_vert1:
                num = carre_vert1
            else:
                num = carre_vert2
        tab.append(tab2)
    return tab

def contient_pomme(matrice):
    for x in range(len(matrice)):
        for y in range(len(matrice)):
            if matrice[x][y] == 2: #2 c'est la pomme
                return True
    return False

def mettre_pomme(matrice, longueur):
    x = 0
    y = 0
    while matrice[x][y] != 0:
        x = random.randint(1, longueur)
        y = random.randint(1, longueur)
    matrice[x][y] = 2
    return matrice

def pose_bloc(matrice, longueur):
    x = 0
    y = 0
    while matrice[x][y] != 0:
        x = random.randint(1, longueur)
        y = random.randint(1, longueur)
    matrice[x][y] = 3
    return matrice

def contient_bloc(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] == 3: #2 c'est un bloc
                return True
    return False

def est_le_corps(cord, corps):
    for elt in corps:
        if elt[0] == cord:
            return True
    return False

def creer_matrice(longueur):
    matrice = [[1] * (longueur+2)]
    for i in range(longueur):
        mat = [1]
        for j in range(longueur):
            mat.append(0)
        mat.append(1)
        matrice.append(mat)
    mat = [1] * (longueur+2)
    matrice.append(mat)
    return matrice

def affichage_matrice(matrice):
    for i in range(len(matrice)):
        print(matrice[i])
    print()

def pose_et_renvoie_snake(longueur):
    i = random.randint(1, longueur-1)
    j = random.randint(1, longueur-1)
    if i < longueur / 2:
        dir1 = 'd'
    else:
        dir1 = 'g'
    if j < longueur / 2:
        dir2 = 'b'
    else:
        dir2 = 'h'
    if random.randint(1, 2) == 1:
        return ((i, j), dir1)
    return ((i, j), dir2)

def deplacement(matrice, tete, corps, long, temps, compt, score, nb_block, bloc):
    time.sleep(temps/15)
    compt += 1
    bool = False
    for elt in corps:
        cord = elt[0]
        matrice[cord[0]][cord[1]] = 4
    matrice[corps[0][0][0]][corps[0][0][1]] = 5
    print(matrice)
    if compt % 15 == 0:
        i = tete[0][0]
        j = tete[0][1]
        print(i, j)
        if tete[1] == 'b':
            if matrice[i][j+1] == 0 or matrice[i][j+1] == 2:
                tete = ((i, j+1), tete[1])
                j += 1
            else:
                bool = True
        elif tete[1] == 'h':
            if matrice[i][j - 1] == 0 or matrice[i][j-1] == 2:
                tete = ((i, j - 1), tete[1])
                j -= 1
            else:
                bool = True
        elif tete[1] == 'g':
            if matrice[i-1][j] == 0 or matrice[i-1][j] == 2:
                tete = ((i-1, j), tete[1])
                i -= 1
            else:
                bool = True
        else:
            if matrice[i + 1][j] == 0 or matrice[i+1][j] == 2:
                tete = ((i + 1, j), tete[1])
                i += 1
            else:
                bool = True
        if not contient_pomme(matrice):
            matrice = mettre_pomme(matrice, longueur)
        elif matrice[i][j] == 2:
            score += 1
            matrice = mettre_pomme(matrice, longueur)
        #la tete a bougé ou c'est perdu
        if not bool:
            if matrice[tete[0][0]][tete[0][1]] == 2:
                corps = [tete] + corps
                if score % 2 == 0 and bloc:
                    pose_bloc(matrice, longueur)
            else:
                matrice[corps[-1][0][0]][corps[-1][0][1]] = 0
                corps = [tete] + corps[ : -1]
    return (matrice, tete, corps, bool, compt, score, nb_block)

while running:
    if depart:
        #afficher l'écran d'accueil
        screen.blit(background, (0, 0))
        screen.blit(play1, play1_rect)
        screen.blit(play2, play2_rect)
        screen.blit(play3, play3_rect)
        screen.blit(texte1, (186, 562))
        screen.blit(texte2, (585, 562))
        screen.blit(texte3, (368, 770))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if play1_rect.collidepoint(pygame.mouse.get_pos()):
                texte1 = police.render('Facil', 0, (255, 255, 255))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    depart = False
                    facil = True
                    choix_bloc = True
            elif play2_rect.collidepoint(pygame.mouse.get_pos()):
                texte2 = police.render('Moyen', 0, (255, 255, 255))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    depart = False
                    moyen = True
                    choix_bloc = True
            elif play3_rect.collidepoint(pygame.mouse.get_pos()):
                texte3 = police.render('Difficil', 0, (255, 255, 255))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    depart = False
                    difficil = True
                    choix_bloc = True
            else:
                texte1 = police.render('Facil', 0, (0, 0, 0))
                texte2 = police.render('Moyen', 0, (0, 0, 0))
                texte3 = police.render('Difficil', 0, (0, 0, 0))
        pygame.display.flip()
    if facil:
        longueur = 5
        temps = 1
    if moyen:
        longueur = 11
        temps = 0.5
    if difficil:
        longueur = 15
        temps = 0.25
    if choix_bloc:
        screen.blit(background, (0, 0))
        screen.blit(play4, play4_rect)
        screen.blit(play5, play5_rect)
        screen.blit(texte4, (190, 560))
        screen.blit(texte5, (572, 560))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if play4_rect.collidepoint(pygame.mouse.get_pos()):
                texte4 = police.render('Block', 0, (255, 255, 255))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    bloc = True
                    game = True
                    choix_bloc = False
                    game1 = Game(creer_matrice(longueur), pose_et_renvoie_snake(longueur))
                    mat = creer_matrice(longueur)
            elif play5_rect.collidepoint(pygame.mouse.get_pos()):
                texte5 = police.render('No Block', 0, (255, 255, 255))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game = True
                    bloc = False
                    choix_bloc = False
                    game1 = Game(creer_matrice(longueur), pose_et_renvoie_snake(longueur))
                    mat = creer_matrice(longueur)
            else:
                texte4 = police.render('Block', 0, (0, 0, 0))
                texte5 = police.render('No Block', 0, (0, 0, 0))
        pygame.display.flip()
    if game:
        texte6 = police.render(str(record), 0, (0, 0, 0))
        texte8 = police.render(str(nb_block), 0, (0, 0, 0))
        texte7 = police.render(str(score), 0, (0, 0, 0))
        texte6 = pygame.transform.scale(texte6, (85, 145))
        texte7 = pygame.transform.scale(texte7, (85, 145))
        texte8 = pygame.transform.scale(texte8, (85, 145))
        for elt in game1.corps:
            mat[elt[0][0]][elt[0][1]] = 4
        mat[game1.head[0][0]][game1.head[0][1]] = 5
        for b in blocs:
            matrice[b[0]][b[1]] = 3
        corps = pygame.transform.scale(corps, (786 / longueur, 786 / longueur))
        pomme = pygame.transform.scale(pomme, (786/ longueur, 786 / longueur ))
        tête = pygame.transform.scale(tête, (786 / longueur, 786 / longueur))
        carre_vert1 = pygame.transform.scale(carre_vert1, (786 / longueur, 786 / longueur))
        carre_vert2 = pygame.transform.scale(carre_vert2, (786 / longueur, 786 / longueur))
        block_jeu = pygame.transform.scale(corps2, (786 / longueur, 786 / longueur))
        #afficher le décor
        screen.blit(corps2, (0, 0))
        screen.blit(carre_vert1_2, (33, 187))
        screen.blit(tête2, (0, 0))
        screen.blit(trophee, (20, 30))
        screen.blit(texte6, (120, 16))
        screen.blit(pomme2, (250, 18))
        screen.blit(texte7, (366, 16))
        if bloc:
            screen.blit(block, (498, 30))
            screen.blit(texte8, (618, 16))
        carre = []
        tab = terrain(longueur)
        #charger les images pour le terrain
        #afficher terrain de jeu
        for i in range(1, len(tab)+1):
            for j in range(1, len(tab)+1):
                carre.append(tab[i-1][j-1][0])
                rect = carre[-1].get_rect()
                rect.x = tab[i-1][j-1][1][0]
                rect.y = tab[i-1][j-1][1][1]
                if mat[i][j] == 5:
                    screen.blit(tête, rect)
                elif mat[i][j] == 4:
                    screen.blit(corps, rect)
                elif mat[i][j] == 2:
                    screen.blit(carre[-1], rect)
                    screen.blit(pomme, rect)
                elif mat[i][j] == 3:
                    screen.blit(block_jeu, rect)
                else:
                    screen.blit(carre[-1], rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    game1.head = (game1.head[0], 'd')
                elif event.key == pygame.K_LEFT:
                    game1.head = (game1.head[0], 'g')
                elif event.key == pygame.K_UP:
                    game1.head = (game1.head[0], 'h')
                else:
                    game1.head = (game1.head[0], 'b')
        pygame.display.flip()
        res = deplacement(mat, game1.head, game1.corps, longueur, temps, compt, score, nb_block, bloc)
        mat = res[0]
        game1.head = res[1]
        game1.corps = res[2]
        fin = res[3]
        compt = res[4]
        score = res[5]
        nb_block = res[6]
        if fin:
            game = False

    # jeu
    if fin:
        screen.blit(play6, play6_rect)
        screen.blit(texte9, (320, 490))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if play6_rect.collidepoint(pygame.mouse.get_pos()):
                texte9 = police.render('Relancer', 0, (255, 255, 255))
                texte9 = pygame.transform.scale(texte9, (200, 66))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game1 = Game(creer_matrice(longueur), pose_et_renvoie_snake(longueur))
                    mat = creer_matrice(longueur)
                    fin = False
                    depart = True
                    compt = 0
                    if score > record:
                        record = score
                    score = 0
            else:
                texte9 = police.render('Relancer', 0, (0, 0, 0))
                texte9 = pygame.transform.scale(texte9, (200, 66))
        pygame.display.flip()






