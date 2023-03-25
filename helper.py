import pyttsx3


def find_voices(speech_to_say: str, language: str):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice_counter in range(len(voices)):
        voice = voices[voice_counter]
        # Restrict voices to English based ones for phoneme consistency
        if language not in voice.languages[0]:
            continue

        print(f"Trying out voice #{voice_counter} with metadata: {voice}")
        engine.setProperty('voice', voice.id)
        engine.say(speech_to_say)
        engine.runAndWait()
    engine.stop()


def speak_text(speech_to_say: str, voice_index_to_use: int):
    # Function to convert text to speech
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_index_to_use])
    engine.say(speech_to_say)
    engine.runAndWait()
    engine.stop()
