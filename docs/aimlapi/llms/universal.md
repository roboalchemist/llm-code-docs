# Source: https://docs.aimlapi.com/api-references/speech-models/speech-to-text/assembly-ai/universal.md

# universal

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `aai/universal`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/aai/universal" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

A new Speech-to-Text model offering exceptional accuracy by leveraging its deep understanding of context and semantics, with the broadest language support.

{% hint style="success" %}
This model use per-second billing. The cost of audio transcription is based on the number of seconds in the input audio file, not the processing time.
{% endhint %}

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

#### Creating and sending a speech-to-text conversion task to the server

## POST /v1/stt/create

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Voice.v1.SpeechToTextCreateResponseDTO":{"type":"object","properties":{"generation_id":{"type":"string","format":"uuid"}},"required":["generation_id"]}}},"paths":{"/v1/stt/create":{"post":{"operationId":"VoiceModelsController_createSpeechToText_v1","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"enum":["aai/universal"]},"audio":{"type":"object","properties":{"buffer":{"nullable":true},"mimetype":{"type":"string"},"size":{"type":"integer"},"originalname":{"type":"string"},"encoding":{"type":"string"},"fieldname":{"type":"string"}},"required":["mimetype","originalname","encoding","fieldname"],"description":"The audio file to transcribe."},"audio_start_from":{"type":"integer","description":"The point in time, in milliseconds, in the file at which the transcription was started."},"audio_end_at":{"type":"integer","description":"The point in time, in milliseconds, in the file at which the transcription was terminated."},"language_code":{"type":"string","description":"The language of your audio file. Possible values are found in Supported Languages. The default value is 'en_us'."},"language_confidence_threshold":{"type":"number","minimum":0,"maximum":1,"description":"The confidence threshold for the automatically detected language. An error will be returned if the language confidence is below this threshold. Defaults to 0."},"language_detection":{"type":"boolean","description":"Enable Automatic language detection, either true or false. Available for universal model only."},"punctuate":{"type":"boolean","nullable":true,"default":null,"description":"Adds punctuation and capitalization to the transcript"},"format_text":{"type":"boolean","default":true,"description":"Enable Text Formatting, can be true or false."},"disfluencies":{"type":"boolean","default":false,"description":"Transcribe Filler Words, like \"umm\", in your media file; can be true or false."},"multichannel":{"type":"boolean","default":false,"description":"Enable Multichannel transcription, can be true or false."},"speaker_labels":{"type":"boolean","nullable":true,"default":null,"description":"Enable Speaker diarization, can be true or false."},"speakers_expected":{"type":"integer","nullable":true,"default":null,"description":"Tell the speaker label model how many speakers it should attempt to identify. See Speaker diarization for more details."},"content_safety":{"type":"boolean","default":false,"description":"Enable Content Moderation, can be true or false."},"iab_categories":{"type":"boolean","default":false,"description":"Enable Topic Detection, can be true or false."},"custom_spelling":{"type":"array","items":{"type":"object","properties":{"from":{"type":"string"},"to":{"type":"string"}},"required":["from","to"]},"description":"Customize how words are spelled and formatted using to and from values."},"auto_highlights":{"type":"boolean","default":false,"description":"Enable Key Phrases, either true or false."},"word_boost":{"type":"array","items":{"type":"string"},"description":"The list of custom vocabulary to boost transcription probability for."},"boost_param":{"type":"string","enum":["low","default","high"],"description":"How much to boost specified words. Allowed values: low, default, high."},"filter_profanity":{"type":"boolean","default":false,"description":"Filter profanity from the transcribed text, can be true or false."},"redact_pii":{"type":"boolean","default":false,"description":"Redact PII from the transcribed text using the Redact PII model, can be true or false."},"redact_pii_audio":{"type":"boolean","default":false,"description":"Generate a copy of the original media file with spoken PII \"beeped\" out, can be true or false. See PII redaction for more details."},"redact_pii_audio_quality":{"type":"string","enum":["mp3","wav"],"description":"Controls the filetype of the audio created by redact_pii_audio. Currently supports mp3 (default) and wav. See PII redaction for more details."},"redact_pii_policies":{"type":"array","items":{"type":"string","enum":["account_number","banking_information","blood_type","credit_card_cvv","credit_card_expiration","credit_card_number","date","date_interval","date_of_birth","drivers_license","drug","duration","email_address","event","filename","gender_sexuality","healthcare_number","injury","ip_address","language","location","marital_status","medical_condition","medical_process","money_amount","nationality","number_sequence","occupation","organization","passport_number","password","person_age","person_name","phone_number","physical_attribute","political_affiliation","religion","statistics","time","url","us_social_security_number","username","vehicle_id","zodiac_sign"]},"description":"The list of PII Redaction policies to enable. See PII redaction for more details."},"redact_pii_sub":{"type":"string","enum":["entity_name","hash"],"description":"The replacement logic for detected PII, can be `entity_type` or `hash`. See PII redaction for more details."},"sentiment_analysis":{"type":"boolean","default":false,"description":"Enable Sentiment Analysis, can be true or false."},"entity_detection":{"type":"boolean","default":false,"description":"Enable Entity Detection, can be true or false."},"summarization":{"type":"boolean","default":false,"description":"Enable Summarization, can be true or false."},"summary_model":{"type":"string","enum":["informative","conversational","catchy"],"description":"The model to summarize the transcript. Allowed values: informative, conversational, catchy."},"summary_type":{"type":"string","enum":["bullets","bullets_verbose","gist","headline","paragraph"],"description":"The type of summary. Allowed values: bullets, bullets_verbose, gist, headline, paragraph."},"auto_chapters":{"type":"boolean","default":false,"description":"Enable Auto Chapters, either true or false."},"speech_threshold":{"type":"number","minimum":0,"maximum":1,"description":"Reject audio files that contain less than this fraction of speech. Valid values are in the range [0, 1] inclusive."}},"required":["model","audio"]}}}},"responses":{"201":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Voice.v1.SpeechToTextCreateResponseDTO"}}}}},"tags":["Voice Models"]}}}}
```

#### Requesting the result of the task from the server using the generation\_id

## GET /v1/stt/{generation\_id}

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Voice.v1.SpeechToTextGetResponseDTO":{"type":"object","properties":{"generation_id":{"type":"string"},"status":{"type":"string","enum":["queued","completed","error","generating"]},"result":{"anyOf":[{"type":"object","properties":{"metadata":{"type":"object","properties":{"transaction_key":{"type":"string","description":"A unique transaction key; currently always “deprecated”."},"request_id":{"type":"string","description":"A UUID identifying this specific transcription request."},"sha256":{"type":"string","description":"The SHA-256 hash of the submitted audio file (for pre-recorded requests)."},"created":{"type":"string","format":"date-time","description":"ISO-8601 timestamp."},"duration":{"type":"number","description":"Length of the audio in seconds."},"channels":{"type":"number","description":"The top-level results object containing per-channel transcription alternatives."},"models":{"type":"array","items":{"type":"string"},"description":"List of model UUIDs used for this transcription"},"model_info":{"type":"object","additionalProperties":{"type":"object","properties":{"name":{"type":"string","description":"The human-readable name of the model — identifies which model was used."},"version":{"type":"string","description":"The specific version of the model."},"arch":{"type":"string","description":"The architecture of the model — describes the model family / generation."}},"required":["name","version","arch"]},"description":"Mapping from each model UUID (in 'models') to detailed info: its name, version, and architecture."}},"required":["transaction_key","request_id","sha256","created","duration","channels","models","model_info"],"description":"Metadata about the transcription response, including timing, models, and IDs."},"results":{"type":"object","nullable":true,"properties":{"channels":{"type":"object","properties":{"alternatives":{"type":"array","items":{"type":"object","properties":{"transcript":{"type":"string","description":"The full transcript text for this alternative."},"confidence":{"type":"number","description":"Overall confidence score (0-1) that assigns to this transcript alternative."},"words":{"type":"array","items":{"type":"object","properties":{"word":{"type":"string","description":"The raw recognized word, without punctuation or capitalization."},"start":{"type":"number","description":"Start timestamp of the word (in seconds, from beginning of audio)."},"end":{"type":"number","description":"End timestamp of the word (in seconds)."},"confidence":{"type":"number","description":"Confidence score (0-1) for this individual word."},"punctuated_word":{"type":"string","description":"The same word but with punctuation/capitalization applied (if smart_format is enabled)."}},"required":["word","start","end","confidence","punctuated_word"]},"description":"List of word-level timing, confidence, and punctuation details."},"paragraphs":{"type":"array","items":{"type":"object","properties":{"transcript":{"type":"string","description":"The transcript split into paragraphs (with line breaks), when paragraphing is enabled."},"paragraphs":{"type":"object","properties":{"sentences":{"type":"array","items":{"type":"object","properties":{"text":{"type":"string","description":"Text of a single sentence in the paragraph."},"start":{"type":"number","description":"Start time of the sentence (in seconds)."},"end":{"type":"number","description":"End time of the sentence (in seconds)."}},"required":["text","start","end"]},"description":"List of sentences in this paragraph, with start/end times."},"num_words":{"type":"number","description":"Number of words in this paragraph."},"start":{"type":"number","description":"Start time of the paragraph (in seconds)."},"end":{"type":"number","description":"End time of the paragraph (in seconds)."}},"required":["sentences","num_words","start","end"],"description":"Structure describing each paragraph: its timespan, word count, and sentence breakdown."}},"required":["transcript","paragraphs"]},"description":"An array of paragraph objects, present when the paragraphs feature is enabled."}},"required":["transcript","confidence","words","paragraphs"]},"description":"List of possible transcription hypotheses (“alternatives”) for each channel."}},"required":["alternatives"],"description":"The top-level results object containing per-channel transcription alternatives."}},"required":["channels"]}},"required":["metadata"]},{"type":"object","properties":{"id":{"type":"string","format":"uuid"},"language_model":{"type":"string"},"acoustic_model":{"type":"string"},"language_code":{"type":"string"},"status":{"type":"string","enum":["queued","processing","completed","error"]},"language_detection":{"type":"boolean"},"language_confidence_threshold":{"type":"number"},"language_confidence":{"type":"number"},"speech_model":{"type":"string","enum":["best","slam-1","universal"]},"text":{"type":"string"},"words":{"type":"array","items":{"type":"object","properties":{"confidence":{"type":"number"},"end":{"type":"number"},"speaker":{"type":"string"},"start":{"type":"number"},"text":{"type":"string"}},"required":["confidence","end","start","text"]}},"utterances":{"type":"array","items":{"type":"object","properties":{"confidence":{"type":"number"},"end":{"type":"number"},"speaker":{"type":"string"},"start":{"type":"number"},"text":{"type":"string"},"words":{"type":"array","items":{"type":"object","properties":{"confidence":{"type":"number"},"end":{"type":"number"},"speaker":{"type":"string"},"start":{"type":"number"},"text":{"type":"string"}},"required":["confidence","end","start","text"]}}},"required":["confidence","end","speaker","start","text","words"]}},"confidence":{"type":"number"},"audio_duration":{"type":"number"},"punctuate":{"type":"boolean"},"format_text":{"type":"boolean"},"disfluencies":{"type":"boolean"},"multichannel":{"type":"boolean"},"webhook_url":{"type":"string"},"webhook_status_code":{"type":"number"},"webhook_auth_header_name":{"type":"string"},"speed_boost":{"type":"boolean"},"auto_highlights_result":{"type":"object","properties":{"status":{"type":"string"},"results":{"type":"array","items":{"type":"object","properties":{"count":{"type":"number"},"rank":{"type":"number"},"text":{"type":"string"},"timestamps":{"type":"array","items":{"type":"object","properties":{"start":{"type":"number"},"end":{"type":"number"}},"required":["start","end"]}}},"required":["count","rank","text","timestamps"]}}},"required":["status","results"]},"auto_highlights":{"type":"boolean"},"audio_start_from":{"type":"number"},"audio_end_at":{"type":"number"},"word_boost":{"type":"array","items":{"type":"string"}},"boost_param":{"type":"string"},"filter_profanity":{"type":"boolean"},"redact_pii":{"type":"boolean"},"redact_pii_audio":{"type":"boolean"},"redact_pii_audio_quality":{"type":"string","enum":["mp3","wav"]},"redact_pii_policies":{"type":"array","items":{"type":"string"}},"redact_pii_sub":{"type":"string","enum":["entity_name","hash"]},"speaker_labels":{"type":"boolean"},"speakers_expected":{"type":"number"},"content_safety":{"type":"boolean"},"iab_categories":{"type":"boolean"},"content_safety_labels":{"type":"object","properties":{"status":{"type":"string"},"results":{"type":"array","items":{"type":"object","properties":{"text":{"type":"string"},"labels":{"type":"array","items":{"type":"object","properties":{"label":{"type":"string"},"confidence":{"type":"number"},"severity":{"type":"number"}},"required":["label","confidence","severity"]}},"sentences_idx_start":{"type":"number"},"sentences_idx_end":{"type":"number"},"timestamp":{"type":"object","properties":{"start":{"type":"number"},"end":{"type":"number"}},"required":["start","end"]}},"required":["text","labels","sentences_idx_start","sentences_idx_end","timestamp"]}},"summary":{"type":"object","additionalProperties":{"type":"number"}}},"required":["status","results","summary"]},"iab_categories_result":{"type":"object","properties":{"status":{"type":"string"},"results":{"type":"array","items":{"type":"object","properties":{"text":{"type":"string"},"labels":{"type":"array","items":{"type":"object","properties":{"relevance":{"type":"number"},"label":{"type":"string"}},"required":["relevance","label"]}},"timestamp":{"type":"object","properties":{"start":{"type":"number"},"end":{"type":"number"}},"required":["start","end"]}},"required":["text","labels","timestamp"]}},"summary":{"type":"object","additionalProperties":{"type":"number"}}},"required":["status","results","summary"]},"custom_spelling":{"type":"array","items":{"type":"object","properties":{"from":{"type":"string"},"to":{"type":"string"}},"required":["from","to"]}},"chapters":{"type":"array","items":{"type":"object","properties":{"summary":{"type":"string"},"headline":{"type":"string"},"gist":{"type":"string"},"start":{"type":"number"},"end":{"type":"number"}},"required":["summary","headline","gist","start","end"]}},"summarization":{"type":"boolean"},"summary_type":{"type":"string"},"summary_model":{"type":"string"},"summary":{"type":"string"},"auto_chapters":{"type":"boolean"},"sentiment_analysis":{"type":"boolean"},"sentiment_analysis_results":{"type":"array","items":{"type":"object","properties":{"text":{"type":"string"},"start":{"type":"number"},"end":{"type":"number"},"sentiment":{"type":"string","enum":["POSITIVE","NEUTRAL","NEGATIVE"]},"confidence":{"type":"number"},"speaker":{"type":"string"}},"required":["text","start","end","sentiment","confidence"]}},"entity_detection":{"type":"boolean"},"entities":{"type":"array","items":{"type":"object","properties":{"entity_type":{"type":"string"},"text":{"type":"string"},"start":{"type":"number"},"end":{"type":"number"}},"required":["entity_type","text","start","end"]}},"speech_threshold":{"type":"number"},"throttled":{"type":"boolean"},"error":{"type":"string"}},"required":["id","status"],"additionalProperties":false},{"type":"object","properties":{"text":{"type":"string"},"usage":{"type":"object","properties":{"type":{"type":"string","enum":["tokens"]},"input_tokens":{"type":"number"},"input_token_details":{"type":"object","properties":{"text_tokens":{"type":"number"},"audio_tokens":{"type":"number"}},"required":["text_tokens","audio_tokens"]},"output_tokens":{"type":"number"},"total_tokens":{"type":"number"}},"required":["input_tokens","output_tokens","total_tokens"]}},"required":["text"],"additionalProperties":false},{"nullable":true}]},"error":{"nullable":true}},"required":["generation_id","status"]}}},"paths":{"/v1/stt/{generation_id}":{"get":{"operationId":"VoiceModelsController_getSTT_v1","parameters":[{"name":"generation_id","required":true,"in":"path","schema":{"type":"string"}}],"responses":{"201":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Voice.v1.SpeechToTextGetResponseDTO"}}}}},"tags":["Voice Models"]}}}}
```

## Quick Example: Processing a Speech Audio File via URL

Let's transcribe the following audio fragment:

{% embed url="<https://drive.google.com/file/d/1ZN-28NUbK1TXHt6oEPj42zUJCv82e9L4/view?usp=sharing>" %}

{% code overflow="wrap" %}

```python
import time
import requests
import json   # for getting a structured output with indentation

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
        "model": "aai/universal",
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
                
                print("Processing complete:\n", response_data["result"]["text"])
                
                # Uncomment the line below to print the entire "result" object with all service data
                # print("Processing complete:\n", json.dumps(response_data["result"], indent=2, ensure_ascii=False))
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

```json5
{'generation_id': '0cff4e24-c1ba-419d-8b62-46f342985881'}
Still waiting... Checking again in 10 seconds.
Processing complete:\n {
  "id": "04d07a4c-9238-4860-ac6f-534d58fdaf9a",
  "language_model": "assemblyai_default",
  "acoustic_model": "assemblyai_default",
  "language_code": "en_us",
  "status": "completed",
  "audio_url": "https://audio-samples.github.io/samples/mp3/blizzard_primed/sample-0.mp3",
  "text": "He doesn't belong to you. And I don't see how you have anything to do with what is be his power yet his he presumably that from this stage to you be fired.",
  "words": [
    {
      "text": "He",
      "start": 400,
      "end": 520,
      "confidence": 0.98876953,
      "speaker": null
    },
    {
      "text": "doesn't",
      "start": 520,
      "end": 880,
      "confidence": 0.9296875,
      "speaker": null
    },
    {
      "text": "belong",
      "start": 880,
      "end": 1320,
      "confidence": 1,
      "speaker": null
    },
    {
      "text": "to",
      "start": 1320,
      "end": 1560,
      "confidence": 0.99853516,
      "speaker": null
    },
    {
      "text": "you.",
      "start": 1560,
      "end": 1840,
      "confidence": 0.99853516,
      "speaker": null
    },
    {
      "text": "And",
      "start": 1840,
      "end": 2120,
      "confidence": 0.99365234,
      "speaker": null
    },
    {
      "text": "I",
      "start": 2120,
      "end": 2280,
      "confidence": 0.99902344,
      "speaker": null
    },
    {
      "text": "don't",
      "start": 2280,
      "end": 2520,
      "confidence": 0.9949544,
      "speaker": null
    },
    {
      "text": "see",
      "start": 2520,
      "end": 2720,
      "confidence": 0.99902344,
      "speaker": null
    },
    {
      "text": "how",
      "start": 2720,
      "end": 3000,
      "confidence": 0.99902344,
      "speaker": null
    },
    {
      "text": "you",
      "start": 3000,
      "end": 3320,
      "confidence": 0.99853516,
      "speaker": null
    },
    {
      "text": "have",
      "start": 3320,
      "end": 3600,
      "confidence": 0.99658203,
      "speaker": null
    },
    {
      "text": "anything",
      "start": 3600,
      "end": 4080,
      "confidence": 0.9968262,
      "speaker": null
    },
    {
      "text": "to",
      "start": 4080,
      "end": 4240,
      "confidence": 0.99902344,
      "speaker": null
    },
    {
      "text": "do",
      "start": 4240,
      "end": 4360,
      "confidence": 0.99902344,
      "speaker": null
    },
    {
      "text": "with",
      "start": 4360,
      "end": 4520,
      "confidence": 0.9902344,
      "speaker": null
    },
    {
      "text": "what",
      "start": 4520,
      "end": 4720,
      "confidence": 0.9941406,
      "speaker": null
    },
    {
      "text": "is",
      "start": 4720,
      "end": 4920,
      "confidence": 0.9819336,
      "speaker": null
    },
    {
      "text": "be",
      "start": 4920,
      "end": 5080,
      "confidence": 0.8720703,
      "speaker": null
    },
    {
      "text": "his",
      "start": 5080,
      "end": 5280,
      "confidence": 0.9951172,
      "speaker": null
    },
    {
      "text": "power",
      "start": 5280,
      "end": 5520,
      "confidence": 0.8588867,
      "speaker": null
    },
    {
      "text": "yet",
      "start": 5520,
      "end": 5840,
      "confidence": 0.5756836,
      "speaker": null
    },
    {
      "text": "his",
      "start": 5840,
      "end": 6160,
      "confidence": 0.5419922,
      "speaker": null
    },
    {
      "text": "he",
      "start": 6160,
      "end": 6360,
      "confidence": 0.96972656,
      "speaker": null
    },
    {
      "text": "presumably",
      "start": 6360,
      "end": 6840,
      "confidence": 0.5012207,
      "speaker": null
    },
    {
      "text": "that",
      "start": 6840,
      "end": 7000,
      "confidence": 0.8901367,
      "speaker": null
    },
    {
      "text": "from",
      "start": 7000,
      "end": 7160,
      "confidence": 0.9951172,
      "speaker": null
    },
    {
      "text": "this",
      "start": 7160,
      "end": 7320,
      "confidence": 0.9926758,
      "speaker": null
    },
    {
      "text": "stage",
      "start": 7320,
      "end": 7680,
      "confidence": 0.9953613,
      "speaker": null
    },
    {
      "text": "to",
      "start": 7680,
      "end": 7960,
      "confidence": 0.9941406,
      "speaker": null
    },
    {
      "text": "you",
      "start": 7960,
      "end": 8320,
      "confidence": 0.9975586,
      "speaker": null
    },
    {
      "text": "be",
      "start": 9440,
      "end": 9720,
      "confidence": 0.4555664,
      "speaker": null
    },
    {
      "text": "fired.",
      "start": 9720,
      "end": 10050,
      "confidence": 0.4534912,
      "speaker": null
    }
  ],
  "utterances": null,
  "confidence": 0.90746206,
  "audio_duration": 11,
  "punctuate": true,
  "format_text": true,
  "dual_channel": null,
  "webhook_url": null,
  "webhook_status_code": null,
  "webhook_auth": false,
  "webhook_auth_header_name": null,
  "speed_boost": false,
  "auto_highlights_result": null,
  "auto_highlights": false,
  "audio_start_from": null,
  "audio_end_at": null,
  "word_boost": [],
  "boost_param": null,
  "prompt": null,
  "keyterms_prompt": [],
  "filter_profanity": false,
  "redact_pii": false,
  "redact_pii_audio": false,
  "redact_pii_audio_quality": null,
  "redact_pii_audio_options": null,
  "redact_pii_policies": null,
  "redact_pii_sub": null,
  "speaker_labels": false,
  "speaker_options": null,
  "content_safety": false,
  "iab_categories": false,
  "content_safety_labels": {
    "status": "unavailable",
    "results": [],
    "summary": {}
  },
  "iab_categories_result": {
    "status": "unavailable",
    "results": [],
    "summary": {}
  },
  "language_detection": false,
  "language_detection_options": null,
  "language_confidence_threshold": null,
  "language_confidence": null,
  "custom_spelling": null,
  "throttled": false,
  "auto_chapters": false,
  "summarization": false,
  "summary_type": null,
  "summary_model": null,
  "custom_topics": false,
  "topics": [],
  "speech_threshold": null,
  "speech_model": "universal",
  "chapters": null,
  "disfluencies": false,
  "entity_detection": false,
  "sentiment_analysis": false,
  "sentiment_analysis_results": null,
  "entities": null,
  "speakers_expected": null,
  "summary": null,
  "custom_topics_results": null,
  "is_deleted": null,
  "multichannel": null,
  "project_id": 675898,
  "token_id": 1245789
}
```

{% endcode %}

</details>
