import IPython as ipd
from scipy.io import wavfile
import noisereduce as nr
import soundfile as sf
from noisereduce.generate_noise import band_limited_noise
import matplotlib.pyplot as plt
import urllib.request
import numpy as np
import io
import librosa
data, sr = librosa.load(r'/content/drive/MyDrive/AmpersandProfiles/sample.wav')
ipd.display.Audio('/content/drive/MyDrive/AmpersandProfiles/sample.wav', autoplay=False)
fig, ax = plt.subplots(figsize=(20,3))
ax.plot(data)
noise = band_limited_noise(min_freq=3000, max_freq = 18000, samples=len(data), samplerate=sr)*10
audio_clip_band_limited = data + noise
reduced_noise = nr.reduce_noise(y = audio_clip_band_limited, sr=sr,stationary=False)
fig, ax = plt.subplots(figsize=(20,3))
ax.plot(data)
fig, ax = plt.subplots(figsize=(20,3))
ax.plot(reduced_noise)
ipd.display.Audio(data=reduced_noise, rate=sr)