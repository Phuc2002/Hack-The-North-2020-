from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

key = "API-KEY"
endpoint = "https://smartnote2.cognitiveservices.azure.com/"

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client


client = authenticate_client()


def key_phrase_extraction_example(client, all_text):

    #with open ("audio-to-text\output.txt", "r") as myfile:
    keywords = list()
    data = all_text

    try:
        documents = [str(data)]

        response = client.extract_key_phrases(documents = documents)[0]

        if not response.is_error:
            #print("\tKey Phrases:")
            for phrase in response.key_phrases:
                #print("\t\t", phrase)
                keywords.append(phrase)
        else:
            print(response.id, response.error)


    except Exception as err:
        print("Encountered exception. {}".format(err))

    return keywords
    
