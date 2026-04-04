# Source: https://docs.aimlapi.com/api-references/speech-models/text-to-speech/inworld/tts-1-max.md

# inworld/tts-1-max

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `inworld/tts-1-max`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/inworld/tts-1-max" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

This model is designed for realtime text-to-speech generation. A larger, more expressive variant of [inworld/tts-1](https://docs.aimlapi.com/api-references/speech-models/text-to-speech/inworld/tts-1).

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/tts

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Voice.v1.TextToSpeechResponse":{"type":"object","properties":{"metadata":{"type":"object","properties":{"transaction_key":{"type":"string"},"request_id":{"type":"string"},"sha256":{"type":"string"},"created":{"type":"string","format":"date-time"},"duration":{"type":"number"},"channels":{"type":"number"},"models":{"type":"array","items":{"type":"string"}},"model_info":{"type":"object","additionalProperties":{"type":"object","properties":{"name":{"type":"string"},"version":{"type":"string"},"arch":{"type":"string"}},"required":["name","version","arch"]}}},"required":["transaction_key","request_id","sha256","created","duration","channels","models","model_info"]}},"required":["metadata"]}}},"paths":{"/v1/tts":{"post":{"operationId":"VoiceModelsController_textToSpeech_v1","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"enum":["inworld/tts-1-max"]},"text":{"type":"string","minLength":1,"maxLength":500000,"description":"The text content to be converted to speech."},"voice":{"type":"string","enum":["Alex","Ashley","Craig","Deborah","Dennis","Dominus","Edward","Elizabeth","Hades","Heitor","Julia","Maitê","Mark","Olivia","Pixie","Priya","Ronald","Sarah","Shaun","Theodore","Timothy","Wendy"],"default":"Alex","description":"Name of the voice to be used."},"format":{"type":"string","enum":["wav","mp3"],"default":"mp3","description":"Audio output format. WAV delivers uncompressed audio in a widely supported container format, while MP3 provides good compression and compatibility."}},"required":["model","text"]}}}},"responses":{"201":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Voice.v1.TextToSpeechResponse"}}}}},"tags":["Voice Models"]}}}}
```

## Code Example

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

# Insert your AI/ML API key instead of <YOUR_AIMLAPI_KEY>:
api_key = "<YOUR_AIMLAPI_KEY>" 
base_url = "https://api.aimlapi.com/v1"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

data = {
    "model": "inworld/tts-1-max",
    "text": "It is a fast and powerful language model. Use it to convert text to natural sounding spoken text.",
    "voice": "Timothy",
}

response = requests.post(f"{base_url}/tts", headers=headers, json=data)
response.raise_for_status()

result = response.json()

print("Audio URL:", result["audio"]["url"])
```

{% endcode %}
{% endtab %}

{% tab title="JaveScript" %}
{% code overflow="wrap" %}

```javascript
import axios from "axios";

// Insert your AI/ML API key instead of <YOUR_AIMLAPI_KEY>:
const apiKey = "<YOUR_API_KEY>";
const baseURL = "https://api.aimlapi.com/v1";

const headers = {
  Authorization: `Bearer ${apiKey}`,
  "Content-Type": "application/json",
};

const data = {
  model: "inworld/tts-1-max",
  text: "It is a fast and powerful language model. Use it to convert text to natural sounding spoken text.",
  voice: "Timothy",
};

const main = async () => {
  const response = await axios.post(`${baseURL}/tts`, data, { headers });
  console.log("Audio URL:", response.data.audio.url);
};

main().catch(console.error);
```

{% endcode %}
{% endtab %}
{% endtabs %}

<details>

<summary>Response</summary>

{% code overflow="wrap" %}

```
Audio URL: https://cdn.aimlapi.com/generations/tts/inworld-tts-fc718c97-12b3-42dc-919c-518c48ace59a.mp3/1764327592881-89e9ea63-935c-42d0-b769-8290ad769b7c.mp3
```

{% endcode %}

</details>

Listen to the audio sample we generated (\~ 3.2 s):

{% embed url="<https://drive.google.com/file/d/1qPJZfzsvqsEliyVS9SZsjT-R6B_KFhNE/view>" %}
