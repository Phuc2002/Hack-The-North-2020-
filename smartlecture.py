import split
import data
import audio_extraction
import audio_to_text 
import keywords
import time

#data.post("COMP 2804B, Fall 2020, Lecture 1, Part 1.mp4","C:/Users/ilong/AppData/Local/Programs/Microsoft VS Code/Law of demand Supply demand and market equilibrium Microeconomics Khan Academy.mp4")


#time.sleep(10)

'''split.split_video()
#time.sleep(20)

temp = data.download()
#print(temp)
wav_list = list()
for i in temp:
    wav_list.append(audio_extraction.audio_extractor(i))

all_texts = dict()
# WAV vs. ITS TEXT key-value pair ...string wav file path vs. a string of text
for wav in wav_list:
    all_texts[wav] = audio_to_text.A2T(wav)

# string wav file path vs. string of keywords?
all_keywords = dict()
for item in all_texts:
    all_keywords[item] = keywords.key_phrase_extraction_example(keywords.client, all_texts[item])


for wav in all_keywords:
    print("Key Phrase - " + wav)
    for kword in all_keywords[wav]:
        print("\t" + kword)

reversed_dict = dict()


def reverse_key_val(all_keywords):
    for wav in all_keywords:
        for kword in all_keywords[wav]:
            if kword not in reversed_dict:
                reversed_dict[kword] = list()
            reversed_dict[kword].append(wav)

reverse_key_val(all_keywords)

#print(reversed_dict)



def search_lecture(keyword):
    return reversed_dict[keyword]

#print(search_lecture("Amazon"))'''

data.delete()