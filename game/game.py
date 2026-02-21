import pygame
from .player import Player
from .ghost import Ghost
from .game_board import MAZE
from .sounds import SoundManager

class PacManGame:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Pac-Man - Simple Version")
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 15
        
        # Calculate cell size based on maze
        self.cell_size = width // len(MAZE[0])
        
        # RESET THE MAZE
        self.maze = [row[:] for row in MAZE]
        
        # Initialize sound manager
        self.sound_manager = SoundManager()
        
        # Initialize sprites
        self.player = Player(1, 1, self.cell_size)
        self.ghosts = [
            Ghost(5, 5, self.cell_size, (255, 0, 0)),      # Red ghost
            Ghost(6, 5, self.cell_size, (255, 184, 255)),  # Pink ghost
        ]
        
        self.score = 0
        self.pellets = self.count_pellets()
        self.game_over = False
        self.won = False
    
    def count_pellets(self):
        count = 0
        for row in self.maze:
            for cell in row:
                if cell == 0:
                    count += 1
        return count
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.set_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.player.set_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.player.set_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.player.set_direction((1, 0))
                elif event.key == pygame.K_r:  # Press R to restart
                    self.restart_game()
    
    def update(self):
        # Only update player and ghosts if game is still active
        if not self.game_over and not self.won:
            self.player.update(self.maze)
            for ghost in self.ghosts:
                ghost.update(self.maze, self.player)
            
            # Check pellet collection
            if self.maze[self.player.y][self.player.x] == 0:
                self.maze[self.player.y][self.player.x] = 2
                self.score += 10
                self.pellets -= 1
                self.sound_manager.play('chomp')  # PLAY CHOMP SOUND
                
                # Check if won
                if self.pellets == 0:
                    self.won = True
                    self.sound_manager.play('win')  # PLAY WIN SOUND
            
            # Check collision with ghosts (Game Over)
            for ghost in self.ghosts:
                if self.player.x == ghost.x and self.player.y == ghost.y:
                    self.game_over = True
                    self.sound_manager.play('game_over')  # PLAY GAME OVER SOUND
    
    def draw(self):
        self.screen.fill((0, 0, 0))  # Black background
        
        # Draw maze
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, 
                                 self.cell_size, self.cell_size)
                
                if cell == 1:  # Wall - blue rectangle
                    pygame.draw.rect(self.screen, (33, 33, 222), rect)
                    pygame.draw.rect(self.screen, (50, 50, 255), rect, 2)
                
                elif cell == 0:  # Pellet - small white dot
                    center_x = x * self.cell_size + self.cell_size // 2
                    center_y = y * self.cell_size + self.cell_size // 2
                    pygame.draw.circle(self.screen, (255, 200, 150), 
                                     (center_x, center_y), 3)
        
        # Draw player (yellow rectangle)
        self.screen.blit(self.player.image, self.player.rect)
        
        # Draw ghosts (colored circles)
        for ghost in self.ghosts:
            self.screen.blit(ghost.image, ghost.rect)
        
        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        
        # Draw pellets remaining
        pellets_text = font.render(f"Pellets: {self.pellets}", True, (255, 255, 255))
        self.screen.blit(pellets_text, (10, 50))
        
        # Draw game over or win message
        if self.game_over:
            game_over_font = pygame.font.Font(None, 72)
            game_over_text = game_over_font.render("GAME OVER!", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(game_over_text, text_rect)
            
            restart_font = pygame.font.Font(None, 36)
            restart_text = restart_font.render("Press R to Restart", True, (255, 255, 255))
            restart_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 80))
            self.screen.blit(restart_text, restart_rect)
        
        elif self.won:
            win_font = pygame.font.Font(None, 72)
            win_text = win_font.render("YOU WON!", True, (0, 255, 0))
            text_rect = win_text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(win_text, text_rect)
            
            restart_font = pygame.font.Font(None, 36)
            restart_text = restart_font.render("Press R to Restart", True, (255, 255, 255))
            restart_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 80))
            self.screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
    
    def restart_game(self):
        """Restart the game without recreating the window"""
        # Reset maze
        self.maze = [row[:] for row in MAZE]
        
        # Reset player and ghosts
        self.player = Player(1, 1, self.cell_size)
        self.ghosts = [
            Ghost(5, 5, self.cell_size, (255, 0, 0)),      # Red ghost
            Ghost(6, 5, self.cell_size, (255, 184, 255)),  # Pink ghost
        ]
        
        # Reset game state
        self.score = 0
        self.pellets = self.count_pellets()
        self.game_over = False
        self.won = False
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        
        pygame.quit()
