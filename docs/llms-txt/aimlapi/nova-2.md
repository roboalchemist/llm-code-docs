# Source: https://docs.aimlapi.com/api-references/speech-models/speech-to-text/deepgram/nova-2.md

# nova-2

{% hint style="info" %}
This documentation is valid for the following list of our models:

* `#g1_nova-2-automotive`
* `#g1_nova-2-conversationalai`
* `#g1_nova-2-drivethru`
* `#g1_nova-2-finance`
* `#g1_nova-2-general`
* `#g1_nova-2-medical`
* `#g1_nova-2-meeting`
* `#g1_nova-2-phonecall`
* `#g1_nova-2-video`
* `#g1_nova-2-voicemail`
  {% endhint %}

## Model Overview

Nova-2 builds on the advancements of Nova-1 with speech-specific optimizations to its Transformer architecture, refined data curation techniques, and a multi-stage training approach. These improvements result in a lower word error rate (WER) and better entity recognition (including proper nouns and alphanumeric sequences), as well as enhanced punctuation and capitalization.

Nova-2 offers the following model options:

* **automotive**: Optimized for audio with automotive oriented vocabulary.
* **conversationalai**: Optimized for use cases in which a human is talking to an automated bot, such as IVR, a voice assistant, or an automated kiosk.
* **drivethru**: Optimized for audio sources from drivethrus.
* **finance**: Optimized for multiple speakers with varying audio quality, such as might be found on a typical earnings call. Vocabulary is heavily finance oriented.
* **general**: Optimized for everyday audio processing.
* **medical**: Optimized for audio with medical oriented vocabulary.
* **meeting**: Optimized for conference room settings, which include multiple speakers with a single microphone.
* **phonecall**: Optimized for low-bandwidth audio phone calls.
* **video**: Optimized for audio sourced from videos.
* **voicemail**: Optimized for low-bandwidth audio clips with a single speaker. Derived from the phonecall model.

{% hint style="success" %}
Nova-2 models use per-second billing. The cost of audio transcription is based on the number of seconds in the input audio file, not the processing time.
{% endhint %}

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## Quick Code Examples

Let's use the `#g1_nova-2-meeting` model to transcribe the following audio fragment:

{% embed url="<https://drive.google.com/file/d/1ZN-28NUbK1TXHt6oEPj42zUJCv82e9L4/view?usp=sharing>" %}

### Example #1: Processing a Speech Audio File via URL

<pre class="language-python" data-overflow="wrap"><code class="lang-python">import time
import requests

base_url = "https://api.aimlapi.com/v1"
# Insert your AIML API Key instead of &#x3C;YOUR_AIMLAPI_KEY>:
api_key = "&#x3C;YOUR_AIMLAPI_KEY>"

<strong># Creating and sending a speech-to-text conversion task to the server
</strong>def create_stt():
    url = f"{base_url}/stt/create"
    headers = {
        "Authorization": f"Bearer {api_key}", 
    }

    data = {
        "model": "#g1_nova-2-meeting",
        "url": "https://audio-samples.github.io/samples/mp3/blizzard_primed/sample-0.mp3"
    }
 
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code >= 400:
        print(f"Error: {response.status_code} - {response.text}")
    else:
        response_data = response.json()
        print(response_data)
        return response_data

# Requesting the result of the task from the server using the generation_id
def get_stt(gen_id):
    url = f"{base_url}/stt/{gen_id}"
    headers = {
        "Authorization": f"Bearer {api_key}", 
    }
    response = requests.get(url, headers=headers)
    return response.json()
    
# First, start the generation, then repeatedly request the result from the server every 10 seconds.
def main():
    stt_response = create_stt()
    gen_id = stt_response.get("generation_id")



    if gen_id:
        start_time = time.time()

        timeout = 600
        while time.time() - start_time &#x3C; timeout:
            response_data = get_stt(gen_id)

            if response_data is None:
                print("Error: No response from API")
                break
        
            status = response_data.get("status")

            if status == "waiting" or status == "active":
                print("Still waiting... Checking again in 10 seconds.")
                time.sleep(10)
            else:
                print("Processing complete:/n", response_data["result"]['results']["channels"][0]["alternatives"][0]["transcript"])
                return response_data
   
        print("Timeout reached. Stopping.")
        return None     


