# Source: https://docs.aimlapi.com/api-references/speech-models/text-to-speech/alibaba-cloud/qwen3-tts-flash.md

# qwen3-tts-flash

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `alibaba/qwen3-tts-flash`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/alibaba/qwen3-tts-flash" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

The model offers a range of natural, human-like voices with support for multiple languages and dialects. It can produce multilingual speech in a consistent voice, adapting tone and intonation to deliver smooth, expressive narration even for complex text.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/tts

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Voice.v1.TextToSpeechResponse":{"type":"object","properties":{"metadata":{"type":"object","properties":{"transaction_key":{"type":"string"},"request_id":{"type":"string"},"sha256":{"type":"string"},"created":{"type":"string","format":"date-time"},"duration":{"type":"number"},"channels":{"type":"number"},"models":{"type":"array","items":{"type":"string"}},"model_info":{"type":"object","additionalProperties":{"type":"object","properties":{"name":{"type":"string"},"version":{"type":"string"},"arch":{"type":"string"}},"required":["name","version","arch"]}}},"required":["transaction_key","request_id","sha256","created","duration","channels","models","model_info"]}},"required":["metadata"]}}},"paths":{"/v1/tts":{"post":{"operationId":"VoiceModelsController_textToSpeech_v1","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"enum":["alibaba/qwen3-tts-flash"]},"text":{"type":"string","minLength":1,"maxLength":600,"description":"The text content to be converted to speech."},"voice":{"type":"string","enum":["Cherry","Ethan","Nofish","Jennifer","Ryan","Katerina","Elias","Jada","Dylan","Sunny","Li","Marcus","Roy","Peter","Rocky","Kiki","Eric"],"description":"Name of the voice to be used"}},"required":["model","text","voice"]}}}},"responses":{"201":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Voice.v1.TextToSpeechResponse"}}}}},"tags":["Voice Models"]}}}}
```

## Code Example

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests
import json   # for getting a structured output with indentation

def main():
    url = "https://api.aimlapi.com/v1/tts"
    headers = {
        # Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
        "Authorization": "Bearer <YOUR_AIMLAPI_KEY>",
    }
    payload = { 
        "model": "alibaba/qwen3-tts-flash",
        "text": "Qwen3 Speech Synthesis offers a range of natural, human-like voices with support for multiple languages and dialects. It can produce multilingual speech in a consistent voice, adapting tone and intonation to deliver smooth, expressive narration even for complex text.",
        "voice": "Cherry"
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    print(json.dumps(data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
```

{% endcode %}
{% endtab %}
{% endtabs %}

<details>

<summary>Response</summary>

{% code overflow="wrap" %}

```json5
{
  "audio": {
    "url": "http://dashscope-result-sgp.oss-ap-southeast-1.aliyuncs.com/1d/18/20251022/cc0d532d/4adfa7be-08fe-4960-96c9-7dd866b24b48.wav?Expires=1761212494&OSSAccessKeyId=LTAI5tBLUzt9WaK89DU8aECd&Signature=CRyPQI%2BtVRQZSfjI5C5QH0VGDwU%3D"
  },
  "usage": {
    "characters": 267
  }
}
```

{% endcode %}

</details>

{% embed url="<https://drive.google.com/file/d/15A-Ohkk2D0tDoTuYOOFDGAHrLiv0QUXt/view?usp=sharing>" %}
