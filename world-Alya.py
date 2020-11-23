import random
import pygame
from constants import *



def create_world():

#Dessiner des carrés qui représente les objets à récuprer
    BLACK = (0,0,0)
    BLUE = (0,0,255)
    GREEN = (0, 255, 0)

    rect1 = pygame.draw.rect (background,BLACK, (20,20,90,30))
    rect2 = pygame.draw.rect (background,GREEN, (20,20,70,10))
    rect3 = pygame.draw.rect (background,BLUE, (20,20,100,120))
    
#Inserer les carrés dans la liste des  objets disponible 
    available_items = [rect1 , rect2 , rect3 , "poireaux", "orange", "bonbon", "carotte", "croissant"]
    contenu = []
    world = []

#Inserer la liste des objet disponible dans la liste des cases (ne marche pas)
    for y in range (WORLD_HEIGHT):
        for x in range (WORLD_WIDTH):
            contenu.insert (x, random.choices(available_items, k=2))
            world.append(contenu[2])
        print()

#Fonction pour transferer les objets du monde vers l'inventaire du joueur
       def transfer_item (available_items, inventaire, world):
       
       inventaire = []
       
           if available_items in world:
           
               world. remove (available_items)
               inventaire.append (available_items)
           
            return world, inventaire
        
#Fonction pour les commandes de PRENDRE ou POSER un objet    
        def prendre_poser (available_items) :
#Si la liste des objets dans le monde n'est pas vide alors...
    #À ajouter : la condition du joueur d'être sur la même case que l'objet (mais ne sais pas comment faire)
            while len(world) > 0  : 
#Les commandes suivantes s'activent          
                if event.key == pygame.K_p :
                    world, inventaire = transfer_item(world, inventaire)
                if event.key == pygame.K_l :
                    inventaire, world = transfer_item (inventaire,world)
                
                    
                    
                
    
    # TODO Il faut remplir notre terrain ici, en fonction de la taille choisie préalablement.

    return print(world)

case = get_index(4,2)
print(world[case])

def get_index(x, y):
    return y * WORLD_HEIGHT + x


# def transfer_item(source, cible, item):
#     if item in source:
#         source.remove(item)
#         cible.append(item)
#     return source, target
# 