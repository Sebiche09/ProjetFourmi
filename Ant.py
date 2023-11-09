import pygame
import random

counter_food = 0
counter_larva = 0
counter_ant = 0
compteur = 0
larva_dict = dict()
food_dict = dict()
classes = ['Worker', 'Soldier', 'Explorer', 'Male', 'ChildcareWorker', 'Farmer', 'Slaver']
ant_dict = dict()

class Ant:
    def __init__(self, x, y):
        # Propriétés communes à toutes les fourmis
        self.position = (x, y)
        self.state = "idle"  # État initial
        self.move_interval = 500  # Interval de spawn en secondes (ajustez selon vos besoins)
        self.move_timer = self.move_interval
        # Autres propriétés communes
    def update(self):
        """
        POST: - Permet après X secondes, lancer la fonction spawn_larva()
        """
        self.move_timer -= 1


class Queen():
    def __init__(self, nest):
        self.nest = nest
        self.role = "queen"
        self.image = pygame.transform.scale(pygame.image.load("queen.png"), (30, 60)) # Image de la reine
        self.rect = self.image.get_rect()
        self.position = (nest.x + nest.width // 2, nest.y + nest.height // 2) #position de la reine (fixe)
        self.rect.center = self.position
# ----------------------------------------- Attribut spawn larve ------------------------------------------
        self.spawn_interval = 500  # Interval de spawn en secondes (ajustez selon vos besoins)
        self.spawn_timer = self.spawn_interval
# --------------------------------------------------------------------------------------------------------------
    def update(self):
        """
        POST: - Permet après X secondes, lancer la fonction spawn_larva()
        """
        self.spawn_timer -=1
        if self.spawn_timer <= 0:
            self.spawn_larva()
            self.spawn_timer = self.spawn_interval
    def draw(self, window):
        # Dessinez l'image de la reine sur la fenêtre Pygame
        window.blit(self.image, self.rect)
    def spawn_larva(self):
        global counter_larva
        while True:
            # Générer de nouvelles coordonnées pour la larve
            new_x = random.randint(((self.nest.width + 300) // 2) - 60, ((self.nest.width + 300) // 2) + 60)
            new_y = random.randint(((self.nest.height + 300) // 2) - 60, ((self.nest.height + 300) // 2) + 60)

            # Vérifier s'il y a une collision avec une larve existante
            collides = False
            new_larva_rect = pygame.Rect(new_x, new_y, 7, 7)
            for larva_key, (existing_larva, _, x, y) in larva_dict.items():
                existing_larva_rect = pygame.Rect(x, y, 7, 7)
                if existing_larva_rect.colliderect(new_larva_rect):
                    collides = True
                    break
            # Si aucune collision n'a été trouvée, ajouter la nouvelle larve au dictionnaire
            if not collides:
                larva = Larva(self.nest)
                larva.rect.topleft = (new_x, new_y)
                larva_key = f'larve{counter_larva}'
                larva_dict[larva_key] = (larva, 1000, new_x, new_y)
                counter_larva += 1
                break

class Larva():
    def __init__(self, nest):
        self.position = (nest.x + random.randint(325,375), nest.y + random.randint(275,300))
        self.role = "larva"
        self.image = pygame.transform.scale(pygame.image.load("larva.png"), (7, 7))
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.nest = nest

    def draw(self, window):
        window.blit(self.image, self.rect)

    def update(self):
        larvae_to_remove = []  # Liste pour stocker les clés des larves à supprimer
        for larva_key, (larva, value, x,y) in list(larva_dict.items()):
            if value == 0:
                larvae_to_remove.append(larva_key)  # Ajouter la clé à la liste des larves à supprimer
            else:
                value -= 1
                larva_dict[larva_key] = (larva, value,x,y)
        return larvae_to_remove
    def spawn_ant(self):
        global compteur
        global counter_ant
        if compteur == 0:
            selected_class_name = 'ChildcareWorker'
        else :
            selected_class_name = random.choice(classes)
        selected_class = eval(selected_class_name)
        image = pygame.image.load(f"{selected_class_name.lower()}.png")
        ant_width, ant_height =20, 40

        # Générer de nouvelles coordonnées pour la fourmi
        new_x = (larva_dict['larve'+str(compteur)][2])-10
        new_y = larva_dict['larve'+str(compteur)][3]-20
        compteur +=1
        ant = selected_class(self.nest, image, ant_width, ant_height)
        ant.rect.topleft = (new_x, new_y)
        ant_key = f'ant{counter_ant}'
        ant_dict[ant_key] = (ant, 10000,new_x,new_y)
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
