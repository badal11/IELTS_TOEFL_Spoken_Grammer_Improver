import pyaudio
import wave


def record_audio(file_path, duration=10, sample_rate=44100):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=1024)

    frames = []
    print("Recording...")
    for _ in range(0, int(sample_rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))


if __name__ == '__main__':
    audio_file = 'recorded_audio.wav'
    record_audio(audio_file)
