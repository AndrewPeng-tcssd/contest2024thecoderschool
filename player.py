import pygame


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.hit_box = pygame.Rect(self.x, self.y, 20, 20)
        self.sprite = None
        self.speed = 5
        self.g = 10
        self.inAir = [False, False, False]

    def draw(self, window):
        self.move()
        if self.hit_box.y > 700:
            self.y = 700
            self.hit_box = pygame.Rect(self.x, self.y, 20, 20)
            pygame.draw.rect(window, (255, 0, 0), self.hit_box)
        else:
            pygame.draw.rect(window, (255, 0, 0), self.hit_box)

    def gravity(self):
        if self.y < 700:
            self.y += self.g
            self.g += 1
        else:
            self.g = 10
            self.y = 700

    def jump(self):
        self.y -= self.g
        self.g -= 1
        if self.g < -10:
            self.inAir[0] = False
    def move(self):
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_UP] and not self.inAir[len(self.inAir) - 1]:
            if not self.inAir[0]:
                self.inAir[0] = True
            elif not self.inAir[1]:
                self.inAir[1] = True
            else:
                self.inAir[2] = True
        if user_input[pygame.K_LEFT]:
            self.x -= self.speed
        if user_input[pygame.K_RIGHT]:
            self.x += self.speed
        if not self.inAir[0] or not self.inAir[1]:
            self.gravity()
        else:
            self.jump()
        self.hit_box = pygame.Rect(self.x, self.y, 20, 20)
