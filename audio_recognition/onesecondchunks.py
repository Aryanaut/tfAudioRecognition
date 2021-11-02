import pyaudio
import sys
import wave

chunk = 4096
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "output.wav"
NFRAMES = int((RATE * RECORD_SECONDS) / chunk)

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT, 
                channels = CHANNELS, 
                rate = RATE, 
                input = True, 
                frames_per_buffer = chunk, 
                input_device_index = 1)
frames = []

for i in range(0, int(NFRAMES / 2)):
    data = stream.read(chunk, exception_on_overflow = False)
    frames.append(data)


print("Program terminated")
stream.stop_stream()
stream.close()
p.terminate()
# Save the recorded data as a WAV file
wf = wave.open("output.wav", 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()