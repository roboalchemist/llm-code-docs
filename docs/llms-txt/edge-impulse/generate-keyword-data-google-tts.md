# Source: https://docs.edgeimpulse.com/tutorials/topics/data/generate-keyword-data-google-tts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate keyword data using Google TTS

<a href="https://colab.research.google.com/github/edgeimpulse/notebooks/blob/main/notebooks/generate-keyword-spotting-dataset.ipynb" target="_blank">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Google Colab" noZoom />
</a>

### Local Software Requirements

* Python 3
* Pip package manager
* Jupyter Notebook: [https://jupyter.org/install](https://jupyter.org/install)
* pip packages (install with `pip install`*`packagename`*):
  * pydub [https://pypi.org/project/pydub/](https://pypi.org/project/pydub/)
  * google-cloud-texttospeech [https://cloud.google.com/python/docs/reference/texttospeech/latest](https://cloud.google.com/python/docs/reference/texttospeech/latest)
  * requests [https://pypi.org/project/requests/](https://pypi.org/project/requests/)

```python  theme={"system"}
# Imports
import os
import json
import time
import io
import random
import requests
from pydub import AudioSegment
from google.cloud import texttospeech
```

## Set up Google TTS API

First off you will need to set up and Edge Impulse account and create your first project. You will also need a Google Cloud account with the Text to Speech API enabled: [https://cloud.google.com/text-to-speech](https://cloud.google.com/text-to-speech), the first million characters generated each month are free (WaveNet voices), this should be plenty for most cases as you'll only need to generate your dataset once. From google you will need to download a credentials JSON file and set it to the correct environment variable on your system to allow the python API to work: ([https://developers.google.com/workspace/guides/create-credentials#service-account](https://developers.google.com/workspace/guides/create-credentials#service-account))

```python  theme={"system"}

# Insert the path to your service account API key json file here for google cloud
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../path-to-google-credentials-file.json'
```

## Generate the desired samples

First off we need to set our desired keywords and labels:

```python  theme={"system"}

# Keyword or short sentence and label (e.g. 'hello world')
keyword = [
    {'string':'edge','label':'edge'},
    {'string':'impulse','label':'impulse'},
           ]
```

Then we need to set up the parameters for our speech dataset, all possible combinations will be iterated through:

* languages - Choose the text to speech voice languages to use ([https://cloud.google.com/text-to-speech/docs/voices](https://cloud.google.com/text-to-speech/docs/voices))
* pitches - Which voice pitches to apply
* genders - Which SSML genders to apply
* speakingRates - Which speaking speeds to apply

```python  theme={"system"}


# Languages, remove as appropriate
# languages = [
#     'ar-XA', 'bn-IN',  'en-GB',  'fr-CA',
#     'en-US', 'es-ES',  'fi-FI',  'gu-IN',
#     'ja-JP', 'kn-IN',  'ml-IN',  'sv-SE',
#     'ta-IN', 'tr-TR',  'cs-CZ',  'de-DE',
#     'en-AU', 'en-IN',  'fr-FR',  'hi-IN',
#     'id-ID', 'it-IT',  'ko-KR',  'ru-RU',
#     'uk-UA', 'cmn-CN', 'cmn-TW', 'da-DK',
#     'el-GR', 'fil-PH', 'hu-HU',  'nb-NO',
#     'nl-NL', 'pt-PT',  'sk-SK',  'vi-VN',
#     'pl-PL', 'pt-BR',  'ca-ES',  'yue-HK',
#     'af-ZA', 'bg-BG',  'lv-LV',  'ro-RO',
#     'sr-RS', 'th-TH',  'te-IN',  'is-IS'
# ]
languages = [
    'en-GB',
    'en-US',
]
# Pitches to generate (in semitones) range: [-20.0, 20.0]
pitches = [-2, 0, 2]
# Voice genders to use
genders = ["NEUTRAL", "FEMALE", "MALE"]
# Speaking rates to use range: [0.25, 4.0]
speakingRates = [0.9, 1, 1.1]


```

Then provide some other key parameters:

* out\_length - How long each output sample should be
* count - Maximum number of samples to output (if all combinations of languages, pitches etc are higher then this restricts output)
* voice-dir - Where to store the clean samples before noise is added
* noise-url - Which noise file to download and apply to your samples
* output-folder - The final output location of the noised samples
* num-copies - How many different noisy versions of each sample to create
* max-noise-level - in Db,

```python  theme={"system"}
# Out length minimum (default: 1s)
out_length = 1
# Maximum number of keywords to generate
count = 30
# Raw sample output directory
voice_dir = 'out-wav'
# Creative commons background noise from freesound.org:https://freesound.org/people/Astounded/sounds/483561/
noise_url = 'https://cdn.freesound.org/previews/483/483561_10201334-lq.ogg'
output_folder = 'out-noisy'
num_copies = 2  # Number of noisy copies to create for each input sample
max_noise_level = -5  # Maximum noise level to add in dBFS (negative value)

```

Then we need to check all the output folders are ready

```python  theme={"system"}

# Check if output directory for noisey files exists and create it if it doesn't
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# Check if output directory for raw voices exists and create it if it doesn't
if not os.path.exists(voice_dir):
    os.makedirs(voice_dir)

```

And download the background noise file

```python  theme={"system"}

# Download background noise file
response = requests.get(noise_url)
response.raise_for_status()
noise_audio = AudioSegment.from_file(io.BytesIO(response.content), format='ogg')

```

Then we can generate a list of all possible parameter combinations based on the input earlier. If you have set `num_copies` to be smaller than the number of combinations then these options will be reduced:

```python  theme={"system"}

# Generate all combinations of parameters
all_opts = []
for p in pitches:
    for g in genders:
        for l in languages:
            for s in speakingRates:
                for kw in keyword:
                    all_opts.append({
                            "pitch": p,
                            "gender": g,
                            "language": l,
                            "speakingRate": s,
                            "text": kw['string'],
                            "label": kw['label']
                        })
if len(all_opts)*num_copies > count:
    selectEvery = len(all_opts)*num_copies // count
    selectNext = 0
    all_opts = all_opts[::selectEvery]
print(f'Generating {len(all_opts)*num_copies} samples')
```

Finally we iterate though all the options generated, call the Google TTS API to generate the desired sample, and apply noise to it, saving locally with metadata:

```python  theme={"system"}

# Instantiate list for file label information
downloaded_files = []

# Instantiates a client
client = texttospeech.TextToSpeechClient()

ix = 0
for o in all_opts:
    ix += 1
    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=o['text'])
    # Build the voice request
    voice = texttospeech.VoiceSelectionParams(
        language_code=o['language'],
        ssml_gender=o['gender']
    )
    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        pitch=o['pitch'],
        speaking_rate=o['speakingRate'],
        sample_rate_hertz=16000
    )
    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type

    wav_file_name = f"{voice_dir}/{o['label']}.{o['language']}-{o['gender']}-{o['pitch']}-{o['speakingRate']}.tts.wav"

    if not os.path.exists(wav_file_name):
        print(f"[{ix}/{len(all_opts)}] Text-to-speeching...")
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        with open(wav_file_name, "wb") as f:
            f.write(response.audio_content)
        has_hit_api = True
    else:
        print(f'skipping {wav_file_name}')
        has_hit_api = False

    # Load voice sample
    voice_audio = AudioSegment.from_file(wav_file_name)
    # Add silence to match output length with random padding
    difference = (out_length * 1000) - len(voice_audio)
    if difference > 0:
        padding_before = random.randint(0, difference)
        padding_after = difference - padding_before
        voice_audio = AudioSegment.silent(duration=padding_before) +  voice_audio + AudioSegment.silent(duration=padding_after)

    for i in range(num_copies):
        # Save noisy sample to output folder
        output_filename = f"{o['label']}.{o['language']}-{o['gender']}-{o['pitch']}-{o['speakingRate']}_noisy_{i+1}.wav"
        output_path = os.path.join(output_folder, output_filename)
        if not os.path.exists(output_path):
            # Select random section of noise and random noise level
            start_time = random.randint(0, len(noise_audio) - len(voice_audio))
            end_time = start_time +len(voice_audio)
            noise_level = random.uniform(max_noise_level, 0)

            # Extract selected section of noise and adjust volume
            noise_segment = noise_audio[start_time:end_time]
            noise_segment = noise_segment - abs(noise_level)

            # Mix voice sample with noise segment
            mixed_audio = voice_audio.overlay(noise_segment)
            # Save mixed audio to file
            mixed_audio.export(output_path, format='wav')

            print(f'Saved mixed audio to {output_path}')
        else:
            print(f'skipping {output_path}')
        # Save metadata for file
        downloaded_files.append({
            "path": str(output_filename),
            "label": o['label'],
            "category": "split",
            "metadata": {
                "pitch": str(['pitch']),
                "gender": str(o['gender']),
                "language": str(o['language']),
                "speakingRate": str(o['speakingRate']),
                "text": o['text'],
                "imported_from": "Google Cloud TTS"
            }
        })

    if has_hit_api:
        time.sleep(0.5)

print("Done text-to-speeching")
print("")

input_file = os.path.join(output_folder, 'input.json')
info_file = {
    "version": 1,
    "files": downloaded_files
}
# Output the metadata file
with open(input_file, "w") as f:
    json.dump(info_file, f)
```

The files in `./out-noisy` can be uploaded easily using the [Edge Impulse CLI tool](/tools/clis/edge-impulse-cli/uploader):

```python  theme={"system"}
# Move to the out-noisy folder
! cd out-noisy
# Upload all files in the out-noisy folder with metadata attached in the input.json file
! edge-impulse-uploader --info-file input.json *
```

## What next?

Now you can use your keywords to create a robust keyword detection model in Edge Impulse Studio!

Make use of our pre-built keyword dataset to add noise and 'unknown' words to your model: [Keyword Spotting Dataset](/datasets/audio/keyword-spotting)

Try out both classification models and the transfer learning keyword spotting model to see which works best for your case


Built with [Mintlify](https://mintlify.com).