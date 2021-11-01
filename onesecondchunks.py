import pyaudio
import sys
import wave

chunk = 4096
FORMAT = pyaudio.paInt32
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

for i in range(0, NFRAMES):
    data = stream.read(chunk, exception_on_overflow = False)

    try:
        while True:
            print("Listening...")
            frames = []
            for i in range(0, NFRAMES):
                data = stream.read(chunk, exception_on_overflow = False)
                frames.append(data)
    except KeyboardInterrupt:
        print("Program terminated")
    
    
    stream.stop_stream()
    stream.close()
    p.terminate()
