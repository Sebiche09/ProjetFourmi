import pygame
import random
counter_larva = 0
counter_ant = 0
larva_dict = dict()
classes = ['Worker', 'Soldier', 'Explorer', 'Male', 'ChildcareWorker', 'Farmer', 'Slaver']
ant_dict = dict()
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

        self.spawn_interval = 500  # Interval de spawn en secondes (ajustez selon vos besoins)
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
        global counter_larva
        larva_image = pygame.image.load("larva.png")
        larva_width, larva_height = 5, 5

        while True:
            # Générer de nouvelles coordonnées pour la larve
            new_x = self.nest.x + random.randint(335, 365)
            new_y = self.nest.y + random.randint(280, 320)

            # Vérifier s'il y a une collision avec une larve existante
            collides = False
            for key, (existing_larva, value) in larva_dict.items():
                if existing_larva.rect.colliderect(new_x, new_y, larva_width, larva_height):
                    collides = True
                    break

            # Si aucune collision n'a été trouvée, ajouter la nouvelle larve au dictionnaire
            if not collides:
                larva = Larva(self.nest, larva_image, larva_width, larva_height)
                larva.rect.topleft = (new_x, new_y)
                larva_key = f'larve{counter_larva}'
                larva_dict[larva_key] = (larva, 1000)
                counter_larva += 1
                break


class Larva(Ant):
    def __init__(self, nest, larva_image, width, height):
        super().__init__(nest.x + random.randint(325,375), nest.y + random.randint(275,300))
        self.role = "larva"
        self.image = pygame.transform.scale(larva_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.nest = nest

    def draw(self, window):
        window.blit(self.image, self.rect)

    def update(self):
        larvae_to_remove = []  # Liste pour stocker les clés des larves à supprimer
        for larva_key, (larva, value) in list(larva_dict.items()):
            if value == 0:
                larvae_to_remove.append(larva_key)  # Ajouter la clé à la liste des larves à supprimer
            else:
                value -= 1
                larva_dict[larva_key] = (larva, value)
        return larvae_to_remove
    def spawn_ant(self):
        global counter_ant
        selected_class_name = random.choice(classes)
        selected_class = eval(selected_class_name)
        image = pygame.image.load(f"{selected_class_name.lower()}.png")
        ant_width, ant_height = 15, 30

        # Générer de nouvelles coordonnées pour la fourmi
        new_x = self.nest.x + random.randint(5, 695)
        new_y = self.nest.y + random.randint(5, 595)
        ant = selected_class(self.nest, image, ant_width, ant_height)
        ant.rect.topleft = (new_x, new_y)
        ant_key = f'ant{counter_ant}'
        ant_dict[ant_key] = (ant, 10000)
        counter_ant += 1

class Worker(Ant):
    def __init__(self, nest, worker_image, width, height):
        super().__init__(nest.x + random.randint(5,695), nest.y + random.randint(5,595))
        self.role = "worker"
        self.image = pygame.transform.scale(worker_image, (width, height))  # Image de la reine
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        # Propriétés spécifiques à une ouvrière (comportement de collecte, etc.)
    def draw(self, window):
        # Dessinez l'image de la reine sur la fenêtre Pygame
        window.blit(self.image, self.rect)

class Soldier(Ant):
    def __init__(self, nest, soldier_image, width, height):
        super().__init__(nest.x + random.randint(5,695), nest.y + random.randint(5,595))
        self.role = "soldier"
        self.image = pygame.transform.scale(soldier_image, (width, height))  # Image de la reine
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        # Propriétés spécifiques à une soldate (comportement de défense, etc.)
    def draw(self, window):
        # Dessinez l'image de la reine sur la fenêtre Pygame
        window.blit(self.image, self.rect)

class Explorer(Ant):
    def __init__(self, nest, explorer_image, width, height):
        super().__init__(nest.x + random.randint(5,695), nest.y + random.randint(5,595))
        self.role = "explorer"
        self.image = pygame.transform.scale(explorer_image, (width, height))  # Image de la reine
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        # Propriétés spécifiques à une exploratrice (comportement d'exploration, etc.)
    def draw(self, window):
        # Dessinez l'image de la reine sur la fenêtre Pygame
        window.blit(self.image, self.rect)

class Male(Ant):
    def __init__(self, nest, male_image, width, height):
        super().__init__(nest.x + random.randint(5,695), nest.y + random.randint(5,595))
        self.role = "male"
        self.image = pygame.transform.scale(male_image, (width, height))  # Image de la reine
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        # Propriétés spécifiques à un male (comportement de reproduction, etc.)
    def draw(self, window):
        # Dessinez l'image de la reine sur la fenêtre Pygame
        window.blit(self.image, self.rect)

class ChildcareWorker(Ant):
    def __init__(self, nest, childcare_worker_image, width, height):
        super().__init__(nest.x + random.randint(5,695), nest.y + random.randint(5,595))
        self.role = "childcare_worker"
        self.image = pygame.transform.scale(childcare_worker_image, (width, height))  # Image de la reine
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        # Propriétés spécifiques à une puéricultrice (comportement de gestion des larves, etc.)
    def draw(self, window):
        # Dessinez l'image de la reine sur la fenêtre Pygame
        window.blit(self.image, self.rect)

class Farmer(Ant):
    def __init__(self, nest, farmer_image, width, height):
        super().__init__(nest.x + random.randint(5,695), nest.y + random.randint(5,595))
        self.role = "farmer"
        self.image = pygame.transform.scale(farmer_image, (width, height))  # Image de la reine
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        # Propriétés spécifiques à une agricultrice (comportement de nourriture, etc.)
    def draw(self, window):
        # Dessinez l'image de la reine sur la fenêtre Pygame
        window.blit(self.image, self.rect)

class Slaver(Ant):
    def __init__(self, nest, slaver_image, width, height):
        super().__init__(nest.x + random.randint(5,695), nest.y + random.randint(5,595))
        self.role = "salver"
        self.image = pygame.transform.scale(slaver_image, (width, height))  # Image de la reine
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        # Propriétés spécifiques à une esclavagiste (comportement d'esclavagisme, etc.)
    def draw(self, window):
        # Dessinez l'image de la reine sur la fenêtre Pygame
        window.blit(self.image, self.rect)

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
