# Source: https://docs.aimlapi.com/api-references/speech-models/text-to-speech/openai/tts-1-hd.md

# TTS-1 HD

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `openai/tts-1-hd`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/openai/tts-1-hd" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

This model is designed for high quality text-to-speech generation.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/tts

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Voice.v1.TextToSpeechResponse":{"type":"object","properties":{"metadata":{"type":"object","properties":{"transaction_key":{"type":"string"},"request_id":{"type":"string"},"sha256":{"type":"string"},"created":{"type":"string","format":"date-time"},"duration":{"type":"number"},"channels":{"type":"number"},"models":{"type":"array","items":{"type":"string"}},"model_info":{"type":"object","additionalProperties":{"type":"object","properties":{"name":{"type":"string"},"version":{"type":"string"},"arch":{"type":"string"}},"required":["name","version","arch"]}}},"required":["transaction_key","request_id","sha256","created","duration","channels","models","model_info"]}},"required":["metadata"]}}},"paths":{"/v1/tts":{"post":{"operationId":"VoiceModelsController_textToSpeech_v1","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"enum":["openai/tts-1-hd"]},"text":{"type":"string","minLength":1,"maxLength":4096,"description":"The text content to be converted to speech."},"voice":{"type":"string","enum":["alloy","ash","ballad","coral","echo","fable","nova","onyx","sage","shimmer","verse"],"default":"alloy","description":"Name of the voice to be used."},"style":{"type":"string","description":"Determines the style exaggeration of the voice. This setting attempts to amplify the style of the original speaker. It does consume additional computational resources and might increase latency if set to anything other than 0."},"response_format":{"type":"string","enum":["mp3","opus","aac","flac","wav","pcm"],"default":"mp3","description":"Format of the output content for non-streaming requests. Controls how the generated audio data is encoded in the response."},"speed":{"type":"number","minimum":0.25,"maximum":4,"default":1,"description":"Adjusts the speed of the voice. A value of 1.0 is the default speed, while values less than 1.0 slow down the speech, and values greater than 1.0 speed it up."}},"required":["model","text"]}}}},"responses":{"201":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Voice.v1.TextToSpeechResponse"}}}}},"tags":["Voice Models"]}}}}
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
    "model": "openai/tts-1-hd",
    "text": "TTS-1 is a fast and powerful language model. Use it to convert text to natural sounding spoken text.",
    "voice": "coral",
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
  model: "openai/tts-1-hd",
  text: "TTS-1 is a fast and powerful language model. Use it to convert text to natural sounding spoken text.",
  voice: "coral",
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
Audio URL: https://cdn.aimlapi.com/generations/hedgehog/1760948051400-99effd93-a38a-43d5-b4e4-76b42afb6e67.mp3
```

{% endcode %}

</details>

Listen to the audio sample we generated:

{% embed url="<https://drive.google.com/file/d/1d-FCR76Q9OXaVN3Or5txh_6sheEy_J4w/view?usp=sharing>" %}