if __name__ == "__main__":
    main()

</code></pre>

<details>

<summary>Response</summary>

{% code overflow="wrap" %}

```
{'generation_id': 'h66460ba-0562-1dd9-b440-a56d947e72a3'}
Processing complete:
 He doesn't belong to you and i don't see how you have anything to do with what is be his power yet he's he persona from this stage to you be fine
```

{% endcode %}

</details>

### Example #2: Processing a Speech Audio File via File Path

{% code overflow="wrap" %}

```python
import time
import requests

base_url = "https://api.aimlapi.com/v1"
# Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
api_key = "<YOUR_AIMLAPI_KEY>"

# Creating and sending a speech-to-text conversion task to the server
def create_stt():
    url = f"{base_url}/stt/create"
    headers = {
        "Authorization": f"Bearer {api_key}", 
    }

    data = {
        "model": "#g1_nova-2-meeting",
    }
    with open("stt-sample.mp3", "rb") as file:
        files = {"audio": ("sample.mp3", file, "audio/mpeg")}
        response = requests.post(url, data=data, headers=headers, files=files)
    
    if response.status_code >= 400:
        print(f"Error: {response.status_code} - {response.text}")
    else:
        response_data = response.json()
        print(response_data)
        return response_data

# Requesting the result of the task from the server using the generation_id
def get_stt(gen_id):
    url = f"{base_url}/stt/{gen_id}"
    headers = {
        "Authorization": f"Bearer {api_key}", 
    }
    response = requests.get(url, headers=headers)
    return response.json()
    
# First, start the generation, then repeatedly request the result from the server every 10 seconds.
def main():
    stt_response = create_stt()
    gen_id = stt_response.get("generation_id")


    if gen_id:
        start_time = time.time()

        timeout = 600
        while time.time() - start_time < timeout:
            response_data = get_stt(gen_id)

            if response_data is None:
                print("Error: No response from API")
                break
        
            status = response_data.get("status")

            if status == "waiting" or status == "active":
                print("Still waiting... Checking again in 10 seconds.")
                time.sleep(10)
            else:
                print("Processing complete:/n", response_data["result"]['results']["channels"][0]["alternatives"][0]["transcript"])
                return response_data
   
        print("Timeout reached. Stopping.")
        return None     


if __name__ == "__main__":
    main()

```

{% endcode %}

<details>

<summary>Response</summary>

{% code overflow="wrap" %}

```
{'generation_id': 'd793a81c-f8d8-40e0-a7c6-049ec6f54446'}
Processing complete:
 He doesn't belong to you, and I don't see how you have anything to do with what is be his power yet. He's he pursuing that from this stage to you.
```

{% endcode %}

</details>

## API Schema

#### Creating and sending a speech-to-text conversion task to the server

