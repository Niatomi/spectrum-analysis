import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import IPython.display as ipd
import librosa.display
import numpy
import scipy
from scipy.fft import fft, fftfreq

RESOURCES_PATH = './resources'

SAMPLE_RATE = 44100  # Гц
DURATION = 5  # Секунды

def main():
    matplotlib.use('TkAgg')

    """ Анализ аудио """

    def audio_analysis():
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

    """ Анализ генрируемого сигнала """

    def generate_sine_wave(freq, sample_rate, duration):
        x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
        frequencies = x * freq
        # 2pi для преобразования в радианы
        y = np.sin((2 * np.pi) * frequencies)
        return x, y

    def furrier_analysis():
        x, y = generate_sine_wave(2, SAMPLE_RATE, DURATION)
        plt.plot(x, y)
        plt.show()

    # _, nice_tone = generate_sine_wave(400, SAMPLE_RATE, DURATION)
    # _, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
    #
    # noise_tone = noise_tone * 0.3
    # mixed_tone = nice_tone + noise_tone
    # normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)
    #
    # # plt.plot(normalized_tone[:1000])
    # # plt.show()
    #
    # N = SAMPLE_RATE * DURATION
    #
    # yf = fft(normalized_tone)
    # xf = fftfreq(N, 1 / SAMPLE_RATE)
    #
    # plt.plot(xf, np.abs(yf))
    # plt.show()

if __name__ == "__main__":
    main()
