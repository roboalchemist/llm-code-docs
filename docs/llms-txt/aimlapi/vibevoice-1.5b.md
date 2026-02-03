# Source: https://docs.aimlapi.com/api-references/speech-models/text-to-speech/microsoft/vibevoice-1.5b.md

# vibevoice-1.5b

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `microsoft/vibevoice-1.5b`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/microsoft/vibevoice-1-5b" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

Designed to produce rich, multi-speaker conversations from text, the model is well-suited for podcasts and other long-form audio content.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/tts

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Voice.v1.TextToSpeechResponse":{"type":"object","properties":{"metadata":{"type":"object","properties":{"transaction_key":{"type":"string"},"request_id":{"type":"string"},"sha256":{"type":"string"},"created":{"type":"string","format":"date-time"},"duration":{"type":"number"},"channels":{"type":"number"},"models":{"type":"array","items":{"type":"string"}},"model_info":{"type":"object","additionalProperties":{"type":"object","properties":{"name":{"type":"string"},"version":{"type":"string"},"arch":{"type":"string"}},"required":["name","version","arch"]}}},"required":["transaction_key","request_id","sha256","created","duration","channels","models","model_info"]}},"required":["metadata"]}}},"paths":{"/v1/tts":{"post":{"operationId":"VoiceModelsController_textToSpeech_v1","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"enum":["microsoft/vibevoice-1.5b"]},"script":{"type":"string","minLength":1,"maxLength":5000,"description":"The script to convert to speech. Can be formatted with \"Speaker X:\" prefixes for multi-speaker dialogues."},"speakers":{"type":"array","items":{"type":"object","properties":{"preset":{"type":"string","enum":["Alice [EN]","Alice [EN] (Background Music)","Carter [EN]","Frank [EN]","Maya [EN]","Anchen [ZH] (Background Music)","Bowen [ZH]","Xinran [ZH]"],"description":"Default voice preset to use for the speaker. Not used if audio_url is provided."},"audio_url":{"type":"string","format":"uri","description":"URL to a voice sample audio file. If provided, preset will be ignored."}}},"minItems":1,"maxItems":4,"default":[{"preset":"Alice [EN]"}],"description":"List of speakers to use for the script. If not provided, will be inferred from the script or voice samples."},"seed":{"type":"integer","description":"If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed."},"cfg_scale":{"type":"number","minimum":0.1,"maximum":2,"default":1.3,"description":"The CFG (Classifier Free Guidance) scale is a measure of how close you want the model to stick to your prompt."}},"required":["model","script"]}}}},"responses":{"201":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Voice.v1.TextToSpeechResponse"}}}}},"tags":["Voice Models"]}}}}
```

## Code Example

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import os
import requests

def main():
    url = "https://api.aimlapi.com/v1/tts"
    headers = {
        "Authorization": "Bearer <YOUR_AIMLAPI_KEY>",
    }
    payload = { 
        "model": "microsoft/vibevoice-1.5b",
        "script": "Speaker 1: Wow, whats happening, Alice? \nSpeaker 2: Oh, just the usual… a full-blown AI revolution. Nothing to worry about",
        "speakers": [
            {   "preset": "Frank [EN]"   },
            {   "preset": "Alice [EN]"   }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        response_data = response.json()
        audio_url = response_data["audio"]["url"]
        file_name = response_data["audio"]["file_name"]
        
        audio_response = requests.get(audio_url, stream=True)
        audio_response.raise_for_status()
        
        # Save with the original file extension from the API
        # dist = os.path.join(os.path.dirname(__file__), file_name)  # if you run this code as a .py file
        dist = "audio.wav"  # if you run this code in Jupyter Notebook

        with open(dist, "wb") as write_stream:
            for chunk in audio_response.iter_content(chunk_size=8192):
                if chunk:
                    write_stream.write(chunk)

        print("Audio saved to:", dist)
        print(f"Duration: {response_data['duration']} seconds")
        print(f"Sample rate: {response_data['sample_rate']} Hz")
        
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

{% endcode %}
{% endtab %}
{% endtabs %}

<details>

<summary>Response</summary>

```
Audio saved to: audio.wav
Duration: 8.4 seconds
Sample rate: 24000 Hz
```

</details>

Listen to the dialogue we generated:

{% embed url="<https://drive.google.com/file/d/12Cfolhx2jx7QWWfUTNiuXYhPBBtqvdwh/view>" %}
