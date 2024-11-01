import pygame
import numpy as np
import time

# Initialize Pygame
pygame.init()
screen_width, screen_height = 800, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Musical Note Generator with Sine Wave Visualization")

# Define sample rate and initial parameters
sample_rate = 44100
duration = 2.0  # Maximum duration for sound decay in seconds
initial_volume = 1.0

def generate_tone(frequency, duration):
    """Generates a continuous tone as a stereo wave array."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)
    stereo_wave = np.stack((wave, wave), axis=-1)  # Stereo wave
    return stereo_wave

frequencies = {
    pygame.K_a: 261.63,  # C3
    pygame.K_s: 293.66,  # D3
    pygame.K_d: 329.63,  # E3
    pygame.K_f: 349.23,  # F3
    pygame.K_g: 392.00,  # G3
    pygame.K_h: 440.00,  # A3
    pygame.K_j: 493.88,  # B3
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

        # Key down event
        if event.type == pygame.KEYDOWN:
            if event.key in frequencies and event.key not in playing_notes:
                frequency = frequencies[event.key]
                tone = generate_tone(frequency, duration)
                if previous_note == event.key:
                    sound.set_volume(0)
                sound = pygame.sndarray.make_sound((tone * 32767).astype(np.int16))  # Convert to sound format
                sound.set_volume(initial_volume)  # Set initial volume
                sound.play(-1)  # Play sound on loop
                start_time = time.time()
                playing_notes[event.key] = {'sound': sound, 'start_time': start_time}

        # Key up event
        if event.type == pygame.KEYUP:
            if event.key in playing_notes:
                playing_notes[event.key]['sound'].fadeout(1000)  # Smooth fade-out over 1 second
                del playing_notes[event.key]

    # Handle real-time amplitude decay for each playing note
    for key in list(playing_notes.keys()):
        note_data = playing_notes[key]
        sound.set_volume(initial_volume)
        elapsed_time = time.time() - note_data['start_time']  # Calculate elapsed time
        if elapsed_time > duration:
            note_data['sound'].fadeout(500)  # Fade out sound smoothly if max duration exceeded
            del playing_notes[key]
        else:
            # Adjust volume based on elapsed time for smooth decay
            volume = max(initial_volume - (elapsed_time / duration), 0)
            note_data['sound'].set_volume(volume)  # Update volume smoothly
        previous_note = key

    screen.fill((0, 0, 0))
    pygame.display.flip()


# create sound class and load all the sound frequency
# Access these sounds once loaded hopefully it we dont here breaks.