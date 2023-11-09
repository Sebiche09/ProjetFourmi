import pygame
import pygame_widgets
import random
import sys
import time
from colony_simulation import Nest, ColonySimulation
from Ant import Queen, larva_dict,classes,Worker,Soldier,Explorer,Male,ChildcareWorker,Farmer,Slaver,ant_dict, Ant
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button

# Initialisation de Pygame
pygame.init()
# ----------------------------------------- Paramètres de la fenêtre ------------------------------------------
screen_info = pygame.display.Info()
WINDOW_WIDTH, WINDOW_HEIGHT = screen_info.current_w, screen_info.current_h
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
background_color = (255, 255, 255)  # Blanc
pygame.display.set_caption("Simulation de colonie de fourmis")
# --------------------------------------------- Paramètres du jeu ---------------------------------------------
# Couleur du bouton "Arrêter"
button_color = (0, 128, 0)  # Vert
button_rect = pygame.Rect((WINDOW_WIDTH // 2) - 50, WINDOW_HEIGHT - 50, 100, 50)
# Définition de la police
font = pygame.font.SysFont(None, 50)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
def main_menu():
    window.fill((119,136,153))
    pygame.draw.rect(window, (25,25,112), pygame.Rect((WINDOW_WIDTH//2)-275, 350, (WINDOW_HEIGHT//2)-75, 775),border_radius=20)
    draw_text('Menu Principal', font, (255, 255, 255), window, (WINDOW_WIDTH // 2) - 150, WINDOW_HEIGHT // 2 - 200)
    draw_text('Larves', pygame.font.SysFont(None, 30), (255, 255, 255), window, (WINDOW_WIDTH // 2)-270, WINDOW_HEIGHT // 2 - 125)
    draw_text('Nourritures', pygame.font.SysFont(None, 30), (255, 255, 255), window, (WINDOW_WIDTH // 2) - 270,WINDOW_HEIGHT // 2 - 75)
    draw_text('Fourmis', pygame.font.SysFont(None, 30), (255, 255, 255), window, (WINDOW_WIDTH // 2) - 270,WINDOW_HEIGHT // 2 - 25)

    # Création des boutons
    slider_larva = Slider(window, (WINDOW_WIDTH // 2) - 145, WINDOW_HEIGHT // 2 -125, 275, 20, min=1, max=20, step=1)
    slider_food = Slider(window, (WINDOW_WIDTH // 2) - 145, WINDOW_HEIGHT // 2 - 75, 275, 20, min=1, max=20, step=1)
    slider_ant = Slider(window, (WINDOW_WIDTH // 2) - 145, WINDOW_HEIGHT // 2 - 25, 275, 20, min=1, max=20, step=1)
    output_larva = TextBox(window, (WINDOW_WIDTH // 2) + 145, 435, 70, 50, fontSize=30, borderColour=(0, 0, 0), radius=10, textColour=(0, 0, 0))
    output_food = TextBox(window, (WINDOW_WIDTH // 2) + 145, WINDOW_HEIGHT // 2 - 90, 70, 50, fontSize=30, borderColour=(0, 0, 0), radius=10, textColour=(0, 0, 0))
    output_ant = TextBox(window, (WINDOW_WIDTH // 2) + 145, WINDOW_HEIGHT // 2 - 40, 70, 50, fontSize=30,borderColour=(0, 0, 0), radius=10, textColour=(0, 0, 0))
    output_larva.disable()
    output_food.disable()
    output_ant.disable()
    Button(window, (WINDOW_WIDTH // 2) - 130, WINDOW_HEIGHT-100, 200, 50, text='Simulation', fontSize=30, margin=20,inactiveColour=(119,136,153), pressedColour=(0, 255, 0), radius=20,
           onClick=lambda: Simulation(slider_larva.getValue(),slider_food.getValue(),slider_ant.getValue()))
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        output_larva.setText(slider_larva.getValue())
        output_food.setText(slider_food.getValue())
        output_ant.setText(slider_ant.getValue())
        pygame_widgets.update(events)
        pygame.display.update()

def Simulation(larva_value,food_value,ant_value):
    start_time = time.time()
    #--------------------------------------------------------------------------------------------------------------
    # Instanciez la classe Nest pour créer le nid
    nest = Nest(150, 50, WINDOW_WIDTH - 300, WINDOW_HEIGHT - 100)  # Exemple de position et de dimensions
    # Instanciez la classe ColonySimulation pour gérer la simulation
    simulation = ColonySimulation(nest, WINDOW_WIDTH - 300, WINDOW_HEIGHT - 100)


    queen = Queen(nest,larva_value,ant_value)
    # ----------------------------------------- Boucle principale de jeu ------------------------------------------
    running = True
    while running:
        # Gérez les événements Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    running = False
        # Effacez l'écran avec la couleur d'arrière-plan
        window.fill(background_color)
        # Dessinez le carré représentant la colonie (Nest)
        pygame.draw.rect(window, (0, 0, 0), (nest.x, nest.y, nest.width, nest.height), 4)  # Bordure noire
        # Appelez la méthode update de la simulation pour mettre à jour la simulation
        simulation.update()
        # Appelez la méthode draw de la simulation pour dessiner les éléments de la simulation
        simulation.draw(window)
        queen.draw(window)
        queen.update()
        larvae_to_remove = []
        for larva_key, (larva, value,x,y) in larva_dict.items():
            larvae_to_remove = larva.update()
            larva.draw(window)
        for larva_key in larvae_to_remove:
            larva.spawn_ant()
            del larva_dict[larva_key]

        for ant_key, (ant, value,new_x,new_y) in ant_dict.items() :
            print(ant.move_timer)
            x = new_x + random.randint(-10,10)
            y = new_y + random.randint(-10, 10)
            if x < nest.x+20 or x > nest.x+nest.width-20:
                x = new_x
            if y < nest.y+20 or y > nest.y+nest.height-20:
                y = new_y
            ant.rect.topleft = (x, y)
            ant_dict[ant_key] = (ant,value,x,y)
            ant.draw(window)

        #-------------------------------------------- Gestion du temps --------------------------------------------
        # Obtenez le temps écoulé en secondes
        current_time = time.time()  # Enregistrez le temps actuel
        elapsed_time = int(current_time - start_time)
        # Dessinez le temps en haut à droite
        font = pygame.font.Font(None, 36)
        timer_text = font.render(f"Temps : {elapsed_time} secondes", True, (0, 0, 0))
        larva_text = font.render(str(larva_dict), True, (0,0,0))
        text_rect = timer_text.get_rect()
        text_larva_rect = timer_text.get_rect()
        text_rect.topright = (WINDOW_WIDTH - 10, 10)
        text_larva_rect.topleft = (10, 10)
        window.blit(timer_text, text_rect)
        window.blit(larva_text,text_larva_rect)

        #--------------------------------------------------Boutons--------------------------------------------------
        pygame.draw.rect(window, button_color, button_rect)
        font = pygame.font.Font(None, 36)
        text = font.render("Arrêter", True, (255, 255, 255))
        text_rect = text.get_rect(center=button_rect.center)
        window.blit(text, text_rect)
        # ----------------------------------------------------------------------------------------------------------

        pygame.display.flip()
    #--------------------------------------------------------------------------------------------------------------



        # Quittez Pygame et terminez le programme
    pygame.quit()
    sys.exit()
main_menu()