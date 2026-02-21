import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, cell_size):
        super().__init__()
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.animation_frame = 0
        
        self.image = pygame.Surface((cell_size, cell_size), pygame.SRCALPHA)
        self.draw_pacman()
        self.rect = self.image.get_rect(topleft=(x * cell_size, y * cell_size))
    
    def draw_pacman(self):
        """Draw cute Pac-Man with animated mouth"""
        self.image.fill((0, 0, 0, 0))  # Transparent background
        
        # Mouth animation
        mouth_open = abs((self.animation_frame % 20) - 10) / 10  # 0 to 1 to 0
        mouth_angle = int(mouth_open * 60)  # Opens from 0 to 60 degrees
        
        # Draw yellow circle body
        center = self.cell_size // 2
        radius = self.cell_size // 2 - 2
        pygame.draw.circle(self.image, (255, 255, 0), (center, center), radius)
        
        # Draw mouth (black wedge)
        mouth_points = [
            (center, center),
            (center + int(radius * 0.8), center - int(radius * 0.3)),
            (center + int(radius * 0.8), center + int(radius * 0.3))
        ]
        pygame.draw.polygon(self.image, (0, 0, 0), mouth_points)
        
        # Draw cute eye
        pygame.draw.circle(self.image, (0, 0, 0), (center + 2, center - 3), 2)
    
    def update(self, maze):
        self.animation_frame += 1
        self.draw_pacman()
        
        # Try to move in next direction
        next_x = self.x + self.next_direction[0]
        next_y = self.y + self.next_direction[1]
        
        if self.is_valid_move(next_x, next_y, maze):
            self.direction = self.next_direction
            self.x = next_x
            self.y = next_y
        
        self.rect.topleft = (self.x * self.cell_size, self.y * self.cell_size)
    
    def is_valid_move(self, x, y, maze):
        if 0 <= x < len(maze[0]) and 0 <= y < len(maze):
            return maze[y][x] != 1
        return False
    
    def set_direction(self, direction):
        self.next_direction = direction
