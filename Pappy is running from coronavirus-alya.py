import pygame
from pygame.locals import *
import time

surfaceW = 1000
surfaceH = 700
blue = (56,111,72)
white = (255,255,255)
pugW = 142
pugH = 167
horloge = pygame.time.Clock()

surface = pygame.display.set_mode((surfaceW,surfaceH))
pygame.display.set_caption("Pappy is running from Coronavirus")

pug_img = pygame.image.load('carlin.png')


pygame.init()

#Fonction pour les commandes de rejouer ou quitter le jeu :
def rejoue_ou_quitte():
    for event in pygame.event.get ([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
#quand la personne relache la touche le jeu recommence,
#on met le relachement de la touche pour une sécurité supplémentaire
#pour que le jeu ne redemarre pas directement apres 
        elif event.type == pygame.KEYUP:
            continue
        return event.key
    return None 

#Fonction qui décrit le rectangle dans lequel va se trouver le texte 
def creaTexteObj (texte, Police):

#Police.render permet de créer la police 
    texteSurface = Police.render(texte, True, white)
    
    return texteSurface, texteSurface.get_rect()

def message (texte) :

#pygame.font.Font permet de telecharger la police pour le gros texte (GOtexte) et le petit texte (petitTexte) 
    GOTexte = pygame.font.Font ('Dimbo Regular.ttf', 150)
    petitTexte = pygame.font.Font ('Dimbo Regular.ttf', 50)
    
    GOTexteSurf, GOTexteRect = creaTexteObj(texte, GOTexte)
    print (GOTexteRect) 
#Position du rectangle qui contient le gros texte
    GOTexteRect.center = surfaceW/2, (surfaceH/2)-50
#ici, on affiche la surface du texte definti precedemment, et le rectangle du texte bien positionné 
    surface.blit(GOTexteSurf, GOTexteRect)
    
    petitTexteSurf, petitTexteRect = creaTexteObj("Si tu veux rejouer, appuies sur cette touche !", petitTexte)
    print (petitTexteRect)  
    petitTexteRect.center = (surfaceW/2, surfaceH/2+70)
    print (petitTexteRect.center)
    surface.blit(petitTexteSurf, petitTexteRect)
    
    pygame.display.update()
    
#On ajoute un temps de latence pour que le joueur ai le temps de choisir s'il veut rejouer ou pas
    time.sleep(2)

#tant que la fonction ne renvoie rien, on veut que l'horloge indique 0,
#c'est à dire que le nombre d'image par seconde soit égal à 0,
#donc que l'image n'est pas renouvelé. L'horlogetick bloque le jeux 
    while rejoue_ou_quitte () == None :
        horloge.tick()
    principale()
    
def gameover () :
    message("I got you!")

def pug (x, y, image) :
    surface.blit(image, (x,y))

def principale() :
    
    x = 100
    y = 200
    y_mouvement = 0 

    game_over = False
        
        
    while not game_over :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
    #déplacement du pug
            if event.type == pygame.KEYDOWN : 
                if event.key == pygame.K_UP :
                    y_mouvement = -2
            if event.type == pygame.KEYUP :
                y_mouvement = 2
            
        y += y_mouvement
                        
#definission de l'arriere plan et de la position du chien        
        surface.fill(blue)
        pug (x, y, pug_img)
    
        pygame.display.update()
#creation des bords de l'écran que le chien ne peut pas depasser       
        if y > surfaceH - 40 or y < - 10 :
            gameover()
            
principale()

pygame.quit()
quit() 
 
    
    