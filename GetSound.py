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
        # tone = self.generate_tone(base, duration)
        self.C = self.generate_note_sound(base, 0, duration)

        # tone = self.generate_tone(base*2, duration)
        self.D = self.generate_note_sound(base, 2, duration)

        # tone = self.generate_tone(base*3, duration)
        self.E = self.generate_note_sound(base, 4, duration)

        # tone = self.generate_tone(base*4, duration)
        self.F = self.generate_note_sound(base, 5, duration)

        # tone = self.generate_tone(base*5, duration)
        self.G = self.generate_note_sound(base, 7, duration)

        # tone = self.generate_tone(base*6, duration)
        self.A = self.generate_note_sound(base, 9, duration)

        # tone = self.generate_tone(base*7, duration)
        self.B = self.generate_note_sound(base, 11, duration)

    def generate_tone(self, frequency, duration):
        """Generates a continuous tone as a stereo wave array."""
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        wave = .5*np.sin(2 * np.pi * frequency * t)
        stereo_wave = np.stack((wave, wave), axis=-1)  # Stereo wave
        return stereo_wave

    def generate_note_sound(self, base_freq, half_steps, duration):
        target_freq = base_freq * (2 ** (half_steps / 12))
        tone = self.generate_tone(target_freq, duration)
        print(tone)
        return pygame.sndarray.make_sound((tone * 32767).astype(np.int16))

    def get_c(self):
        return self.C

    def get_d(self):
        return self.D

    def get_e(self):
        return self.E

    def get_f(self):
        return self.F

    def get_g(self):
        return self.G

    def get_a(self):
        return self.A

    def get_b(self):
        return self.B
