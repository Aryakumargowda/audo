import numpy as np
import pygame
sample_rate = 44100
duration = 2.0  # Maximum duration for sound decay in seconds
initial_volume = 1.0
class GetSound():

    def __init__(self):
        self.C3 = None
        self.D3 = None
        self.E3 = None
        self.F3 = None
        self.G3 = None
        self.A3 = None
        self.B3 = None
        self.c_hash = None
        self.load_tones()

    def load_tones(self):
        tone = self.generate_tone(261.63, duration)
        self.C3 = pygame.sndarray.make_sound((tone * 32767).astype(np.int16))

        tone = self.generate_tone(293.66, duration)
        self.D3 = pygame.sndarray.make_sound((tone * 32767).astype(np.int16))

        tone = self.generate_tone(329.63, duration)
        self.E3 = pygame.sndarray.make_sound((tone * 32767).astype(np.int16))

        tone = self.generate_tone(349.23, duration)
        self.F3 = pygame.sndarray.make_sound((tone * 32767).astype(np.int16))

        tone = self.generate_tone(392.00, duration)
        self.G3 = pygame.sndarray.make_sound((tone * 32767).astype(np.int16))

        tone = self.generate_tone(440.00, duration)
        self.A3 = pygame.sndarray.make_sound((tone * 32767).astype(np.int16))

        tone = self.generate_tone(493.88, duration)
        self.B3 = pygame.sndarray.make_sound((tone * 32767).astype(np.int16))

        tone = self.generate_tone(277.183, duration)
        self.c_hash = pygame.sndarray.make_sound((tone * 32767).astype(np.int16))

    def generate_tone(self, frequency, duration):
        """Generates a continuous tone as a stereo wave array."""
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        wave = np.sin(2 * np.pi * frequency * t)
        stereo_wave = np.stack((wave, wave), axis=-1)  # Stereo wave
        return stereo_wave
    
    def get_c3(self):
        return self.C3
    
    def get_D3(self):
        return self.D3
    
    def get_E3(self):
        return self.E3
    
    def get_F3(self):
        return self.F3
    
    def get_G3(self):
        return self.G3
    
    def get_A3(self):
        return self.A3
    
    def get_B3(self):
        return self.B3
    
    def get_c_hash(self):
        return self.c_hash
