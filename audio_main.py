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
duration = 2  # Maximum duration for sound decay in seconds
initial_volume = 1.0

base_frequency =BaseFrequency()

C3 = GetSound(base_frequency.c3)
C4 = GetSound(base_frequency.c4)
C5 = GetSound(base_frequency.c5)
C6 = GetSound(base_frequency.c6)
C7 = GetSound(base_frequency.c7)
C8 = GetSound(base_frequency.c8)

frequencies = {
    (pygame.K_a, pygame.K_1): C3.get_c(),
    (pygame.K_a, pygame.K_2): C3.get_d(),
    (pygame.K_a, pygame.K_3): C3.get_e(),
    (pygame.K_a, pygame.K_4): C3.get_f(),
    (pygame.K_a, pygame.K_5): C3.get_g(),
    (pygame.K_a, pygame.K_6): C3.get_a(),
    (pygame.K_a, pygame.K_7): C3.get_b(),

    (pygame.K_s, pygame.K_1): C4.get_c(),
    (pygame.K_s, pygame.K_2): C4.get_d(),
    (pygame.K_s, pygame.K_3): C4.get_e(),
    (pygame.K_s, pygame.K_4): C4.get_f(),
    (pygame.K_s, pygame.K_5): C4.get_g(),
    (pygame.K_s, pygame.K_6): C4.get_a(),
    (pygame.K_s, pygame.K_7): C4.get_b(),

    (pygame.K_d, pygame.K_1): C5.get_c(),
    (pygame.K_d, pygame.K_2): C5.get_d(),
    (pygame.K_d, pygame.K_3): C5.get_e(),
    (pygame.K_d, pygame.K_4): C5.get_f(),
    (pygame.K_d, pygame.K_5): C5.get_g(),
    (pygame.K_d, pygame.K_6): C5.get_a(),
    (pygame.K_d, pygame.K_7): C5.get_b(),

    (pygame.K_f, pygame.K_1): C6.get_c(),
    (pygame.K_f, pygame.K_2): C6.get_d(),
    (pygame.K_f, pygame.K_3): C6.get_e(),
    (pygame.K_f, pygame.K_4): C6.get_f(),
    (pygame.K_f, pygame.K_5): C6.get_g(),
    (pygame.K_f, pygame.K_6): C6.get_a(),
    (pygame.K_f, pygame.K_7): C6.get_b(),

    (pygame.K_g, pygame.K_1): C7.get_c(),
    (pygame.K_g, pygame.K_2): C7.get_d(),
    (pygame.K_g, pygame.K_3): C7.get_e(),
    (pygame.K_g, pygame.K_4): C7.get_f(),
    (pygame.K_g, pygame.K_5): C7.get_g(),
    (pygame.K_g, pygame.K_6): C7.get_a(),
    (pygame.K_g, pygame.K_7): C7.get_b(),

    (pygame.K_h, pygame.K_1): C8.get_c(),
    (pygame.K_h, pygame.K_2): C8.get_d(),
    (pygame.K_h, pygame.K_3): C8.get_e(),
    (pygame.K_h, pygame.K_4): C8.get_f(),
    (pygame.K_h, pygame.K_5): C8.get_g(),
    (pygame.K_h, pygame.K_6): C8.get_a(),
    (pygame.K_h, pygame.K_7): C8.get_b(),
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
                print(key_combo)
                if previous_note == key_combo:
                    sound.set_volume(0)
                # Convert to sound format
                sound = frequency
                sound.set_volume(initial_volume)
                sound.play()  # Play sound on loop
                playing_notes[key_combo] = {"sound": sound, "start_time": time.time()}

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
        if key_combo in playing_notes:
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
