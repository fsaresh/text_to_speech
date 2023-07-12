from voices import find_voices, speak_text

# See voices.py and find_voices function for other voices
VOICE_INDEX = 7


def main():
    # To pick a voice, uncomment the below line and listen through the options
    # find_voices(speech_to_say="sample text to say", language='en')

    with open("speech.txt") as file:
        speech_to_say = file.read()
        speak_text(speech_to_say=speech_to_say, voice_index_to_use=VOICE_INDEX)


if __name__ == '__main__':
    main()
