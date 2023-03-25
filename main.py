from helper import find_voices, speak_text

# See helper.py and find_voices function for other voices
VOICE_INDEX = 7


def main():
    with open("speech.txt") as file:
        speech_to_say = file.read()

        # find_voices(speech_to_say="sample text to say", language='en')
        speak_text(speech_to_say=speech_to_say, voice_index_to_use=VOICE_INDEX)


if __name__ == '__main__':
    main()
