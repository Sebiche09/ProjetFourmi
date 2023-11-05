import pygame
import random
import sys
from colony_simulation import Queen, Nest, Food, ColonySimulation, Larva, larva_list

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 600
# Créez une surface de fenêtre
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Définissez la couleur de l'arrière-plan
background_color = (255, 255, 255)  # Blanc
# Définissez le titre de la fenêtre
pygame.display.set_caption("Simulation de colonie de fourmis")
# Instanciez la classe Nest pour créer le nid
nest = Nest(150, 50, WINDOW_WIDTH - 300, WINDOW_HEIGHT - 100)  # Exemple de position et de dimensions
# Instanciez la classe ColonySimulation pour gérer la simulation
simulation = ColonySimulation(nest, WINDOW_WIDTH - 300, WINDOW_HEIGHT - 100)

queen_image = pygame.image.load("queen.png")
queen = Queen(nest, queen_image, 30, 60)  # Où "queen.png" est le chemin de l'image de la reine
# ----------------------------------------- Boucle principale de jeu ------------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Effacez l'écran avec la couleur d'arrière-plan
    window.fill(background_color)
    # Dessinez le carré représentant la colonie (Nest)
    pygame.draw.rect(window, (0, 0, 0), (nest.x, nest.y, nest.width, nest.height), 2)  # Bordure noire
    # Appelez la méthode update de la simulation pour mettre à jour la simulation
    simulation.update()
    # Appelez la méthode draw de la simulation pour dessiner les éléments de la simulation
    simulation.draw(window)
    queen.draw(window)
    #-------------------------------------------- Gestion du temps --------------------------------------------
    # Obtenez le temps écoulé en secondes
    elapsed_time = pygame.time.get_ticks() // 1000
    # Dessinez le temps en haut à droite
    font = pygame.font.Font(None, 36)
    timer_text = font.render(f"Temps : {elapsed_time} secondes", True, (0, 0, 0))
    text_rect = timer_text.get_rect()
    text_rect.topright = (WINDOW_WIDTH - 10, 10)
    window.blit(timer_text, text_rect)
    #----------------------------------------------------------------------------------------------------------

    pygame.display.flip()
#--------------------------------------------------------------------------------------------------------------

# Quittez Pygame et terminez le programme
pygame.quit()
sys.exit()
