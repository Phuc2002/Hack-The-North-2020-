import azure.cognitiveservices.speech as speechsdk
import time


def A2T(wav_file):
    speech_config = speechsdk.SpeechConfig(subscription="c332c1bc68b441c7892e47f8345baa53", region="eastus")
    audio_input = speechsdk.AudioConfig(filename=wav_file)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
    speech_config.enable_dictation()

    done = False

    def stop_cb(evt):
        print('CLOSING on {}'.format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True

    all_results = []
    def handle_final_result(evt):
        all_results.append(evt.result.text)

    speech_recognizer.recognized.connect(handle_final_result)

    speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
    speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt)))
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))

    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)

    #print(all_results)
    # Function to convert   
    def listToString(s):  
    
        # initialize an empty string 
        str1 = " " 
        
        # return string   
        return (str1.join(s))


    return listToString(all_results)

    """with open(wav_file + ".txt",'w') as f:
        for line in all_results:
            f.writelines(line+'\n')"""




