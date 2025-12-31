# Source: https://docs.aimlapi.com/api-references/speech-models/text-to-speech/elevenlabs/eleven_turbo_v2_5.md

# eleven\_turbo\_v2\_5

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `elevenlabs/eleven_turbo_v2_5`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/elevenlabs/eleven_turbo_v2_5" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

A high-quality text-to-speech model offering natural-sounding intonation, support for **31** languages, and a broad selection of built-in voices. Up to 3× faster than [eleven\_multilingual\_v2](https://docs.aimlapi.com/api-references/speech-models/text-to-speech/elevenlabs/eleven_multilingual_v2).\
A wide range of output audio formats and quality settings is also available.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/tts

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Voice.v1.TextToSpeechResponse":{"type":"object","properties":{"metadata":{"type":"object","properties":{"transaction_key":{"type":"string"},"request_id":{"type":"string"},"sha256":{"type":"string"},"created":{"type":"string","format":"date-time"},"duration":{"type":"number"},"channels":{"type":"number"},"models":{"type":"array","items":{"type":"string"}},"model_info":{"type":"object","additionalProperties":{"type":"object","properties":{"name":{"type":"string"},"version":{"type":"string"},"arch":{"type":"string"}},"required":["name","version","arch"]}}},"required":["transaction_key","request_id","sha256","created","duration","channels","models","model_info"]}},"required":["metadata"]}}},"paths":{"/v1/tts":{"post":{"operationId":"VoiceModelsController_textToSpeech_v1","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"enum":["elevenlabs/eleven_turbo_v2_5"]},"text":{"type":"string","description":"The text content to be converted to speech."},"voice":{"type":"string","enum":["Rachel","Drew","Clyde","Paul","Aria","Domi","Dave","Roger","Fin","Sarah","Antoni","Laura","Thomas","Charlie","George","Emily","Elli","Callum","Patrick","River","Harry","Liam","Dorothy","Josh","Arnold","Charlotte","Alice","Matilda","James","Joseph","Will","Jeremy","Jessica","Eric","Michael","Ethan","Chris","Gigi","Freya","Santa Claus","Brian","Grace","Daniel","Lily","Serena","Adam","Nicole","Bill","Jessie","Sam","Glinda","Giovanni","Mimi"],"description":"Name of the voice to be used"},"apply_text_normalization":{"type":"string","enum":["auto","on","off"],"description":"This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped."},"next_text":{"type":"string","description":"The text that comes after the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation."},"previous_text":{"type":"string","description":"The text that came before the text of the current request. Can be used to improve the speech's continuity when concatenating together multiple generations or to influence the speech's continuity in the current generation."},"output_format":{"type":"string","enum":["mp3_22050_32","mp3_44100_32","mp3_44100_64","mp3_44100_96","mp3_44100_128","mp3_44100_192","pcm_8000","pcm_16000","pcm_22050","pcm_24000","pcm_44100","pcm_48000","ulaw_8000","alaw_8000","opus_48000_32","opus_48000_64","opus_48000_96","opus_48000_128","opus_48000_192"],"description":"Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32"},"voice_settings":{"type":"object","properties":{"stability":{"type":"number","description":"Determines how stable the voice is and the randomness between each generation. Lower values introduce broader emotional range for the voice. Higher values can result in a monotonous voice with limited emotion."},"use_speaker_boost":{"type":"boolean","description":"This setting boosts the similarity to the original speaker. Using this setting requires a slightly higher computational load, which in turn increases latency."},"similarity_boost":{"type":"number","description":"Determines how closely the AI should adhere to the original voice when attempting to replicate it."},"style":{"type":"number","description":"Determines the style exaggeration of the voice. This setting attempts to amplify the style of the original speaker. It does consume additional computational resources and might increase latency if set to anything other than 0."},"speed":{"type":"number","description":"Adjusts the speed of the voice. A value of 1.0 is the default speed, while values less than 1.0 slow down the speech, and values greater than 1.0 speed it up."}},"description":"Voice settings overriding stored settings for the given voice. They are applied only on the given request."},"seed":{"type":"integer","description":"If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed."}},"required":["model","text","voice"]}}}},"responses":{"201":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Voice.v1.TextToSpeechResponse"}}}}},"tags":["Voice Models"]}}}}
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
         # Insert your AI/ML API key instead of <YOUR_AIMLAPI_KEY>:
        "Authorization": "Bearer <YOUR_AIMLAPI_KEY>",
    }
    payload = {
        "model": "elevenlabs/eleven_turbo_v2_5",
        "text": '''
        Cities of the future promise to radically transform how people live, work, and move. 
        Instead of sprawling layouts, we’ll see vertical structures that integrate residential, work, and public spaces into single, self-sustaining ecosystems. 
        Architecture will adapt to climate conditions, and buildings will be energy-efficient—generating power through solar panels, wind turbines, and even foot traffic.
    ''',
        "voice": "Nicole"
    }

    response = requests.post(url, headers=headers, json=payload, stream=True)
    # result = os.path.join(os.path.dirname(__file__), "audio.wav")  # if you run this code as a .py file
    result = "audio.wav"  # if you run this code in Jupyter Notebook    

    with open(result, "wb") as write_stream:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                write_stream.write(chunk)

    print("Audio saved to:", result)


main()
```

{% endcode %}
{% endtab %}

{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
const https = require("https");
const fs = require("fs");

// Insert your AI/ML API key instead of <YOUR_AIMLAPI_KEY>:
const apiKey = "<YOUR_AIMLAPI_KEY>";

const data = JSON.stringify({
  model: "elevenlabs/eleven_turbo_v2_5",
  text: `
Cities of the future promise to radically transform how people live, work, and move. 
Instead of sprawling layouts, we’ll see vertical structures that integrate residential, work, and public spaces into single, self-sustaining ecosystems. 
Architecture will adapt to climate conditions, and buildings will be energy-efficient—generating power through solar panels, wind turbines, and even foot traffic.
  `,
  voice: "Nicole",
});

const options = {
  hostname: "api.aimlapi.com",
  path: "/v1/tts",
  method: "POST",
  headers: {
    "Authorization": `Bearer ${apiKey}`,
    "Content-Type": "application/json",
    "Content-Length": Buffer.byteLength(data),
  }
};

const req = https.request(options, (res) => {
  if (res.statusCode >= 400) {
    let error = "";
    res.on("data", chunk => error += chunk);
    res.on("end", () => {
      console.error(`Error ${res.statusCode}:`, error);
    });
    return;
  }

  const file = fs.createWriteStream("audio.wav");
  res.pipe(file);

  file.on("finish", () => {
    file.close();
    console.log("Audio saved to audio.wav");
  });
});

req.on("error", (e) => {
  console.error("Request error:", e);
});

req.write(data);
req.end();
```

{% endcode %}
{% endtab %}
{% endtabs %}

<details>

<summary>Response</summary>

```
Audio saved to: audio.wav
```

</details>

{% embed url="<https://drive.google.com/file/d/1GW05P4Gfugtx10vfaw106cogTz9JrBOG/view?usp=sharing>" %}
Each voice in ElevenLabs models has its own accent and unique characteristics.\
Check out this amazing female whisper we stumbled upon completely by accident.
{% endembed %}
