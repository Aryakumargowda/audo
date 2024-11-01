import numpy as np
from scipy.io.wavfile import write

def generate_tone(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)
    return wave

# Define frequencies for C3 to B3
frequencies = {
    'C3': 261.63,
    'D3': 293.66,
    'E3': 329.63,
    'F3': 349.23,
    'G3': 392.00,
    'A3': 440.00,
    'B3': 493.88,
}

# Generate and save each tone as a WAV file
for note_name, freq in frequencies.items():
    tone = generate_tone(freq, duration=1)  # Generate tone for 1 second
    write(f"{note_name}.wav", 44100, tone.astype(np.float32))  # Save as WAV file