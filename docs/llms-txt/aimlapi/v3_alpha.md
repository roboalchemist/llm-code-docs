# Source: https://docs.aimlapi.com/api-references/speech-models/voice-chat/elevenlabs/v3_alpha.md

# v3\_alpha

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `elevenlabs/v3_alpha`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/elevenlabs/v3_alpha" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

The model supports a wide range of output formats and quality levels, text normalization, and over 70 languages.

## How to Make a Call

<details>

<summary>Step-by-Step Instructions</summary>

:digit\_one: **Setup You Can’t Skip**

:black\_small\_square: [**Create an Account**](https://aimlapi.com/app/sign-up): Visit the AI/ML API website and create an account (if you don’t have one yet).\
:black\_small\_square: [**Generate an API Key**](https://aimlapi.com/app/keys): After logging in, navigate to your account dashboard and generate your API key. Ensure that key is enabled on UI.

:digit\_two: **Copy the code example**

At the bottom of this page, you'll find [a code example](#quick-code-example) that shows how to structure the request. Choose the code snippet in your preferred programming language and copy it into your development environment.

:digit\_three: **Modify the code example**

:black\_small\_square: Replace `<YOUR_AIMLAPI_KEY>` with your actual AI/ML API key from your account.\
:black\_small\_square: Provide your instructions via the `text` parameter and set the model voice in the `voice` parameter.

:digit\_four: <sup><sub><mark style="background-color:yellow;">**(Optional)**<mark style="background-color:yellow;"><sub></sup>**&#x20;Adjust other optional parameters if needed**

Only `text` and `voice` are required parameters for this model (and we’ve already filled them in for you in the example), but you can include optional parameters if needed to adjust the model’s behavior. Below, you can find the corresponding [API schema](#api-schemas), which lists all available parameters along with notes on how to use them.

:digit\_five: **Run your modified code**

Run your modified code in your development environment. Response time depends on various factors, but for simple prompts it rarely exceeds 5 seconds.

{% hint style="success" %}
If you need a more detailed walkthrough for setting up your development environment and making a request step by step — feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).
{% endhint %}

</details>

## Quick Code Example

Here is an example of generating an audio response to the user input provided in the `text` parameter.

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import os
import request


def main():
    url = "https://api.aimlapi.com/v1/tts"
    headers = {
        # Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
        "Authorization": "Bearer <YOUR_AIMLAPI_KEY>",
    }
    payload = {
        "model": "elevenlabs/v3_alpha",
        "text": "Hi! What are you doing today?",
        "voice": "Alice"
    }

    response = requests.post(url, headers=headers, json=payload, stream=True)
    dist = os.path.abspath("audio.wav")

    with open(dist, "wb") as write_stream:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                write_stream.write(chunk)

    print("Audio saved to:", dist)


main()
```

{% endcode %}
{% endtab %}

{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
const fs = require('fs');
const path = require('path');
const url = 'https://api.aimlapi.com/v1/tts';

async function main() {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer <YOUR_AIMLAPI_KEY>',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        model: 'elevenlabs/v3_alpha',
        text: 'Hi! What are you doing today?',
        voice: 'Alice'
      })
    });

    const dist = path.resolve(__dirname, 'audio.wav'); // Path to save audio
    const fileStream = fs.createWriteStream(dist);

    // Write audio stream to file
    const reader = response.body.getReader();
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      fileStream.write(value);
    }
    fileStream.end();
    console.log('Audio saved to:', dist);
}

main();
```

{% endcode %}
{% endtab %}
{% endtabs %}

<details>

<summary>Response</summary>

{% code overflow="wrap" %}

```json5
Audio saved to: c:\Users\user\Documents\Python Scripts\AUDIOs\audio.wav
```

{% endcode %}

</details>

Listen to the audio response:

{% embed url="<https://drive.google.com/file/d/1fAR1OVU26huTfgbhNq6KF205y3hCVgCR/view?usp=sharing>" %}

## API Schemas

## POST /v1/tts

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Voice.v1.TextToSpeechResponse":{"type":"object","properties":{"metadata":{"type":"object","properties":{"transaction_key":{"type":"string"},"request_id":{"type":"string"},"sha256":{"type":"string"},"created":{"type":"string","format":"date-time"},"duration":{"type":"number"},"channels":{"type":"number"},"models":{"type":"array","items":{"type":"string"}},"model_info":{"type":"object","additionalProperties":{"type":"object","properties":{"name":{"type":"string"},"version":{"type":"string"},"arch":{"type":"string"}},"required":["name","version","arch"]}}},"required":["transaction_key","request_id","sha256","created","duration","channels","models","model_info"]}},"required":["metadata"]}}},"paths":{"/v1/tts":{"post":{"operationId":"VoiceModelsController_textToSpeech_v1","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"enum":["elevenlabs/v3_alpha"]},"text":{"type":"string","description":"The text content to be converted to speech."},"voice":{"type":"string","enum":["Rachel","Drew","Clyde","Paul","Aria","Domi","Dave","Roger","Fin","Sarah","Antoni","Laura","Thomas","Charlie","George","Emily","Elli","Callum","Patrick","River","Harry","Liam","Dorothy","Josh","Arnold","Charlotte","Alice","Matilda","James","Joseph","Will","Jeremy","Jessica","Eric","Michael","Ethan","Chris","Gigi","Freya","Santa Claus","Brian","Grace","Daniel","Lily","Serena","Adam","Nicole","Bill","Jessie","Sam","Glinda","Giovanni","Mimi"],"default":"Rachel","description":"Name of the voice to be used."},"apply_text_normalization":{"type":"string","enum":["auto","on","off"],"description":"This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped."},"output_format":{"type":"string","enum":["mp3_22050_32","mp3_44100_32","mp3_44100_64","mp3_44100_96","mp3_44100_128","mp3_44100_192","pcm_8000","pcm_16000","pcm_22050","pcm_24000","pcm_44100","pcm_48000","ulaw_8000","alaw_8000","opus_48000_32","opus_48000_64","opus_48000_96","opus_48000_128","opus_48000_192"],"description":"Format of the output content for non-streaming requests. Controls how the generated audio data is encoded in the response."},"voice_settings":{"type":"object","properties":{"stability":{"type":"number","description":"Determines how stable the voice is and the randomness between each generation. Lower values introduce broader emotional range for the voice. Higher values can result in a monotonous voice with limited emotion."},"use_speaker_boost":{"type":"boolean","description":"This setting boosts the similarity to the original speaker. Using this setting requires a slightly higher computational load, which in turn increases latency."},"similarity_boost":{"type":"number","description":"Determines how closely the AI should adhere to the original voice when attempting to replicate it."},"style":{"type":"number","description":"Determines the style exaggeration of the voice. This setting attempts to amplify the style of the original speaker. It does consume additional computational resources and might increase latency if set to anything other than 0."},"speed":{"type":"number","description":"Adjusts the speed of the voice. A value of 1.0 is the default speed, while values less than 1.0 slow down the speech, and values greater than 1.0 speed it up."}},"description":"Voice settings overriding stored settings for the given voice. They are applied only on the given request."},"seed":{"type":"integer","description":"If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed."}},"required":["model","text"]}}}},"responses":{"201":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Voice.v1.TextToSpeechResponse"}}}}},"tags":["Voice Models"]}}}}
```
