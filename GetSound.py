import numpy as np
from BaseFrequency import BaseFrequency
import pygame

sample_rate = 44100
duration = 4  # Maximum duration for sound decay in seconds
initial_volume = 1.0


class GetSound():

    def __init__(self, base):
        self.C = None
        self.D = None
        self.E = None
        self.F = None
        self.G = None
        self.A = None
        self.B = None
        self.load_tones(base)

    def load_tones(self, base):
        tone = self.generate_tone(base, duration)
        self.C = pygame.sndarray.make_sound((tone * 32767).astype(np.int16))

        tone = self.generate_tone(base*2, duration)
        self.D = pygame.sndarray.make_sound((tone * 32767).astype(np.int16))

        tone = self.generate_tone(base*3, duration)
        self.E = pygame.sndarray.make_sound((tone * 32767).astype(np.int16))

        tone = self.generate_tone(base*4, duration)
        self.F = pygame.sndarray.make_sound((tone * 32767).astype(np.int16))

        tone = self.generate_tone(base*5, duration)
        self.G = pygame.sndarray.make_sound((tone * 32767).astype(np.int16))

        tone = self.generate_tone(base*6, duration)
        self.A = pygame.sndarray.make_sound((tone * 32767).astype(np.int16))

        tone = self.generate_tone(base*7, duration)
        self.B = pygame.sndarray.make_sound((tone * 32767).astype(np.int16))

    def generate_tone(self, frequency, duration):
        """Generates a continuous tone as a stereo wave array."""
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        wave = np.sin(2 * np.pi * frequency * t)
        stereo_wave = np.stack((wave, wave), axis=-1)  # Stereo wave
        return stereo_wave
    
    def get_fh(self):
        return self.C
    
    def get_sh(self):
        return self.D
    
    def get_th(self):
        return self.E
    
    def get_fth(self):
        return self.F
    
    def get_fih(self):
        return self.G
    
    def get_sh(self):
        return self.A
    
    def get_seh(self):
        return self.B
