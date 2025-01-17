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

base_frequency = BaseFrequency()

C3 = GetSound(base_frequency.c3)
C4 = GetSound(base_frequency.c4)
C5 = GetSound(base_frequency.c5)
C6 = GetSound(base_frequency.c6)
C7 = GetSound(base_frequency.c7)
C8 = GetSound(base_frequency.c8)

frequencies = {
    (pygame.K_a, pygame.K_1): {"normal": C3.get_c(),
                               "sharp": C3.get_c_s()
                               },
    (pygame.K_a, pygame.K_2): {"normal": C3.get_d(),
                               "sharp": C3.get_d_s()
                               },
    (pygame.K_a, pygame.K_3): {"normal": C3.get_e(),
                               "sharp": C3.get_e()
                               },
    (pygame.K_a, pygame.K_4): {"normal": C3.get_f(),
                               "sharp": C3.get_f_s()
                               },
    (pygame.K_a, pygame.K_5): {"normal": C3.get_g(),
                               "sharp": C3.get_g_s()
                               },
    (pygame.K_a, pygame.K_6): {"normal": C3.get_a(),
                               "sharp": C3.get_a_s()
                               },
    (pygame.K_a, pygame.K_7): {"normal": C3.get_b(),
                               "sharp": C3.get_b()
                               },


    (pygame.K_s, pygame.K_1): {"normal": C4.get_c(),
                               "sharp": C4.get_c_s()
                               },
    (pygame.K_s, pygame.K_2): {"normal": C4.get_d(),
                               "sharp": C4.get_d_s()
                               },
    (pygame.K_s, pygame.K_3): {"normal": C4.get_e(),
                               "sharp": C4.get_e()
                               },
    (pygame.K_s, pygame.K_4): {"normal": C4.get_f(),
                               "sharp": C4.get_f_s()
                               },
    (pygame.K_s, pygame.K_5): {"normal": C4.get_g(),
                               "sharp": C4.get_g_s()
                               },
    (pygame.K_s, pygame.K_6): {"normal": C4.get_a(),
                               "sharp": C4.get_a_s()
                               },
    (pygame.K_s, pygame.K_7): {"normal": C4.get_b(),
                               "sharp": C4.get_b()
                               },

    (pygame.K_d, pygame.K_1): {"normal": C5.get_c(),
                               "sharp": C5.get_c_s()
                               },
    (pygame.K_d, pygame.K_2): {"normal": C5.get_d(),
                               "sharp": C5.get_d_s()
                               },
    (pygame.K_d, pygame.K_3): {"normal": C5.get_e(),
                               "sharp": C5.get_e()
                               },
    (pygame.K_d, pygame.K_4): {"normal": C5.get_f(),
                               "sharp": C5.get_f_s()
                               },
    (pygame.K_d, pygame.K_5): {"normal": C5.get_g(),
                               "sharp": C5.get_g_s()
                               },
    (pygame.K_d, pygame.K_6): {"normal": C5.get_a(),
                               "sharp": C5.get_a_s()
                               },
    (pygame.K_d, pygame.K_7): {"normal": C5.get_b(),
                               "sharp": C5.get_b()
                               },

    (pygame.K_f, pygame.K_1): {"normal": C6.get_c(),
                               "sharp": C6.get_c_s()
                               },
    (pygame.K_f, pygame.K_2): {"normal": C6.get_d(),
                               "sharp": C6.get_d_s()
                               },
    (pygame.K_f, pygame.K_3): {"normal": C6.get_e(),
                               "sharp": C6.get_e()
                               },
    (pygame.K_f, pygame.K_4): {"normal": C6.get_f(),
                               "sharp": C6.get_f_s()
                               },
    (pygame.K_f, pygame.K_5): {"normal": C6.get_g(),
                               "sharp": C6.get_g_s()
                               },
    (pygame.K_f, pygame.K_6): {"normal": C6.get_a(),
                               "sharp": C6.get_a_s()
                               },
    (pygame.K_f, pygame.K_7): {"normal": C6.get_b(),
                               "sharp": C6.get_b()
                               },

    (pygame.K_g, pygame.K_1): {"normal": C7.get_c(),
                               "sharp": C7.get_c_s()
                               },
    (pygame.K_g, pygame.K_2): {"normal": C7.get_d(),
                               "sharp": C7.get_d_s()
                               },
    (pygame.K_g, pygame.K_3): {"normal": C7.get_e(),
                               "sharp": C7.get_e()
                               },
    (pygame.K_g, pygame.K_4): {"normal": C7.get_f(),
                               "sharp": C7.get_f_s()
                               },
    (pygame.K_g, pygame.K_5): {"normal": C7.get_g(),
                               "sharp": C7.get_g_s()
                               },
    (pygame.K_g, pygame.K_6): {"normal": C7.get_a(),
                               "sharp": C7.get_a_s()
                               },
    (pygame.K_g, pygame.K_7): {"normal": C7.get_b(),
                               "sharp": C7.get_b()
                               },

    (pygame.K_h, pygame.K_1): {"normal": C8.get_c(),
                               "sharp": C8.get_c_s()
                               },
    (pygame.K_h, pygame.K_2): {"normal": C8.get_d(),
                               "sharp": C8.get_d_s()
                               },
    (pygame.K_h, pygame.K_3): {"normal": C8.get_e(),
                               "sharp": C8.get_e()
                               },
    (pygame.K_h, pygame.K_4): {"normal": C8.get_f(),
                               "sharp": C8.get_f_s()
                               },
    (pygame.K_h, pygame.K_5): {"normal": C8.get_g(),
                               "sharp": C8.get_g_s()
                               },
    (pygame.K_h, pygame.K_6): {"normal": C8.get_a(),
                               "sharp": C8.get_a_s()
                               },
    (pygame.K_h, pygame.K_7): {"normal": C8.get_b(),
                               "sharp": C8.get_b()
                               }
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
    mods = pygame.key.get_mods()

    # Add an extra key like shift, when pressed the tone should start playing from the volume/amplitude of currently playing tone
    # (simulate string_slide effect)

    # Loop through each key combination in frequencies
    for key_combo, freq_variants in frequencies.items():
        # Check if the current key combination is pressed
        if all(keys_pressed[key] for key in key_combo):

            if mods & pygame.KMOD_SHIFT:
                frequency = freq_variants["sharp"]
            else:
                frequency = freq_variants["normal"]

            print(key_combo)
            if key_combo not in playing_notes:
                starting_volume = 0
                if previous_note and (previous_note in playing_notes):
                    starting_volume = playing_notes[previous_note]["sound"].get_volume()

                # Convert to sound format
                sound = frequency
                sound.set_volume(starting_volume if mods & pygame.KMOD_SHIFT else initial_volume)
                sound.play()  # Play sound on loop

                playing_notes[key_combo] = {"sound": sound, "start_time": time.time()}
                print(playing_notes, previous_note)

            # If this note is repeated, mute it momentarily
            previous_note = key_combo

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

    # Clear the screen and update display
    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)
