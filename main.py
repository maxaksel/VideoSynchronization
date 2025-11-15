import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.io.wavfile as wav

def get_waveform_from_wav(filename: str) -> np.array:
  (sampling_rate, audio_signal) = wav.read(filename)
  signal_length = audio_signal.shape[0] / sampling_rate
  time_axis = np.linspace(0.0, signal_length, audio_signal.shape[0])

  return time_axis, audio_signal[:, 0] / np.max(audio_signal[:, 0])


def main():
    print("Hello from videosynchronization!")
    time_axis2, audio2 = get_waveform_from_wav("data/max_sample1.wav")
    plt.plot(time_axis2, audio2)
    plt.show()


if __name__ == "__main__":
    main()
