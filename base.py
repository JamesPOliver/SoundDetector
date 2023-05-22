import pyaudio as pa
import numpy as np
import wave as wv

audio = pa.PyAudio()

stream = audio.open(format=pa.paFloat32,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)

shout = 80

output_file = wv.open('captured_sound.wav', 'wb')
output_file.setnchannels(1)
output_file.setsampwidth(audio.get_sample_size(pa.paFloat32))
output_file.setframerate(44100)

while True:
    data = stream.read(1024)
    audio_data = np.frombuffer(data, dtype=np.float32)

    rms = np.sqrt(np.mean(audio_data**2))

    decibels = 20 * np.log10(rms)
    print("Decibels: ", decibels)

    output_file.writeframes(data)

    if decibels > shout or output_file.tell() > 44100 * 5:
        output_file.close()
        stream.close()
        audio.terminate()
        print("Warning: Shouting can cause hypertension. How about you shut up for a minute, for your own health and everyone else's sanity?")
    
    
