import pygame
import numpy as np
import math

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.load_sounds()
    
    def load_sounds(self):
        """Load sounds - using generated beeps if files don't exist"""
        self.create_sound_effects()
    
    def create_sound_effects(self):
        """Generate simple beep sounds without needing external files"""
        # Chomp sound (for eating pellets)
        self.sounds['chomp'] = self.generate_beep(400, 100)
        
        # Power-up sound
        self.sounds['powerup'] = self.generate_beep(600, 200)
        
        # Ghost caught sound
        self.sounds['ghost_caught'] = self.generate_beep(200, 150)
        
        # Game over sound
        self.sounds['game_over'] = self.generate_beep(100, 300)
        
        # Win sound (ascending tones)
        self.sounds['win'] = self.generate_win_sound()
    
    def generate_beep(self, frequency, duration_ms):
        """Generate a simple beep sound"""
        sample_rate = 22050
        duration_samples = int(sample_rate * duration_ms / 1000)
        
        # Generate sine wave using numpy
        t = np.linspace(0, duration_ms / 1000, duration_samples, False)
        wave = np.sin(2 * math.pi * frequency * t) * 0.3
        
        # Convert to 16-bit audio
        wave_int16 = np.int16(wave * 32767)
        
        # Create stereo (duplicate for both channels)
        stereo = np.zeros((duration_samples, 2), dtype=np.int16)
        stereo[:, 0] = wave_int16
        stereo[:, 1] = wave_int16
        
        # Create pygame sound
        sound = pygame.mixer.Sound(buffer=stereo.tobytes())
        sound.set_volume(0.3)
        return sound
    
    def generate_win_sound(self):
        """Generate ascending tone for winning"""
        sample_rate = 22050
        duration_ms = 500
        duration_samples = int(sample_rate * duration_ms / 1000)
        
        # Generate frequency sweep from 400 to 800 Hz
        t = np.linspace(0, duration_ms / 1000, duration_samples, False)
        frequency_sweep = 400 + (400 * t / (duration_ms / 1000))
        
        # Generate wave with sweeping frequency
        wave = np.sin(2 * math.pi * frequency_sweep * t) * 0.3
        
        # Convert to 16-bit audio
        wave_int16 = np.int16(wave * 32767)
        
        # Create stereo
        stereo = np.zeros((duration_samples, 2), dtype=np.int16)
        stereo[:, 0] = wave_int16
        stereo[:, 1] = wave_int16
        
        # Create pygame sound
        sound = pygame.mixer.Sound(buffer=stereo.tobytes())
        sound.set_volume(0.3)
        return sound
    
    def play(self, sound_name):
        """Play a sound by name"""
        if sound_name in self.sounds:
            try:
                self.sounds[sound_name].play()
            except Exception as e:
                print(f"Error playing sound {sound_name}: {e}")
