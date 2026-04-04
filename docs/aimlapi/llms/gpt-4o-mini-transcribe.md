# Source: https://docs.aimlapi.com/api-references/speech-models/speech-to-text/openai/gpt-4o-mini-transcribe.md

# gpt-4o-mini-transcribe

{% hint style="info" %}
This documentation is valid for the following list of our models:

* `openai/gpt-4o-mini-transcribe`
  {% endhint %}

## Model Overview

A speech-to-text model based on [GPT-4o mini](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o-mini) for audio transcription. It provides improved word error rates and more accurate language recognition compared to the original Whisper models. Recommended for use cases that require higher transcription accuracy.

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
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Voice.v1.SpeechToTextCreateResponseDTO":{"type":"object","properties":{"generation_id":{"type":"string","format":"uuid"}},"required":["generation_id"]}}},"paths":{"/v1/stt/create":{"post":{"operationId":"VoiceModelsController_createSpeechToText_v1","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"enum":["openai/gpt-4o-mini-transcribe"]},"language":{"type":"string","description":"The BCP-47 language tag that hints at the primary spoken language. Depending on the Model and API endpoint you choose only certain languages are available"},"prompt":{"type":"string","description":"An optional text to guide the model's style or continue a previous audio segment. The prompt should match the audio language."},"temperature":{"type":"number","minimum":0,"maximum":1,"default":0,"description":"The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic."},"url":{"type":"string","format":"uri","description":"URL of the input audio file."}},"required":["model","url"]}}}},"responses":{"201":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Voice.v1.SpeechToTextCreateResponseDTO"}}}}},"tags":["Voice Models"]}}}}
```

#### Requesting the result of the task from the server using the generation\_id

## GET /v1/stt/{generation\_id}

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Voice.v1.SpeechToTextGetResponseDTO":{"type":"object","properties":{"generation_id":{"type":"string"},"status":{"type":"string","enum":["queued","completed","error","generating"]},"result":{"anyOf":[{"type":"object","properties":{"metadata":{"type":"object","properties":{"transaction_key":{"type":"string","description":"A unique transaction key; currently always “deprecated”."},"request_id":{"type":"string","description":"A UUID identifying this specific transcription request."},"sha256":{"type":"string","description":"The SHA-256 hash of the submitted audio file (for pre-recorded requests)."},"created":{"type":"string","format":"date-time","description":"ISO-8601 timestamp."},"duration":{"type":"number","description":"Length of the audio in seconds."},"channels":{"type":"number","description":"The top-level results object containing per-channel transcription alternatives."},"models":{"type":"array","items":{"type":"string"},"description":"List of model UUIDs used for this transcription"},"model_info":{"type":"object","additionalProperties":{"type":"object","properties":{"name":{"type":"string","description":"The human-readable name of the model — identifies which model was used."},"version":{"type":"string","description":"The specific version of the model."},"arch":{"type":"string","description":"The architecture of the model — describes the model family / generation."}},"required":["name","version","arch"]},"description":"Mapping from each model UUID (in 'models') to detailed info: its name, version, and architecture."}},"required":["transaction_key","request_id","sha256","created","duration","channels","models","model_info"],"description":"Metadata about the transcription response, including timing, models, and IDs."},"results":{"type":"object","nullable":true,"properties":{"channels":{"type":"object","properties":{"alternatives":{"type":"array","items":{"type":"object","properties":{"transcript":{"type":"string","description":"The full transcript text for this alternative."},"confidence":{"type":"number","description":"Overall confidence score (0-1) that assigns to this transcript alternative."},"words":{"type":"array","items":{"type":"object","properties":{"word":{"type":"string","description":"The raw recognized word, without punctuation or capitalization."},"start":{"type":"number","description":"Start timestamp of the word (in seconds, from beginning of audio)."},"end":{"type":"number","description":"End timestamp of the word (in seconds)."},"confidence":{"type":"number","description":"Confidence score (0-1) for this individual word."},"punctuated_word":{"type":"string","description":"The same word but with punctuation/capitalization applied (if smart_format is enabled)."}},"required":["word","start","end","confidence","punctuated_word"]},"description":"List of word-level timing, confidence, and punctuation details."},"paragraphs":{"type":"array","items":{"type":"object","properties":{"transcript":{"type":"string","description":"The transcript split into paragraphs (with line breaks), when paragraphing is enabled."},"paragraphs":{"type":"object","properties":{"sentences":{"type":"array","items":{"type":"object","properties":{"text":{"type":"string","description":"Text of a single sentence in the paragraph."},"start":{"type":"number","description":"Start time of the sentence (in seconds)."},"end":{"type":"number","description":"End time of the sentence (in seconds)."}},"required":["text","start","end"]},"description":"List of sentences in this paragraph, with start/end times."},"num_words":{"type":"number","description":"Number of words in this paragraph."},"start":{"type":"number","description":"Start time of the paragraph (in seconds)."},"end":{"type":"number","description":"End time of the paragraph (in seconds)."}},"required":["sentences","num_words","start","end"],"description":"Structure describing each paragraph: its timespan, word count, and sentence breakdown."}},"required":["transcript","paragraphs"]},"description":"An array of paragraph objects, present when the paragraphs feature is enabled."}},"required":["transcript","confidence","words","paragraphs"]},"description":"List of possible transcription hypotheses (“alternatives”) for each channel."}},"required":["alternatives"],"description":"The top-level results object containing per-channel transcription alternatives."}},"required":["channels"]}},"required":["metadata"]},{"type":"object","properties":{"id":{"type":"string","format":"uuid"},"language_model":{"type":"string"},"acoustic_model":{"type":"string"},"language_code":{"type":"string"},"status":{"type":"string","enum":["queued","processing","completed","error"]},"language_detection":{"type":"boolean"},"language_confidence_threshold":{"type":"number"},"language_confidence":{"type":"number"},"speech_model":{"type":"string","enum":["best","slam-1","universal"]},"text":{"type":"string"},"words":{"type":"array","items":{"type":"object","properties":{"confidence":{"type":"number"},"end":{"type":"number"},"speaker":{"type":"string"},"start":{"type":"number"},"text":{"type":"string"}},"required":["confidence","end","start","text"]}},"utterances":{"type":"array","items":{"type":"object","properties":{"confidence":{"type":"number"},"end":{"type":"number"},"speaker":{"type":"string"},"start":{"type":"number"},"text":{"type":"string"},"words":{"type":"array","items":{"type":"object","properties":{"confidence":{"type":"number"},"end":{"type":"number"},"speaker":{"type":"string"},"start":{"type":"number"},"text":{"type":"string"}},"required":["confidence","end","start","text"]}}},"required":["confidence","end","speaker","start","text","words"]}},"confidence":{"type":"number"},"audio_duration":{"type":"number"},"punctuate":{"type":"boolean"},"format_text":{"type":"boolean"},"disfluencies":{"type":"boolean"},"multichannel":{"type":"boolean"},"webhook_url":{"type":"string"},"webhook_status_code":{"type":"number"},"webhook_auth_header_name":{"type":"string"},"speed_boost":{"type":"boolean"},"auto_highlights_result":{"type":"object","properties":{"status":{"type":"string"},"results":{"type":"array","items":{"type":"object","properties":{"count":{"type":"number"},"rank":{"type":"number"},"text":{"type":"string"},"timestamps":{"type":"array","items":{"type":"object","properties":{"start":{"type":"number"},"end":{"type":"number"}},"required":["start","end"]}}},"required":["count","rank","text","timestamps"]}}},"required":["status","results"]},"auto_highlights":{"type":"boolean"},"audio_start_from":{"type":"number"},"audio_end_at":{"type":"number"},"word_boost":{"type":"array","items":{"type":"string"}},"boost_param":{"type":"string"},"filter_profanity":{"type":"boolean"},"redact_pii":{"type":"boolean"},"redact_pii_audio":{"type":"boolean"},"redact_pii_audio_quality":{"type":"string","enum":["mp3","wav"]},"redact_pii_policies":{"type":"array","items":{"type":"string"}},"redact_pii_sub":{"type":"string","enum":["entity_name","hash"]},"speaker_labels":{"type":"boolean"},"speakers_expected":{"type":"number"},"content_safety":{"type":"boolean"},"iab_categories":{"type":"boolean"},"content_safety_labels":{"type":"object","properties":{"status":{"type":"string"},"results":{"type":"array","items":{"type":"object","properties":{"text":{"type":"string"},"labels":{"type":"array","items":{"type":"object","properties":{"label":{"type":"string"},"confidence":{"type":"number"},"severity":{"type":"number"}},"required":["label","confidence","severity"]}},"sentences_idx_start":{"type":"number"},"sentences_idx_end":{"type":"number"},"timestamp":{"type":"object","properties":{"start":{"type":"number"},"end":{"type":"number"}},"required":["start","end"]}},"required":["text","labels","sentences_idx_start","sentences_idx_end","timestamp"]}},"summary":{"type":"object","additionalProperties":{"type":"number"}}},"required":["status","results","summary"]},"iab_categories_result":{"type":"object","properties":{"status":{"type":"string"},"results":{"type":"array","items":{"type":"object","properties":{"text":{"type":"string"},"labels":{"type":"array","items":{"type":"object","properties":{"relevance":{"type":"number"},"label":{"type":"string"}},"required":["relevance","label"]}},"timestamp":{"type":"object","properties":{"start":{"type":"number"},"end":{"type":"number"}},"required":["start","end"]}},"required":["text","labels","timestamp"]}},"summary":{"type":"object","additionalProperties":{"type":"number"}}},"required":["status","results","summary"]},"custom_spelling":{"type":"array","items":{"type":"object","properties":{"from":{"type":"string"},"to":{"type":"string"}},"required":["from","to"]}},"chapters":{"type":"array","items":{"type":"object","properties":{"summary":{"type":"string"},"headline":{"type":"string"},"gist":{"type":"string"},"start":{"type":"number"},"end":{"type":"number"}},"required":["summary","headline","gist","start","end"]}},"summarization":{"type":"boolean"},"summary_type":{"type":"string"},"summary_model":{"type":"string"},"summary":{"type":"string"},"auto_chapters":{"type":"boolean"},"sentiment_analysis":{"type":"boolean"},"sentiment_analysis_results":{"type":"array","items":{"type":"object","properties":{"text":{"type":"string"},"start":{"type":"number"},"end":{"type":"number"},"sentiment":{"type":"string","enum":["POSITIVE","NEUTRAL","NEGATIVE"]},"confidence":{"type":"number"},"speaker":{"type":"string"}},"required":["text","start","end","sentiment","confidence"]}},"entity_detection":{"type":"boolean"},"entities":{"type":"array","items":{"type":"object","properties":{"entity_type":{"type":"string"},"text":{"type":"string"},"start":{"type":"number"},"end":{"type":"number"}},"required":["entity_type","text","start","end"]}},"speech_threshold":{"type":"number"},"throttled":{"type":"boolean"},"error":{"type":"string"}},"required":["id","status"],"additionalProperties":false},{"type":"object","properties":{"text":{"type":"string"},"usage":{"type":"object","properties":{"type":{"type":"string","enum":["tokens"]},"input_tokens":{"type":"number"},"input_token_details":{"type":"object","properties":{"text_tokens":{"type":"number"},"audio_tokens":{"type":"number"}},"required":["text_tokens","audio_tokens"]},"output_tokens":{"type":"number"},"total_tokens":{"type":"number"}},"required":["input_tokens","output_tokens","total_tokens"]}},"required":["text"],"additionalProperties":false},{"nullable":true}]},"error":{"nullable":true}},"required":["generation_id","status"]}}},"paths":{"/v1/stt/{generation_id}":{"get":{"operationId":"VoiceModelsController_getSTT_v1","parameters":[{"name":"generation_id","required":true,"in":"path","schema":{"type":"string"}}],"responses":{"201":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Voice.v1.SpeechToTextGetResponseDTO"}}}}},"tags":["Voice Models"]}}}}
```

## Example Code: Processing a Speech Audio File via URL

Let's use the `openai/gpt-4o-mini-transcribe` model to transcribe the following audio fragment:

{% embed url="<https://drive.google.com/file/d/1ZN-28NUbK1TXHt6oEPj42zUJCv82e9L4/view?usp=sharing>" %}

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests
import time
import json

base_url = "https://api.aimlapi.com/v1"
# Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
api_key = "<YOUR_AIMLAPI_KEY>"

# Create and send a speech-to-text conversion task to the server
def create_stt():
    url = f"{base_url}/stt/create"
    headers = {
        "Authorization": f"Bearer {api_key}", 
    }
    data = {
        "model": "openai/gpt-4o-mini-transcribe",
        "url": "https://audio-samples.github.io/samples/mp3/blizzard_primed/sample-0.mp3"
    }
 
    response = requests.post(url, json=data, headers=headers)
    if response.status_code >= 400:
        print(f"Error: {response.status_code} - {response.text}")
    else:
        response_data = response.json()
        print(response_data)
        return response_data

# Request the result of the task from the server using the generation_id
def get_stt(gen_id):
    url = f"{base_url}/stt/{gen_id}"
    headers = {
        "Authorization": f"Bearer {api_key}", 
    }
    response = requests.get(url, headers=headers)
    return response.json()
    
# Start the generation, then repeatedly request the result from the server every 10 sec.
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

            if status in ["queued", "generating"]:
                print(f"Status: {status}. Checking again in 10 seconds.")
                time.sleep(10)
            else:
                # data = .json()
                print("Processing complete:")
                print(json.dumps(response_data["result"], indent=2, ensure_ascii=False))
                return response_data
   
        print("Timeout reached. Stopping.")
        return None     


if __name__ == "__main__":
    main()
```

{% endcode %}
{% endtab %}

{% tab title="JS" %}
{% code overflow="wrap" %}

```javascript
const baseUrl = "https://api.aimlapi.com/v1";
// Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
const apiKey = "<YOUR_AIMLAPI_KEY>";

// Create and send a speech-to-text conversion task to the server
async function createSTT() {
  const url = `${baseUrl}/stt/create`;

  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${apiKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: "openai/gpt-4o-mini-transcribe",
      url: "https://audio-samples.github.io/samples/mp3/blizzard_primed/sample-0.mp3",
    }),
  });

  if (!response.ok) {
    const text = await response.text();
    console.error(`Error: ${response.status} - ${text}`);
    return null;
  }

  const data = await response.json();
  console.log(data);
  return data;
}

