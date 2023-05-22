import pyaudio as pa
import numpy as np

audio = pa.PyAudio()

stream = audio.open(format=pa.paFloat32,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)

while True:
    data = stream.read(1024)
    audio_data = np.frombuffer(data, dtype=np.float32)

    rms = np.sqrt(np.mean(audio_data**2))

    decibels = 20 * np.log10(rms)
    print("Decibels: ", decibels)

    if decibels > 20:
        stream.close()
        audio.terminate()
        print("Warning: Shouting can cause hypertension. How about you shut up for a minute, for your own health and everyone else's sanity?")

