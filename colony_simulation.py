import pygame
import random

larva_list = []
class Ant:
    def __init__(self, x, y):
        # Propriétés communes à toutes les fourmis
        self.position = (x, y)
        self.state = "idle"  # État initial
        # Autres propriétés communes

class Queen(Ant):
    def __init__(self, nest, queen_image, width, height):
        super().__init__(nest.x + nest.width // 2, nest.y + nest.height // 2)
        self.role = "queen"
        self.image = pygame.transform.scale(queen_image, (width, height))  # Image de la reine
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.spawn_interval = 50  # Interval de spawn en secondes (ajustez selon vos besoins)
        self.spawn_timer = self.spawn_interval
        self.nest = nest
    def update(self):
        self.spawn_timer -=1
        if self.spawn_timer <= 0:
            self.spawn_larva()
            self.spawn_timer = self.spawn_interval
    def draw(self, window):
        # Dessinez l'image de la reine sur la fenêtre Pygame
        window.blit(self.image, self.rect)

    def spawn_larva(self):
        larva_image = pygame.image.load("larva.png")
        larva_width, larva_height = 5, 5

        while True:
            # Générer de nouvelles coordonnées pour la larve
            new_x = self.nest.x + random.randint(325, 375)
            new_y = self.nest.y + random.randint(275, 300)

            # Vérifier s'il y a une collision avec une larve existante
            collides = False
            for larva in larva_list:
                if larva.rect.colliderect(new_x, new_y, larva_width, larva_height):
                    collides = True
                    break

            # Si aucune collision n'a été trouvée, ajouter la nouvelle larve
            if not collides:
                larva = Larva(self.nest, larva_image, larva_width, larva_height)
                larva.rect.topleft = (new_x, new_y)
                larva_list.append(larva)
                break

class Larva(Ant):
    def __init__(self, nest, larva_image, width, height):
        super().__init__(nest.x + random.randint(325,375), nest.y + random.randint(275,300))
        self.role = "larva"
        self.image = pygame.transform.scale(larva_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def draw(self, window):
        window.blit(self.image, self.rect)

    def update(self):
        pass

class Worker(Ant):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.role = "worker"
        # Propriétés spécifiques à une ouvrière (comportement de collecte, etc.)

class Soldier(Ant):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.role = "soldier"
        # Propriétés spécifiques à une soldate (comportement de défense, etc.)

class Explorer(Ant):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.role = "explorer"
        # Propriétés spécifiques à une exploratrice (comportement d'exploration, etc.)

class Nest:
    def __init__(self, x, y, width, height):
        # Position et dimensions du nid
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Autres attributs du nid, comme la quantité de nourriture, le nombre d'œufs, etc.

class Food:
    def __init__(self, x, y):
        # Position de la nourriture
        self.x = x
        self.y = y
        # Autres attributs de la nourriture, comme la quantité, le type, etc.

class ColonySimulation:
    def __init__(self, nest, width, height):
        # Initialisation de la simulation
        self.nest = nest
        self.width = width
        self.height = height
        # Créez d'autres éléments de la simulation, comme des fourmis, la reine, etc.

    def update(self):
        pass
        # Mettez à jour la simulation à chaque itération

    def draw(self, window):
        pass
        # Dessinez les éléments de la simulation sur la fenêtre Pygame

    # Ajoutez d'autres méthodes pour gérer le comportement de la simulation