// Request the result of the task from the server using the generation_id
async function getSTT(genId) {
  const url = `${baseUrl}/stt/${genId}`;

  const response = await fetch(url, {
    headers: {
      "Authorization": `Bearer ${apiKey}`,
    },
  });

  if (!response.ok) {
    return null;
  }

  return response.json();
}

// Start generation and poll every 10s
async function main() {
  const sttResponse = await createSTT();
  const genId = sttResponse?.generation_id;

  if (!genId) {
    console.error("No generation_id received");
    return null;
  }

  const startTime = Date.now();
  const timeoutMs = 600 * 1000; // 10 minutes

  while (Date.now() - startTime < timeoutMs) {
    const responseData = await getSTT(genId);

    if (!responseData) {
      console.error("Error: No response from API");
      return null;
    }

    const status = responseData.status;

    if (status === "queued" || status === "generating") {
      console.log(`Status: ${status}. Checking again in 10 seconds.`);
      await new Promise(resolve => setTimeout(resolve, 10_000));
    } else {
      console.log("Processing complete:");
      console.log(JSON.stringify(responseData.result, null, 2));
      return responseData;
    }
  }

  console.log("Timeout reached. Stopping.");
  return null;
}

main();
```

{% endcode %}
{% endtab %}
{% endtabs %}

<details>

<summary>Response</summary>

{% code overflow="wrap" %}

```
{'generation_id': 'dzIgQQyw8KCfoI5clcbHZ', 'status': 'queued'}
Status: queued. Checking again in 10 seconds.
Processing complete:
{
  "text": "He doesn't belong to you, and I don't see how you have anything to do with what is be his power of. He's he personified that from this stage to you.",
  "usage": {
    "type": "tokens",
    "total_tokens": 137,
    "input_tokens": 100,
    "input_token_details": {
      "text_tokens": 0,
      "audio_tokens": 100
    },
    "output_tokens": 37
  }
}
```

{% endcode %}

</details>