## POST /v1/stt/create

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Voice.v1.SpeechToTextCreateResponseDTO":{"type":"object","properties":{"generation_id":{"type":"string","format":"uuid"}},"required":["generation_id"]}}},"paths":{"/v1/stt/create":{"post":{"operationId":"VoiceModelsController_createSpeechToText_v1","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"enum":["#g1_nova-2-automotive","#g1_nova-2-conversationalai","#g1_nova-2-drivethru","#g1_nova-2-finance","#g1_nova-2-general","#g1_nova-2-medical","#g1_nova-2-meeting","#g1_nova-2-phonecall","#g1_nova-2-video","#g1_nova-2-voicemail"]},"custom_intent":{"anyOf":[{"type":"string"},{"type":"array","items":{"type":"string"}}],"description":"A custom intent you want the model to detect within your input audio if present. Submit up to 100."},"custom_topic":{"anyOf":[{"type":"string"},{"type":"array","items":{"type":"string"}}],"description":"A custom topic you want the model to detect within your input audio if present. Submit up to 100."},"custom_intent_mode":{"type":"string","enum":["strict","extended"],"description":"Sets how the model will interpret strings submitted to the custom_intent param. When strict, the model will only return intents submitted using the custom_intent param. When extended, the model will return its own detected intents in addition those submitted using the custom_intents param."},"custom_topic_mode":{"type":"string","enum":["strict","extended"],"description":"Sets how the model will interpret strings submitted to the custom_topic param. When strict, the model will only return topics submitted using the custom_topic param. When extended, the model will return its own detected topics in addition to those submitted using the custom_topic param."},"detect_language":{"type":"boolean","description":"Enables language detection to identify the dominant language spoken in the submitted audio."},"detect_entities":{"type":"boolean","description":"When Entity Detection is enabled, the Punctuation feature will be enabled by default."},"detect_topics":{"type":"boolean","description":"Detects the most important and relevant topics that are referenced in speech within the audio."},"diarize":{"type":"boolean","description":"Recognizes speaker changes. Each word in the transcript will be assigned a speaker number starting at 0."},"dictation":{"type":"boolean","description":"Identifies and extracts key entities from content in submitted audio."},"diarize_version":{"type":"string","description":""},"extra":{"type":"string","description":"Arbitrary key-value pairs that are attached to the API response for usage in downstream processing."},"filler_words":{"type":"boolean","description":"Filler Words can help transcribe interruptions in your audio, like “uh” and “um”."},"intents":{"type":"boolean","description":"Recognizes speaker intent throughout a transcript or text."},"keywords":{"type":"string","description":"Keywords can boost or suppress specialized terminology and brands."},"language":{"type":"string","description":"The BCP-47 language tag that hints at the primary spoken language. Depending on the Model and API endpoint you choose only certain languages are available"},"measurements":{"type":"boolean","description":"Spoken measurements will be converted to their corresponding abbreviations"},"multi_channel":{"type":"boolean","description":"Transcribes each audio channel independently"},"numerals":{"type":"boolean","description":"Numerals converts numbers from written format to numerical format"},"paragraphs":{"type":"boolean","description":"Splits audio into paragraphs to improve transcript readability"},"profanity_filter":{"type":"boolean","description":"Profanity Filter looks for recognized profanity and converts it to the nearest recognized non-profane word or removes it from the transcript completely"},"punctuate":{"type":"boolean","description":"Adds punctuation and capitalization to the transcript"},"search":{"type":"string","description":"Search for terms or phrases in submitted audio"},"sentiment":{"type":"boolean","description":"Recognizes the sentiment throughout a transcript or text"},"smart_format":{"type":"boolean","description":"Applies formatting to transcript output. When set to true, additional formatting will be applied to transcripts to improve readability"},"summarize":{"type":"string","description":"Summarizes content. For Listen API, supports string version option. For Read API, accepts boolean only."},"tag":{"type":"array","items":{"type":"string"},"description":"Labels your requests for the purpose of identification during usage reporting"},"topics":{"type":"boolean","description":"Detects topics throughout a transcript or text"},"utterances":{"type":"boolean","description":"Segments speech into meaningful semantic units"},"utt_split":{"type":"number","description":"Seconds to wait before detecting a pause between words in submitted audio"}},"required":["model"]}}}},"responses":{"201":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Voice.v1.SpeechToTextCreateResponseDTO"}}}}},"tags":["Voice Models"]}}}}
```

#### Requesting the result of the task from the server using the generation\_id

## GET /v1/stt/{generation\_id}

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Voice.v1.SpeechToTextGetResponseDTO":{"type":"object","properties":{"status":{"type":"string"},"result":{"type":"object","properties":{"metadata":{"type":"object","properties":{"transaction_key":{"type":"string","description":"A unique transaction key; currently always “deprecated”."},"request_id":{"type":"string","description":"A UUID identifying this specific transcription request."},"sha256":{"type":"string","description":"The SHA-256 hash of the submitted audio file (for pre-recorded requests)."},"created":{"type":"string","format":"date-time","description":"ISO-8601 timestamp."},"duration":{"type":"number","description":"Length of the audio in seconds."},"channels":{"type":"number","description":"The top-level results object containing per-channel transcription alternatives."},"models":{"type":"array","items":{"type":"string"},"description":"List of model UUIDs used for this transcription"},"model_info":{"type":"object","additionalProperties":{"type":"object","properties":{"name":{"type":"string","description":"The human-readable name of the model — identifies which model was used."},"version":{"type":"string","description":"The specific version of the model."},"arch":{"type":"string","description":"The architecture of the model — describes the model family / generation."}},"required":["name","version","arch"]},"description":"Mapping from each model UUID (in 'models') to detailed info: its name, version, and architecture."}},"required":["transaction_key","request_id","sha256","created","duration","channels","models","model_info"],"description":"Metadata about the transcription response, including timing, models, and IDs."},"results":{"type":"object","nullable":true,"properties":{"channels":{"type":"object","properties":{"alternatives":{"type":"array","items":{"type":"object","properties":{"transcript":{"type":"string","description":"The full transcript text for this alternative."},"confidence":{"type":"number","description":"Overall confidence score (0-1) that assigns to this transcript alternative."},"words":{"type":"array","items":{"type":"object","properties":{"word":{"type":"string","description":"The raw recognized word, without punctuation or capitalization."},"start":{"type":"number","description":"Start timestamp of the word (in seconds, from beginning of audio)."},"end":{"type":"number","description":"End timestamp of the word (in seconds)."},"confidence":{"type":"number","description":"Confidence score (0-1) for this individual word."},"punctuated_word":{"type":"string","description":"The same word but with punctuation/capitalization applied (if smart_format is enabled)."}},"required":["word","start","end","confidence","punctuated_word"]},"description":"List of word-level timing, confidence, and punctuation details."},"paragraphs":{"type":"array","items":{"type":"object","properties":{"transcript":{"type":"string","description":"The transcript split into paragraphs (with line breaks), when paragraphing is enabled."},"paragraphs":{"type":"object","properties":{"sentences":{"type":"array","items":{"type":"object","properties":{"text":{"type":"string","description":"Text of a single sentence in the paragraph."},"start":{"type":"number","description":"Start time of the sentence (in seconds)."},"end":{"type":"number","description":"End time of the sentence (in seconds)."}},"required":["text","start","end"]},"description":"List of sentences in this paragraph, with start/end times."},"num_words":{"type":"number","description":"Number of words in this paragraph."},"start":{"type":"number","description":"Start time of the paragraph (in seconds)."},"end":{"type":"number","description":"End time of the paragraph (in seconds)."}},"required":["sentences","num_words","start","end"],"description":"Structure describing each paragraph: its timespan, word count, and sentence breakdown."}},"required":["transcript","paragraphs"]},"description":"An array of paragraph objects, present when the paragraphs feature is enabled."}},"required":["transcript","confidence","words","paragraphs"]},"description":"List of possible transcription hypotheses (“alternatives”) for each channel."}},"required":["alternatives"],"description":"The top-level results object containing per-channel transcription alternatives."}},"required":["channels"]}},"required":["metadata"],"additionalProperties":false}},"required":["status"]}}},"paths":{"/v1/stt/{generation_id}":{"get":{"operationId":"VoiceModelsController_getSTT_v1","parameters":[{"name":"generation_id","required":true,"in":"path","schema":{"type":"string"}}],"responses":{"201":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Voice.v1.SpeechToTextGetResponseDTO"}}}}},"tags":["Voice Models"]}}}}
```
