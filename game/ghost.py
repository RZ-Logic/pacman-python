import pygame
import random

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, cell_size, color):
        super().__init__()
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.color = color
        self.move_counter = 0
        self.animation_frame = 0
        
        self.image = pygame.Surface((cell_size, cell_size), pygame.SRCALPHA)
        self.draw_ghost()
        self.rect = self.image.get_rect(topleft=(x * cell_size, y * cell_size))
    
    def draw_ghost(self):
        """Draw cute ghost with eyes and wavy bottom"""
        self.image.fill((0, 0, 0, 0))  # Transparent background
        
        center = self.cell_size // 2
        radius = self.cell_size // 2 - 3
        
        # Draw ghost head (circle)
        pygame.draw.circle(self.image, self.color, (center, center - 2), radius)
        
        # Draw ghost body (rectangle below head)
        pygame.draw.rect(self.image, self.color, 
                        (center - radius, center - 2, radius * 2, radius + 3))
        
        # Draw wavy bottom (cute ghost skirt effect)
        wave_height = 3
        for i in range(4):
            x_pos = center - radius + i * (radius // 2)
            y_pos = self.cell_size - 3 + (2 if i % 2 == 0 else -2)
            pygame.draw.circle(self.image, self.color, (x_pos, y_pos), 3)
        
        # Draw cute eyes
        eye_y = center - 3
        eye_left_x = center - 4
        eye_right_x = center + 4
        
        # Left eye
        pygame.draw.circle(self.image, (255, 255, 255), (eye_left_x, eye_y), 3)
        pygame.draw.circle(self.image, (0, 0, 0), (eye_left_x, eye_y), 1)
        
        # Right eye
        pygame.draw.circle(self.image, (255, 255, 255), (eye_right_x, eye_y), 3)
        pygame.draw.circle(self.image, (0, 0, 0), (eye_right_x, eye_y), 1)
    
    def update(self, maze, player=None):
        self.move_counter += 1
        self.animation_frame += 1
        self.draw_ghost()  # Redraw ghost
        
        # Move ghost every 5 frames
        if self.move_counter % 5 == 0:
            possible_moves = self.get_possible_moves(maze)
            
            if possible_moves:
                # Chase player if available
                if player:
                    best_move = min(possible_moves, 
                                  key=lambda m: abs(m[0] - player.x) + abs(m[1] - player.y))
                else:
                    best_move = random.choice(possible_moves)
                
                self.x, self.y = best_move
        
        self.rect.topleft = (self.x * self.cell_size, self.y * self.cell_size)
    
    def get_possible_moves(self, maze):
        moves = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] != 1:
                moves.append((nx, ny))
        return moves
