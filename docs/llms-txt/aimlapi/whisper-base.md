# Source: https://docs.aimlapi.com/api-references/speech-models/speech-to-text/openai/whisper-base.md

# whisper-base

{% hint style="info" %}
This documentation is valid for the following list of our models:

* `#g1_whisper-base`
  {% endhint %}

{% hint style="success" %}
Note:

Previously, our STT models operated via a single API call to POST `https://api.aimlapi.com/v1/stt`. You can view the API schema [here](https://docs.aimlapi.com/api-references/speech-models/speech-to-text/stt-legacy).

Now, we are switching to a new two-step process:

* `POST https://api.aimlapi.com/v1/stt/create` – Creates and submits a speech-to-text processing task to the server. This method accepts the same parameters as the old version but returns a `generation_id` instead of the final transcript.
* `GET https://api.aimlapi.com/v1/stt/{generation_id}` – Retrieves the generated transcript from the server using the `generation_id` obtained from the previous API call.

This approach helps prevent generation failures due to timeouts.\
We've prepared [a couple of examples](#quick-code-examples) below to make the transition to the new STT API easier for you.
{% endhint %}

## Model Overview

The Whisper models are primarily for AI research, focusing on model robustness, generalization, and biases, and are also effective for English speech recognition. The use of Whisper models for transcribing non-consensual recordings or in high-risk decision-making contexts is strongly discouraged due to potential inaccuracies and ethical concerns.

The models are trained using 680,000 hours of audio and corresponding transcripts from the internet, with 65% being English audio and transcripts, 18% non-English audio with English transcripts, and 17% non-English audio with matching non-English transcripts, covering 98 languages in total.

{% hint style="success" %}
OpenAI STT models are priced based on tokens, similar to chat models. In practice, this means the cost primarily depends on the duration of the input audio.
{% endhint %}

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schemas

#### Creating and sending a speech-to-text conversion task to the server

## POST /v1/stt/create

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Voice.v1.SpeechToTextCreateResponseDTO":{"type":"object","properties":{"generation_id":{"type":"string","format":"uuid"}},"required":["generation_id"]}}},"paths":{"/v1/stt/create":{"post":{"operationId":"VoiceModelsController_createSpeechToText_v1","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"enum":["#g1_whisper-base"]},"custom_intent":{"anyOf":[{"type":"string"},{"type":"array","items":{"type":"string"}}],"description":"A custom intent you want the model to detect within your input audio if present. Submit up to 100."},"custom_topic":{"anyOf":[{"type":"string"},{"type":"array","items":{"type":"string"}}],"description":"A custom topic you want the model to detect within your input audio if present. Submit up to 100."},"custom_intent_mode":{"type":"string","enum":["strict","extended"],"description":"Sets how the model will interpret strings submitted to the custom_intent param. When strict, the model will only return intents submitted using the custom_intent param. When extended, the model will return its own detected intents in addition those submitted using the custom_intents param."},"custom_topic_mode":{"type":"string","enum":["strict","extended"],"description":"Sets how the model will interpret strings submitted to the custom_topic param. When strict, the model will only return topics submitted using the custom_topic param. When extended, the model will return its own detected topics in addition to those submitted using the custom_topic param."},"detect_language":{"type":"boolean","description":"Enables language detection to identify the dominant language spoken in the submitted audio."},"detect_entities":{"type":"boolean","description":"When Entity Detection is enabled, the Punctuation feature will be enabled by default."},"detect_topics":{"type":"boolean","description":"Detects the most important and relevant topics that are referenced in speech within the audio."},"diarize":{"type":"boolean","description":"Recognizes speaker changes. Each word in the transcript will be assigned a speaker number starting at 0."},"dictation":{"type":"boolean","description":"Identifies and extracts key entities from content in submitted audio."},"diarize_version":{"type":"string","description":""},"extra":{"type":"string","description":"Arbitrary key-value pairs that are attached to the API response for usage in downstream processing."},"filler_words":{"type":"boolean","description":"Filler Words can help transcribe interruptions in your audio, like “uh” and “um”."},"intents":{"type":"boolean","description":"Recognizes speaker intent throughout a transcript or text."},"keywords":{"type":"string","description":"Keywords can boost or suppress specialized terminology and brands."},"language":{"type":"string","description":"The BCP-47 language tag that hints at the primary spoken language. Depending on the Model and API endpoint you choose only certain languages are available"},"measurements":{"type":"boolean","description":"Spoken measurements will be converted to their corresponding abbreviations"},"multi_channel":{"type":"boolean","description":"Transcribes each audio channel independently"},"numerals":{"type":"boolean","description":"Numerals converts numbers from written format to numerical format"},"paragraphs":{"type":"boolean","description":"Splits audio into paragraphs to improve transcript readability"},"profanity_filter":{"type":"boolean","description":"Profanity Filter looks for recognized profanity and converts it to the nearest recognized non-profane word or removes it from the transcript completely"},"punctuate":{"type":"boolean","description":"Adds punctuation and capitalization to the transcript"},"search":{"type":"string","description":"Search for terms or phrases in submitted audio"},"sentiment":{"type":"boolean","description":"Recognizes the sentiment throughout a transcript or text"},"smart_format":{"type":"boolean","description":"Applies formatting to transcript output. When set to true, additional formatting will be applied to transcripts to improve readability"},"summarize":{"type":"string","description":"Summarizes content. For Listen API, supports string version option. For Read API, accepts boolean only."},"tag":{"type":"array","items":{"type":"string"},"description":"Labels your requests for the purpose of identification during usage reporting"},"topics":{"type":"boolean","description":"Detects topics throughout a transcript or text"},"utterances":{"type":"boolean","description":"Segments speech into meaningful semantic units"},"utt_split":{"type":"number","description":"Seconds to wait before detecting a pause between words in submitted audio"},"url":{"type":"string","format":"uri"}},"required":["model","url"]}}}},"responses":{"201":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Voice.v1.SpeechToTextCreateResponseDTO"}}}}},"tags":["Voice Models"]}}}}
```

#### Requesting the result of the task from the server using the generation\_id

## GET /v1/stt/{generation\_id}

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Voice.v1.SpeechToTextGetResponseDTO":{"type":"object","properties":{"generation_id":{"type":"string"},"status":{"type":"string","enum":["queued","completed","error","generating"]},"result":{"anyOf":[{"type":"object","properties":{"metadata":{"type":"object","properties":{"transaction_key":{"type":"string","description":"A unique transaction key; currently always “deprecated”."},"request_id":{"type":"string","description":"A UUID identifying this specific transcription request."},"sha256":{"type":"string","description":"The SHA-256 hash of the submitted audio file (for pre-recorded requests)."},"created":{"type":"string","format":"date-time","description":"ISO-8601 timestamp."},"duration":{"type":"number","description":"Length of the audio in seconds."},"channels":{"type":"number","description":"The top-level results object containing per-channel transcription alternatives."},"models":{"type":"array","items":{"type":"string"},"description":"List of model UUIDs used for this transcription"},"model_info":{"type":"object","additionalProperties":{"type":"object","properties":{"name":{"type":"string","description":"The human-readable name of the model — identifies which model was used."},"version":{"type":"string","description":"The specific version of the model."},"arch":{"type":"string","description":"The architecture of the model — describes the model family / generation."}},"required":["name","version","arch"]},"description":"Mapping from each model UUID (in 'models') to detailed info: its name, version, and architecture."}},"required":["transaction_key","request_id","sha256","created","duration","channels","models","model_info"],"description":"Metadata about the transcription response, including timing, models, and IDs."},"results":{"type":"object","nullable":true,"properties":{"channels":{"type":"object","properties":{"alternatives":{"type":"array","items":{"type":"object","properties":{"transcript":{"type":"string","description":"The full transcript text for this alternative."},"confidence":{"type":"number","description":"Overall confidence score (0-1) that assigns to this transcript alternative."},"words":{"type":"array","items":{"type":"object","properties":{"word":{"type":"string","description":"The raw recognized word, without punctuation or capitalization."},"start":{"type":"number","description":"Start timestamp of the word (in seconds, from beginning of audio)."},"end":{"type":"number","description":"End timestamp of the word (in seconds)."},"confidence":{"type":"number","description":"Confidence score (0-1) for this individual word."},"punctuated_word":{"type":"string","description":"The same word but with punctuation/capitalization applied (if smart_format is enabled)."}},"required":["word","start","end","confidence","punctuated_word"]},"description":"List of word-level timing, confidence, and punctuation details."},"paragraphs":{"type":"array","items":{"type":"object","properties":{"transcript":{"type":"string","description":"The transcript split into paragraphs (with line breaks), when paragraphing is enabled."},"paragraphs":{"type":"object","properties":{"sentences":{"type":"array","items":{"type":"object","properties":{"text":{"type":"string","description":"Text of a single sentence in the paragraph."},"start":{"type":"number","description":"Start time of the sentence (in seconds)."},"end":{"type":"number","description":"End time of the sentence (in seconds)."}},"required":["text","start","end"]},"description":"List of sentences in this paragraph, with start/end times."},"num_words":{"type":"number","description":"Number of words in this paragraph."},"start":{"type":"number","description":"Start time of the paragraph (in seconds)."},"end":{"type":"number","description":"End time of the paragraph (in seconds)."}},"required":["sentences","num_words","start","end"],"description":"Structure describing each paragraph: its timespan, word count, and sentence breakdown."}},"required":["transcript","paragraphs"]},"description":"An array of paragraph objects, present when the paragraphs feature is enabled."}},"required":["transcript","confidence","words","paragraphs"]},"description":"List of possible transcription hypotheses (“alternatives”) for each channel."}},"required":["alternatives"],"description":"The top-level results object containing per-channel transcription alternatives."}},"required":["channels"]}},"required":["metadata"]},{"type":"object","properties":{"id":{"type":"string","format":"uuid"},"language_model":{"type":"string"},"acoustic_model":{"type":"string"},"language_code":{"type":"string"},"status":{"type":"string","enum":["queued","processing","completed","error"]},"language_detection":{"type":"boolean"},"language_confidence_threshold":{"type":"number"},"language_confidence":{"type":"number"},"speech_model":{"type":"string","enum":["best","slam-1","universal"]},"text":{"type":"string"},"words":{"type":"array","items":{"type":"object","properties":{"confidence":{"type":"number"},"end":{"type":"number"},"speaker":{"type":"string"},"start":{"type":"number"},"text":{"type":"string"}},"required":["confidence","end","start","text"]}},"utterances":{"type":"array","items":{"type":"object","properties":{"confidence":{"type":"number"},"end":{"type":"number"},"speaker":{"type":"string"},"start":{"type":"number"},"text":{"type":"string"},"words":{"type":"array","items":{"type":"object","properties":{"confidence":{"type":"number"},"end":{"type":"number"},"speaker":{"type":"string"},"start":{"type":"number"},"text":{"type":"string"}},"required":["confidence","end","start","text"]}}},"required":["confidence","end","speaker","start","text","words"]}},"confidence":{"type":"number"},"audio_duration":{"type":"number"},"punctuate":{"type":"boolean"},"format_text":{"type":"boolean"},"disfluencies":{"type":"boolean"},"multichannel":{"type":"boolean"},"webhook_url":{"type":"string"},"webhook_status_code":{"type":"number"},"webhook_auth_header_name":{"type":"string"},"speed_boost":{"type":"boolean"},"auto_highlights_result":{"type":"object","properties":{"status":{"type":"string"},"results":{"type":"array","items":{"type":"object","properties":{"count":{"type":"number"},"rank":{"type":"number"},"text":{"type":"string"},"timestamps":{"type":"array","items":{"type":"object","properties":{"start":{"type":"number"},"end":{"type":"number"}},"required":["start","end"]}}},"required":["count","rank","text","timestamps"]}}},"required":["status","results"]},"auto_highlights":{"type":"boolean"},"audio_start_from":{"type":"number"},"audio_end_at":{"type":"number"},"word_boost":{"type":"array","items":{"type":"string"}},"boost_param":{"type":"string"},"filter_profanity":{"type":"boolean"},"redact_pii":{"type":"boolean"},"redact_pii_audio":{"type":"boolean"},"redact_pii_audio_quality":{"type":"string","enum":["mp3","wav"]},"redact_pii_policies":{"type":"array","items":{"type":"string"}},"redact_pii_sub":{"type":"string","enum":["entity_name","hash"]},"speaker_labels":{"type":"boolean"},"speakers_expected":{"type":"number"},"content_safety":{"type":"boolean"},"iab_categories":{"type":"boolean"},"content_safety_labels":{"type":"object","properties":{"status":{"type":"string"},"results":{"type":"array","items":{"type":"object","properties":{"text":{"type":"string"},"labels":{"type":"array","items":{"type":"object","properties":{"label":{"type":"string"},"confidence":{"type":"number"},"severity":{"type":"number"}},"required":["label","confidence","severity"]}},"sentences_idx_start":{"type":"number"},"sentences_idx_end":{"type":"number"},"timestamp":{"type":"object","properties":{"start":{"type":"number"},"end":{"type":"number"}},"required":["start","end"]}},"required":["text","labels","sentences_idx_start","sentences_idx_end","timestamp"]}},"summary":{"type":"object","additionalProperties":{"type":"number"}}},"required":["status","results","summary"]},"iab_categories_result":{"type":"object","properties":{"status":{"type":"string"},"results":{"type":"array","items":{"type":"object","properties":{"text":{"type":"string"},"labels":{"type":"array","items":{"type":"object","properties":{"relevance":{"type":"number"},"label":{"type":"string"}},"required":["relevance","label"]}},"timestamp":{"type":"object","properties":{"start":{"type":"number"},"end":{"type":"number"}},"required":["start","end"]}},"required":["text","labels","timestamp"]}},"summary":{"type":"object","additionalProperties":{"type":"number"}}},"required":["status","results","summary"]},"custom_spelling":{"type":"array","items":{"type":"object","properties":{"from":{"type":"string"},"to":{"type":"string"}},"required":["from","to"]}},"chapters":{"type":"array","items":{"type":"object","properties":{"summary":{"type":"string"},"headline":{"type":"string"},"gist":{"type":"string"},"start":{"type":"number"},"end":{"type":"number"}},"required":["summary","headline","gist","start","end"]}},"summarization":{"type":"boolean"},"summary_type":{"type":"string"},"summary_model":{"type":"string"},"summary":{"type":"string"},"auto_chapters":{"type":"boolean"},"sentiment_analysis":{"type":"boolean"},"sentiment_analysis_results":{"type":"array","items":{"type":"object","properties":{"text":{"type":"string"},"start":{"type":"number"},"end":{"type":"number"},"sentiment":{"type":"string","enum":["POSITIVE","NEUTRAL","NEGATIVE"]},"confidence":{"type":"number"},"speaker":{"type":"string"}},"required":["text","start","end","sentiment","confidence"]}},"entity_detection":{"type":"boolean"},"entities":{"type":"array","items":{"type":"object","properties":{"entity_type":{"type":"string"},"text":{"type":"string"},"start":{"type":"number"},"end":{"type":"number"}},"required":["entity_type","text","start","end"]}},"speech_threshold":{"type":"number"},"throttled":{"type":"boolean"},"error":{"type":"string"}},"required":["id","status"],"additionalProperties":false},{"type":"object","properties":{"text":{"type":"string"},"usage":{"type":"object","properties":{"type":{"type":"string","enum":["tokens"]},"input_tokens":{"type":"number"},"input_token_details":{"type":"object","properties":{"text_tokens":{"type":"number"},"audio_tokens":{"type":"number"}},"required":["text_tokens","audio_tokens"]},"output_tokens":{"type":"number"},"total_tokens":{"type":"number"}},"required":["input_tokens","output_tokens","total_tokens"]}},"required":["text"],"additionalProperties":false},{"nullable":true}]},"error":{"nullable":true}},"required":["generation_id","status"]}}},"paths":{"/v1/stt/{generation_id}":{"get":{"operationId":"VoiceModelsController_getSTT_v1","parameters":[{"name":"generation_id","required":true,"in":"path","schema":{"type":"string"}}],"responses":{"201":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Voice.v1.SpeechToTextGetResponseDTO"}}}}},"tags":["Voice Models"]}}}}
```

## Quick Code Examples

Let's use the `#g1_whisper-base` model to transcribe the following audio fragment:

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
        "model": "#g1_whisper-base",
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
                print("Processing complete:\n", response_data["result"]['results']["channels"][0]["alternatives"][0]["transcript"])
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
        "model": "#g1_whisper-base",
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
                print("Processing complete:\n", response_data["result"]['results']["channels"][0]["alternatives"][0]["transcript"])
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
{'generation_id': 'e3d46bba-7562-44a9-b440-504d940342a3'}
Processing complete:
 He doesn't belong to you and i don't see how you have anything to do with what is be his power yet he's he persona from this stage to you be fine
```

{% endcode %}

</details>
