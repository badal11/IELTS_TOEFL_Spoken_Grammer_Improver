from audio_recorder import record_audio
from transcriber import transcribe_audio
from grammar_checker import grammar_check

if __name__ == '__main__':
    audio_file = 'recorded_audio.wav'
    model_path = 'deepspeech_model.pbmm'  # We need to provide the Path to DeepSpeech model

    # Record audio
    record_audio(audio_file)

    # Transcribe audio
    transcribed_text = transcribe_audio(audio_file, model_path)
    print("Transcription:", transcribed_text)

    # Grammar check
    doc, grammar_errors = grammar_check(transcribed_text)
    print("Grammar Errors:", grammar_errors)

    # Highlight errors and prodice corrected text
    corrected_text = highlight_errors_and_correct(doc, grammar_errors)
    print("Highlighted and Corrected Text:\n", corrected_text)
