import pygame
import numpy as np
import time
from GetSound import GetSound
from BaseFrequency import BaseFrequency
import random

# Initialize Pygame
pygame.init()
screen_width, screen_height = 800, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Musical Note Generator with Sine Wave Visualization")

# Define sample rate and initial parameters
sample_rate = 44100
duration = 2.0  # Maximum duration for sound decay in seconds
initial_volume = 1.0

base_frequency =BaseFrequency()

C = GetSound(base_frequency.c)
D = GetSound(base_frequency.d)
E = GetSound(base_frequency.e)
F = GetSound(base_frequency.f)
G = GetSound(base_frequency.g)
A = GetSound(base_frequency.a)
B = GetSound(base_frequency.b)


def generate_tone(frequency, duration):
    """Generates a continuous tone as a stereo wave array."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)
    stereo_wave = np.stack((wave, wave), axis=-1)  # Stereo wave
    return stereo_wave


frequencies = {
    (pygame.K_a, pygame.K_0): C.get_fh(),
    (pygame.K_a, pygame.K_1): C.get_sh(),
    (pygame.K_a, pygame.K_2): C.get_th(),
    (pygame.K_a, pygame.K_3): C.get_fth(),
    (pygame.K_a, pygame.K_4): C.get_fih(),
    (pygame.K_a, pygame.K_5): C.get_sh(),
    (pygame.K_a, pygame.K_6): C.get_seh(),

    (pygame.K_s, pygame.K_0): D.get_fh(), # D3
    (pygame.K_s, pygame.K_1): D.get_sh(),
    (pygame.K_s, pygame.K_2): D.get_th(),
    (pygame.K_s, pygame.K_3): D.get_fth(),
    (pygame.K_s, pygame.K_4): D.get_fih(),
    (pygame.K_s, pygame.K_5): D.get_sh(),
    (pygame.K_s, pygame.K_6): D.get_seh(),  

    (pygame.K_d, pygame.K_0): E.get_fh(),  # E3
    (pygame.K_d, pygame.K_1): E.get_sh(),
    (pygame.K_d, pygame.K_2): E.get_th(),
    (pygame.K_d, pygame.K_3): E.get_fth(),
    (pygame.K_d, pygame.K_4): E.get_fih(),
    (pygame.K_d, pygame.K_5): E.get_sh(),
    (pygame.K_d, pygame.K_6): E.get_seh(),

    (pygame.K_f, pygame.K_0): F.get_fh(),  # F3
    (pygame.K_f, pygame.K_1): F.get_sh(),
    (pygame.K_f, pygame.K_2): F.get_th(),
    (pygame.K_f, pygame.K_3): F.get_fth(),
    (pygame.K_f, pygame.K_4): F.get_fih(),
    (pygame.K_f, pygame.K_5): F.get_sh(),
    (pygame.K_f, pygame.K_6): F.get_seh(),

    (pygame.K_g, pygame.K_0): G.get_fh(),  # G3
    (pygame.K_g, pygame.K_1): G.get_sh(),
    (pygame.K_g, pygame.K_2): G.get_th(),
    (pygame.K_g, pygame.K_3): G.get_fth(),
    (pygame.K_g, pygame.K_4): G.get_fih(),
    (pygame.K_g, pygame.K_5): G.get_sh(),
    (pygame.K_g, pygame.K_6): G.get_seh(),

    (pygame.K_h, pygame.K_0): A.get_fh(),  # A3
    (pygame.K_h, pygame.K_1): A.get_sh(),
    (pygame.K_h, pygame.K_2): A.get_th(),
    (pygame.K_h, pygame.K_3): A.get_fth(),
    (pygame.K_h, pygame.K_4): A.get_fih(),
    (pygame.K_h, pygame.K_5): A.get_sh(),
    (pygame.K_h, pygame.K_6): A.get_seh(),

    (pygame.K_j, pygame.K_0): B.get_fh(),  # B3
    (pygame.K_j, pygame.K_1): B.get_sh(),
    (pygame.K_j, pygame.K_2): B.get_th(),
    (pygame.K_j, pygame.K_3): B.get_fth(),
    (pygame.K_j, pygame.K_4): B.get_fih(),
    (pygame.K_j, pygame.K_5): B.get_sh(),
    (pygame.K_j, pygame.K_6): B.get_seh(),  # B3
}

playing_notes = {}
previous_note = None

# Main loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Check current keys pressed
    keys_pressed = pygame.key.get_pressed()

    # Loop through each key combination in frequencies
    for key_combo, frequency in frequencies.items():
        # Check if the current key combination is pressed
        if all(keys_pressed[key] for key in key_combo):
            if key_combo not in playing_notes:
                jitter_delay = random.randint(10, 50)
                print(jitter_delay)  # Random delay to avoid overlap beats
                pygame.time.delay(jitter_delay)
                print(key_combo)
                if previous_note == key_combo:
                    sound.set_volume(0)
                # Convert to sound format
                sound = frequency
                sound.set_volume(initial_volume)
                sound.play(-1)  # Play sound on loop
                start_time = time.time()
                playing_notes[key_combo] = {"sound": sound, "start_time": start_time}

                # If this note is repeated, mute it momentarily
                if previous_note == key_combo:
                    sound.set_volume(0)

    # Key release logic
    for key_combo in list(playing_notes.keys()):
        if not all(
            keys_pressed[key] for key in key_combo
        ):  # If any key in the combo is released
            playing_notes[key_combo]["sound"].fadeout(
                1000
            )  # Smooth fade-out over 1 second
            del playing_notes[key_combo]

    # Handle real-time amplitude decay for each playing note
    for key_combo, note_data in list(playing_notes.items()):
        elapsed_time = time.time() - note_data["start_time"]  # Calculate elapsed time
        if elapsed_time > duration:
            note_data["sound"].fadeout(
                500
            )  # Fade out sound smoothly if max duration exceeded
            del playing_notes[key_combo]
        else:
            # Adjust volume based on elapsed time for smooth decay
            volume = max(initial_volume - (elapsed_time / duration), 0)
            note_data["sound"].set_volume(volume)
        previous_note = key_combo

    # Clear the screen and update display
    screen.fill((0, 0, 0))
    pygame.display.flip()
