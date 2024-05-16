import speech_recognition as sr

def test_microphone():
    recognizer = sr.Recognizer()

    #available microphones
    microphones = sr.Microphone.list_microphone_names()
    print("Available microphones:")
    for index, name in enumerate(microphones):
        print(f"{index}: {name}")

    #select the correct microphone (change the index if needed)
    mic_index = 1  #change it here for mic choice

    try:
        with sr.Microphone(device_index=mic_index) as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Please speak into the microphone...")
            audio = recognizer.listen(source)
            print("Got audio, processing...")

        try:
            recognized_text = recognizer.recognize_google(audio)
            print("You said:", recognized_text)
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Error with the request; {e}")
    except AssertionError as e:
        print(f"Assertion error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

test_microphone()
