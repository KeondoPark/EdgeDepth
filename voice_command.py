import random
import time

import speech_recognition as sr
import rs_snapshot

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    #print("Running voice recognition module...")
    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

if __name__ == "__main__":
    
    PROMPT_LIMIT = 5
    WAKE_UP_WORD = 'kd'

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    #microphone = sr.Microphone(device_index=2)
    microphone = sr.Microphone()
    
    #for i in range(NUM_GUESSES):
        # get the guess from the user
        # if a transcription is returned, break out of the loop and
        #     continue
        # if no transcription returned and API request failed, break
        #     loop and continue
        # if API request succeeded but no transcription was returned,
        #     re-prompt the user to say their guess again. Do this up
        #     to PROMPT_LIMIT times
    while True:
        print("If you want to give instruction, wake up me by saying ", WAKE_UP_WORD)
        listening = recognize_speech_from_mic(recognizer, microphone)
        if listening['transcription']:
            print("Captured voice:", listening['transcription'])
        if listening['transcription'] and listening['transcription'].lower() == WAKE_UP_WORD:            
        
            # format the instructions string
            instructions = "Now woke up. Please wait for 1 second before you give instruction"

            # show instructions and wait 3 seconds before receiving instruction
            print(instructions)
            time.sleep(1)
            
            for j in range(PROMPT_LIMIT):        
                print('Speak now!')
                response = recognize_speech_from_mic(recognizer, microphone)
                if response['transcription']:
                    break
                if not response['success']:
                    break
                if not response["success"]:
                    print("I didn't catch that. What did you say?\n")
                    
            if response["error"]:
                print("Error:{}".format(guess["error"]))
            elif not response["success"]:
                print("I didn't catch that. Exiting program..\n")
            else:            
                # show the user the transcription
                print("You said: {}".format(response["transcription"]))

                if response["transcription"].lower() == 'snapshot':
                    print("Valid instruction for taking depth snapshot, now starting to take depth snapshot")
                    rs_snapshot.take_snapshot()
                    break
