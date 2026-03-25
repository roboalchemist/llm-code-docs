# Source: https://docs.verda.com/inference/audio-models/whisper.md

# Whisper

## Overview

The Verda Whisper Inference Service provides access to the Whisper v3 large model endpoint. The endpoint includes advanced options diarization, phoneme alignment for word-level timestamps, and subtitle generation in SRT format.

### Transcribing Audio

To transcribe audio, submit a request with the audio file URL.

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST https://inference.datacrunch.io/whisper/predict \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_api_key>" \
  -d \
'{
    "audio_input": "<AUDIO_FILE_URL>"
}'
```

{% endtab %}

{% tab title="Python" %}

```python
import requests

url = "https://inference.datacrunch.io/whisper/predict"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <your_api_key>"
}
data = {
    "audio_input": "<AUDIO_FILE_URL>"
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const axios = require('axios');

const url = 'https://inference.datacrunch.io/whisper/predict';
const headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <your_api_key>'
};
const data = {
  audio_input: '<AUDIO_FILE_URL>'
};

axios.post(url, data, { headers: headers })
  .then((response) => {
    console.log(response.data);
  })
  .catch((error) => {
    console.error('Error:', error);
  });
```

{% endtab %}
{% endtabs %}

### Translating Audio

For translation of the transcribed output to English:

```bash
curl -X POST https://inference.datacrunch.io/whisper/predict \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_api_key>" \
  -d \
'{
    "audio_input": "<AUDIO_FILE_URL>",
    "translate": true
}'
```

### Generating Subtitles

When creating subtitles it is best to set `processing_type="align"`, to ensure word-level alignment. Omitting the alignment will result in longer subtitle chunks, potentially leading to worse user experience. Setting `output="subtitles"` ensures that the output is in SRT format.

```bash
curl -X POST https://inference.datacrunch.io/whisper/predict \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_api_key>" \
  -d \
'{
    "audio_input": "<AUDIO_FILE_URL>",
    "translate": true,
    "processing_type": "align",
    "output": "subtitles"
}'
```

### Performing Speaker Diarization

For speaker diarization (assigning speaker labels to text segments), set `processing_type` to `diarize`:

```bash
curl -X https://inference.datacrunch.io/whisper/predict \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_api_key>" \
  -d \
'{
    "audio_input": "<AUDIO_FILE_URL>",
    "translate": true,
    "processing_type": "diarize"
}'
```

## API Parameters

* **audio\_input** (`str`, ***required***): URL of the audio file. This is a required parameter.
* **translate** (`bool`, *optional*): If enabled, provides the English translation of the output. Defaults to `false`.
* **language** (`str`, *optional*): Optional two-letter language code to specify the input language for accurate language detection.
* **processing\_type** (`str`, *optional*): Defines the processing action. Supported types: `diarize`, `align`.
* **output** (`str`), *optional*): Determines the output format. Options: `subtitles` (in SRT format), `raw` (time-stamped text). Default is `raw`.

*Copyright notice: WhisperX includes software developed by Max Bain.*
