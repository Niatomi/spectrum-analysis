import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import IPython.display as ipd
import librosa.display

RESOURCES_PATH = './resources'

SAMPLE_RATE = 44100  # Гц
DURATION = 5  # Секунды

def main():
    matplotlib.use('TkAgg')

    audio_paths = []
    for file in os.listdir(RESOURCES_PATH):
        audio_paths.append(os.path.join(RESOURCES_PATH, file))

    for audio in audio_paths:
        x, sr = librosa.load(audio, sr=None)
        X = librosa.stft(x)
        Xdb = librosa.amplitude_to_db(abs(X))
        plt.figure(figsize=(14, 5))
        librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')

        plt.title(audio.removeprefix(RESOURCES_PATH + '\\'))
        plt.colorbar()
        plt.show()

if __name__ == "__main__":
    main()