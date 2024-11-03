import pygame
import numpy as np
import time
from GetSound import GetSound

# Initialize Pygame
pygame.init()
screen_width, screen_height = 800, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Musical Note Generator with Sine Wave Visualization")

# Define sample rate and initial parameters
sample_rate = 44100
duration = 2.0  # Maximum duration for sound decay in seconds
initial_volume = 1.0

gs = GetSound()

def generate_tone(frequency, duration):
    """Generates a continuous tone as a stereo wave array."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)
    stereo_wave = np.stack((wave, wave), axis=-1)  # Stereo wave
    return stereo_wave

frequencies = {
    (pygame.K_a,): gs.get_c3(),  # C3
    (pygame.K_s,): gs.get_D3(),  # D3
    (pygame.K_d,): gs.get_E3(),  # E3
    (pygame.K_f,): gs.get_F3(),  # F3
    (pygame.K_g,): gs.get_G3(),  # G3
    (pygame.K_h,): gs.get_A3(),  # A3
    (pygame.K_j,): gs.get_B3(),  # B3
    (pygame.K_z, pygame.K_1): gs.get_c_hash()  # C# for combo (Z + 1)
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
                sound.play(-1)  # Play sound on loop
                start_time = time.time()
                playing_notes[key_combo] = {'sound': sound, 'start_time': start_time}
        
                # If this note is repeated, mute it momentarily
                if previous_note == key_combo:
                    sound.set_volume(0)

    # Key release logic
    for key_combo in list(playing_notes.keys()):
        if not all(keys_pressed[key] for key in key_combo):  # If any key in the combo is released
            playing_notes[key_combo]['sound'].fadeout(1000)  # Smooth fade-out over 1 second
            del playing_notes[key_combo]

    # Handle real-time amplitude decay for each playing note
    for key_combo, note_data in playing_notes.items():
        elapsed_time = time.time() - note_data['start_time']  # Calculate elapsed time
        if elapsed_time > duration:
            note_data['sound'].fadeout(500)  # Fade out sound smoothly if max duration exceeded
            del playing_notes[key_combo]
        else:
            # Adjust volume based on elapsed time for smooth decay
            volume = max(initial_volume - (elapsed_time / duration), 0)
            note_data['sound'].set_volume(volume)
        previous_note = key_combo

    # Clear the screen and update display
    screen.fill((0, 0, 0))
    pygame.display.flip()
