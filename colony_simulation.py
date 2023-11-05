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
    def draw(self, window):
        # Dessinez l'image de la reine sur la fenêtre Pygame
        window.blit(self.image, self.rect)

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

class Larva(Ant):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.role = "larva"
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
