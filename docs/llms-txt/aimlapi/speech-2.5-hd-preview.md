# Source: https://docs.aimlapi.com/api-references/speech-models/voice-chat/minimax/speech-2.5-hd-preview.md

# Speech 2.5 HD Preview

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `minimax/speech-2-5-hd-preview`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/minimax/speech-2-5-hd-preview" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

A high-definition text-to-speech model with enhanced multilingual expressiveness, more precise voice replication, and expanded support for 40 languages.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

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
        # Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
        "Authorization": "Bearer <YOUR_AIMLAPI_KEY>",
    }
    payload = {
        "model": "minimax/speech-2.5-turbo-preview",
        "text": "Hi! What are you doing today?",
        "voice_setting": {
          "voice_id": "Wise_Woman"
        }
    }

    response = requests.post(url, headers=headers, json=payload, stream=True)
    dist = os.path.abspath("your_file_name.wav")

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
import fs from "fs";
import path from "path";

async function main() {
  const url = "https://api.aimlapi.com/v1/tts";
  const payload = {
    model: "minimax/speech-2.5-hd-preview",
    text: "Hi! What are you doing today?",
    voice_setting: {
      voice_id: "Wise_Woman"
    }
  };

  const response = await fetch(url, {
    method: "POST",
    headers: {
      // Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
      "Authorization": `Bearer <YOUR_AIMLAPI_KEY>`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });

  // Read response as ArrayBuffer and convert to Buffer
  const arrayBuffer = await response.arrayBuffer();
  const buffer = Buffer.from(arrayBuffer);

  // Save audio to file in the current working directory
  const dist = path.join(process.cwd(), "your_file_name.wav");
  fs.writeFileSync(dist, buffer);

  console.log("Audio saved to:", dist);
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
Audio saved to: c:\Users\user\Documents\Python Scripts\TTSes\your_file_name.wav
```

{% endcode %}

</details>

{% embed url="<https://drive.google.com/file/d/1y1mFt6P-PTHRUW2Rzxkc2TRXR27XP9Gd/view?usp=sharing>" %}

## API Schema

## POST /v1/tts

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Voice.v1.TextToSpeechResponse":{"type":"object","properties":{"metadata":{"type":"object","properties":{"transaction_key":{"type":"string"},"request_id":{"type":"string"},"sha256":{"type":"string"},"created":{"type":"string","format":"date-time"},"duration":{"type":"number"},"channels":{"type":"number"},"models":{"type":"array","items":{"type":"string"}},"model_info":{"type":"object","additionalProperties":{"type":"object","properties":{"name":{"type":"string"},"version":{"type":"string"},"arch":{"type":"string"}},"required":["name","version","arch"]}}},"required":["transaction_key","request_id","sha256","created","duration","channels","models","model_info"]}},"required":["metadata"]}}},"paths":{"/v1/tts":{"post":{"operationId":"VoiceModelsController_textToSpeech_v1","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"enum":["minimax/speech-2.5-hd-preview"]},"text":{"type":"string","minLength":1,"maxLength":5000,"description":"The text content to be converted to speech."},"voice_setting":{"type":"object","properties":{"voice_id":{"type":"string","enum":["Wise_Woman","Friendly_Person","Inspirational_girl","Deep_Voice_Man","Calm_Woman","Casual_Guy","Lively_Girl","Patient_Man","Young_Knight","Determined_Man","Lovely_Girl","Decent_Boy","Imposing_Manner","Elegant_Man","Abbess","Sweet_Girl_2","Exuberant_Girl"],"description":"Voice identifier for text-to-speech synthesis. Supports both predefined system voices and custom cloned voice IDs. "},"speed":{"type":"number","minimum":0.5,"maximum":2,"default":1,"description":"Adjusts the speed of the voice. A value of 1.0 is the default speed, while values less than 1.0 slow down the speech, and values greater than 1.0 speed it up."},"vol":{"type":"number","minimum":0.01,"maximum":10,"default":1,"description":"The volume of the generated speech. Range: (0, 10]. Larger values indicate larger volumes."},"pitch":{"type":"number","minimum":-12,"maximum":12,"default":0,"description":"The pitch of the generated speech. Range: [-12, 12]. 0 = default voice output."},"emotion":{"type":"string","enum":["happy","sad","angry","fearful","disgusted","surprised","neutral"],"description":"Emotional tone to apply to the synthesized speech. Controls the emotional expression of the generated voice output."},"text_normalization":{"type":"boolean","default":false,"description":"English text normalization support. Improves number-reading but increases latency."}},"required":["voice_id"],"description":"Voice settings overriding stored settings for the given voice. They are applied only on the given request."},"audio_setting":{"type":"object","properties":{"sample_rate":{"type":"integer","description":"Audio sample rate in Hz.","enum":[8000,16000,22050,24000,32000,44100]},"bitrate":{"type":"integer","description":"Audio bitrate in bits per second. Controls the compression level and audio quality. Higher bitrates provide better quality but larger file sizes.","enum":[32000,64000,128000,256000]},"format":{"type":"string","enum":["mp3","pcm","flac"],"default":"mp3","description":"Audio output format. MP3 provides good compression and compatibility, PCM offers uncompressed high quality, and FLAC provides lossless compression."},"channel":{"type":"integer","description":"Number of audio channels. 1 for mono (single channel), 2 for stereo (dual channel) output.","enum":[1,2]}},"description":"Audio output configuration"},"pronunciation_dict":{"type":"object","properties":{"tone":{"type":"array","items":{"type":"string"},"description":"Replacement of text and pronunciations. Format: [\"燕少飞/(yan4)(shao3)(fei1)\", \"达菲/(da2)(fei1)\", \"omg/oh my god\"]"}},"required":["tone"],"description":"Custom pronunciation dictionary for handling specific words or phrases. Allows fine-tuning of how certain text should be pronounced using phonetic representations."},"timbre_weights":{"type":"array","items":{"type":"object","properties":{"voice_id":{"type":"string","enum":["Wise_Woman","Friendly_Person","Inspirational_girl","Deep_Voice_Man","Calm_Woman","Casual_Guy","Lively_Girl","Patient_Man","Young_Knight","Determined_Man","Lovely_Girl","Decent_Boy","Imposing_Manner","Elegant_Man","Abbess","Sweet_Girl_2","Exuberant_Girl"],"description":"Voice identifier for text-to-speech synthesis. Supports both predefined system voices and custom cloned voice IDs. "},"weight":{"type":"integer","minimum":1,"maximum":100,"description":"Weight for voice mixing. Range: [1, 100]. Higher weights are sampled more heavily."}},"required":["voice_id","weight"]},"maxItems":4,"description":"Voice mixing configuration allowing combination of up to 4 different voices with specified weights. Each voice contributes to the final output based on its weight value (1-100)."},"stream":{"type":"boolean","default":false,"description":"Enable streaming mode for real-time audio generation. When enabled, audio is generated and delivered in chunks as it's processed."},"language_boost":{"type":"string","enum":["Chinese","Chinese,Yue","English","Arabic","Russian","Spanish","French","Portuguese","German","Turkish","Dutch","Ukrainian","Vietnamese","Indonesian","Japanese","Italian","Korean","Thai","Polish","Romanian","Greek","Czech","Finnish","Hindi","Bulgarian","Danish","Hebrew","Malay","Persian","Slovak","Swedish","Croatian","Filipino","Hungarian","Norwegian","Slovenian","Catalan","Nynorsk","Tamil","Afrikaans","auto"],"description":"Language recognition enhancement option."},"voice_modify":{"type":"object","properties":{"pitch":{"type":"integer","minimum":-100,"maximum":100,"description":"Adjusts voice pitch. Range: [-100, 100]. -100: deeper, 100: lighter"},"intensity":{"type":"integer","minimum":-100,"maximum":100,"description":"Adjusts voice intensity. Range: [-100, 100]. -100: stronger, 100: softer"},"timbre":{"type":"integer","minimum":-100,"maximum":100,"description":"Adjusts voice timbre. Range: [-100, 100]. -100: increased nasality, 100: crisper"},"sound_effects":{"type":"string","enum":["spacious_echo","auditorium_echo","lofi_telephone","robotic"],"description":"Audio effects to apply to the synthesized speech. Includes options like spacious_echo, auditorium_echo, lofi_telephone, and robotic effects."}},"description":"Voice modification settings for adjusting pitch, intensity, timbre, and applying sound effects to customize the voice characteristics."},"subtitle_enable":{"type":"boolean","default":false,"description":"Enable subtitle generation service. Only available for non-streaming requests. Generates timing information for the synthesized speech."},"output_format":{"type":"string","enum":["url","hex"],"default":"hex","description":"Format of the output content for non-streaming requests. Controls how the generated audio data is encoded in the response."}},"required":["model","text"]}}}},"responses":{"201":{"description":"","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Voice.v1.TextToSpeechResponse"}}}}},"tags":["Voice Models"]}}}}
```
