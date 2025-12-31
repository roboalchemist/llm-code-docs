# Source: https://docs.aimlapi.com/api-references/speech-models/text-to-speech/deepgram/aura.md

# aura

<details>

<summary>This documentation is valid for the following list of our models</summary>

<table data-header-hidden data-full-width="true"><thead><tr><th width="215.066650390625"></th><th></th></tr></thead><tbody><tr><td><code>#g1_aura-angus-en</code></td><td><a href="https://aimlapi.com/app/-g1_aura-angus-en" class="button primary">Try in Playground</a></td></tr><tr><td><code>#g1_aura-arcas-en</code></td><td><a href="https://aimlapi.com/app/-g1_aura-arcas-en" class="button primary">Try in Playground</a></td></tr><tr><td><code>#g1_aura-asteria-en</code></td><td><a href="https://aimlapi.com/app/-g1_aura-asteria-en" class="button primary">Try in Playground</a></td></tr><tr><td><code>#g1_aura-athena-en</code></td><td><a href="https://aimlapi.com/app/-g1_aura-athena-en" class="button primary">Try in Playground</a></td></tr><tr><td><code>#g1_aura-helios-en</code></td><td><a href="https://aimlapi.com/app/-g1_aura-helios-en" class="button primary">Try in Playground</a></td></tr><tr><td><code>#g1_aura-hera-en</code></td><td><a href="https://aimlapi.com/app/-g1_aura-hera-en" class="button primary">Try in Playground</a></td></tr><tr><td><code>#g1_aura-luna-en</code></td><td><a href="https://aimlapi.com/app/-g1_aura-luna-en" class="button primary">Try in Playground</a></td></tr><tr><td><code>#g1_aura-orion-en</code></td><td><a href="https://aimlapi.com/app/-g1_aura-orion-en" class="button primary">Try in Playground</a></td></tr><tr><td><code>#g1_aura-orpheus-en</code></td><td><a href="https://aimlapi.com/app/-g1_aura-orpheus-en" class="button primary">Try in Playground</a></td></tr><tr><td><code>#g1_aura-perseus-en</code></td><td><a href="https://aimlapi.com/app/-g1_aura-perseus-en" class="button primary">Try in Playground</a></td></tr><tr><td><code>#g1_aura-stella-en</code></td><td><a href="https://aimlapi.com/app/-g1_aura-stella-en" class="button primary">Try in Playground</a></td></tr><tr><td><code>#g1_aura-zeus-en</code></td><td><a href="https://aimlapi.com/app/-g1_aura-zeus-en" class="button primary">Try in Playground</a></td></tr></tbody></table>

</details>

## Model Overview

Deepgram Aura is the first text-to-speech (TTS) AI model designed for real-time, conversational AI agents and applications. It delivers human-like voice quality with unparalleled speed and efficiency. It has dozen natural, human-like voices with lower latency than any comparable voice AI alternative and supports seamless integration with Deepgram's industry-leading Nova speech-to-text API.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/tts

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Voice.v1.TextToSpeechResponse":{"type":"object","properties":{"metadata":{"type":"object","properties":{"transaction_key":{"type":"string"},"request_id":{"type":"string"},"sha256":{"type":"string"},"created":{"type":"string","format":"date-time"},"duration":{"type":"number"},"channels":{"type":"number"},"models":{"type":"array","items":{"type":"string"}},"model_info":{"type":"object","additionalProperties":{"type":"object","properties":{"name":{"type":"string"},"version":{"type":"string"},"arch":{"type":"string"}},"required":["name","version","arch"]}}},"required":["transaction_key","request_id","sha256","created","duration","channels","models","model_info"]}},"required":["metadata"]}}},"paths":{"/v1/tts":{"post":{"operationId":"VoiceModelsController_textToSpeech_v1","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"enum":["#g1_aura-angus-en","#g1_aura-arcas-en","#g1_aura-asteria-en","#g1_aura-athena-en","#g1_aura-helios-en","#g1_aura-hera-en","#g1_aura-luna-en","#g1_aura-orion-en","#g1_aura-orpheus-en","#g1_aura-perseus-en","#g1_aura-stella-en","#g1_aura-zeus-en"]},"text":{"type":"string","description":"The text content to be converted to speech."},"container":{"type":"string","description":"The file format wrapper for the output audio. The available options depend on the encoding type."},"encoding":{"type":"string","enum":["linear16","mulaw","alaw","mp3","opus","flac","aac"],"default":"linear16","description":"Specifies the expected encoding of your audio output"},"sample_rate":{"type":"string","description":"The sample rate for the output audio. Based on the encoding, different sample rates are supported. For some encodings, the sample rate is not configurable"}},"required":["model","text"],"additionalProperties":false}}}},"responses":{"201":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Voice.v1.TextToSpeechResponse"}}}}},"tags":["Voice Models"]}}}}
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
        "model": "#g1_aura-athena-en",
        "text": '''
        Cities of the future promise to radically transform how people live, work, and move. 
        Instead of sprawling layouts, we’ll see vertical structures that integrate residential, work, and public spaces into single, self-sustaining ecosystems. 
        Architecture will adapt to climate conditions, and buildings will be energy-efficient—generating power through solar panels, wind turbines, and even foot traffic.
    '''
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
  model: "#g1_aura-athena-en",
  text: `
Cities of the future promise to radically transform how people live, work, and move. 
Instead of sprawling layouts, we’ll see vertical structures that integrate residential, work, and public spaces into single, self-sustaining ecosystems. 
Architecture will adapt to climate conditions, and buildings will be energy-efficient—generating power through solar panels, wind turbines, and even foot traffic.
  `
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

{% embed url="<https://drive.google.com/file/d/1DUlxcHSq4iZzDEVG1dbTLGJHMqeMlQpt/view?usp=sharing>" %}
