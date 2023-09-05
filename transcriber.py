import deepspeech
import wave


def transcribe_audio(audio_file, model_path):
    model = deepspeech.Model(model_path)
    model.set_silence_threshold(20)  # We can adjust silence threshold as needed

    with wave.open(audio_file, 'rb') as wf:
        audio_data = wf.readframes(wf.getnframes())
        text = model.stt(audio_data)

    return text


if __name__ == '__main__':
    audio_file = 'recorded_audio.wav'
    model_path = 'deepspeech_model.pbmm'  # We need to provide Path to the DeepSpeech model
    transcribed_text = transcribe_audio(audio_file, model_path)
    print("Transcription:", transcribed_text)
