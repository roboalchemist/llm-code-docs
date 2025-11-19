# Source: https://docs.baseten.co/examples/models/mars/MARS6.md

# MARS6

> MARS6 is a frontier text-to-speech model by CAMB.AI with voice/prosody cloning capabilities in 10 languages. MARS6 must be licensed for commercial use, we can help!

export const MarsIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_631_10869)">
<path fill-rule="evenodd" clip-rule="evenodd" d="M8.63156 18.1049L8.57257 18.2142C8.49832 18.3766 8.47037 18.5619 8.50142 18.7515C8.58658 19.2656 9.07928 19.6143 9.60131 19.53C9.86988 19.487 10.0939 19.3379 10.2364 19.1336L10.3133 19.0025L10.8178 18.1398C10.8208 18.1325 10.8243 18.1256 10.8274 18.1183C10.8588 18.0512 10.8968 17.9881 10.9405 17.9296L11.846 16.3821L12.7455 17.9193C12.7926 17.9812 12.8332 18.0478 12.8669 18.1187C12.872 18.1299 12.8768 18.1411 12.8817 18.1523L13.3736 18.9931L13.4614 19.1431C13.6042 19.343 13.8256 19.4879 14.0899 19.5305C14.6123 19.6143 15.1046 19.2656 15.1902 18.752C15.2226 18.5568 15.1915 18.3654 15.1116 18.1991L15.0692 18.1205L13.7435 15.6581L13.5976 15.3873L13.5251 15.2528C13.3526 15.0061 13.1254 14.7988 12.8603 14.6488C12.562 14.4798 12.2155 14.3831 11.8469 14.3831C11.4773 14.3831 11.131 14.4803 10.8322 14.6496C10.5636 14.8018 10.3338 15.0125 10.1608 15.2643L9.95551 15.6457L8.63109 18.1062L8.63156 18.1049Z" fill="black" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M1.72147 19.175L10.1396 9.01879C10.168 8.98181 10.1977 8.94614 10.2287 8.91132C10.6219 8.46725 11.201 8.18611 11.8471 8.18611C12.4935 8.18611 13.0732 8.46769 13.4668 8.91259C13.4969 8.94656 13.5258 8.98138 13.5533 9.01749L13.8638 9.39191L21.9453 19.1419L22.0374 19.2532C22.212 19.4337 22.4585 19.5468 22.7319 19.5468C23.2609 19.5468 23.6898 19.1247 23.6898 18.6041C23.6898 18.4142 23.633 18.2375 23.5347 18.0896L23.4523 17.9829L16.7682 9.31368L15.4 7.53915L15.2607 7.35903L13.8633 5.54626L13.5043 5.0807C13.4873 5.0605 13.4703 5.04073 13.4528 5.02095C13.0596 4.58463 12.4857 4.30951 11.8462 4.30951C11.2068 4.30951 10.6328 4.58463 10.2396 5.02095C10.2222 5.03986 10.2057 5.05963 10.189 5.07941L10.0846 5.21483L9.82908 5.54583L8.42857 7.36247L8.29277 7.53872L6.92165 9.31711L0.255963 17.9623L0.140661 18.1119C0.0515526 18.255 0 18.4235 0 18.6036C0 19.1243 0.428953 19.5464 0.957925 19.5464C1.24666 19.5464 1.50525 19.4209 1.68128 19.2223L1.72059 19.175H1.72147Z" fill="black" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M10.0556 10.4893L4.29329 17.9627L4.17751 18.1127C4.08841 18.2558 4.03729 18.4243 4.03729 18.6045C4.03729 19.1251 4.46626 19.5472 4.99523 19.5472C5.28396 19.5472 5.54298 19.4212 5.71859 19.2227L5.75658 19.177L10.2649 13.7379C10.6572 13.3158 11.2219 13.0505 11.8492 13.0505C12.4769 13.0505 13.0417 13.3158 13.4339 13.7383L17.9138 19.1427L18.0055 19.2535C18.1803 19.4346 18.427 19.5472 18.7006 19.5472C19.2294 19.5472 19.6585 19.1251 19.6585 18.6045C19.6585 18.4149 19.6016 18.2378 19.5033 18.0903L19.4208 17.9834L13.4693 10.2641C13.4562 10.2495 13.4436 10.2353 13.43 10.2211C13.0377 9.80067 12.4747 9.53717 11.8492 9.53717C11.2219 9.53717 10.6572 9.80196 10.2649 10.2241C10.2531 10.237 10.2413 10.2499 10.2295 10.2632L10.0556 10.4893Z" fill="black" />
</g>
<defs>
<clipPath id="clip0_631_10869">
<rect width="24" height="16" fill="white" transform="translate(0 4)" />
</clipPath>
</defs>
</svg>} horizontal />;

<MarsIconCard title="Deploy MARS6" href="https://app.baseten.co/deploy/mars-6r-tts" />

## Example usage

This model requires at least four inputs:

1. `text`: The input text that needs to be spoken
2. `audio_ref`: An audio file containing the audio of a single person
3. `ref_text`: What is spoken in audio\_ref
4. `language`: The language code for the target language

The model will try to output an audio stream containing the speech in the reference audio's style. The output is by default an HTTP1.1 chunked encoding response of an encoded audio file using an ADTS AAC stream, but can be configured to stream using flac format, or to not stream at all and return the entire response as a base64 encoded flac file.

```
data = {"text": "The quick brown fox jumps over the lazy dog",
        "audio_ref": encoded_str,
        "ref_text": prompt_txt,
        "language": 'en-us', # Target language, in this case english.
        # "top_p": 0.7, # Optionally specify a top_p (default 0.7)
        # "temperature": 0.7, # Optionally specify a temperature (default 0.7)
        # "chunk_length": 200, # Optional text chunk length for splitting long pieces of input text. Default 200
        # "max_new_tokens": 0, # Optional limit on max number of new tokens, default is zero (unlimited)
        # "repetition_penalty": 1.5 # Optional rep penalty, default 1.5
}
```

## Input

```python  theme={"system"}
import base64
import time
import torchaudio
import requests
import IPython.display as ipd
import librosa, librosa.display
import torch
import io
from torchaudio.io import StreamReader

# Step 1: set endpoint url and api key:
url = "<YOUR PREDICTION ENDPOINT>"
headers = {"Authorization": "Api-Key <YOUR API KEY>"}

# Step 2: pick reference audio to clone, encode it as base64
file_path = "ref_debug.flac"  # any valid audio filepath, ideally between 6s-90s.
wav, sr = librosa.load(file_path, sr=None, mono=True, offset=0, duration=5)
io_data = io.BytesIO()
torchaudio.save(io_data, torch.from_numpy(wav)[None], sample_rate=sr, format="wav")
io_data.seek(0)
encoded_data = base64.b64encode(io_data.read())
encoded_str = encoded_data.decode("utf-8")
# OPTIONAL: specify the transcript of the reference/prompt (slightly speeds up inference, and may make it sound a bit better).
prompt_txt = None  # if unspecified, can be left as None

# Step 3: define other inference settings:
data = {
    "text": "The quick brown fox jumps over the lazy dog",
    "audio_ref": encoded_str,
    "ref_text": prompt_txt,
    "language": "en-us",  # Target language, in this case english.
    # "top_p": 0.7, # Optionally specify a top_p (default 0.7)
    # "temperature": 0.7, # Optionally specify a temperature (default 0.7)
    # "chunk_length": 200, # Optional text chunk length for splitting long pieces of input text. Default 200
    # "max_new_tokens": 0, # Optional limit on max number of new tokens, default is zero (unlimited)
    # "repetition_penalty": 1.5 # Optional rep penalty, default 1.5
    # stream: bool = True # whether to stream the response back as an HTTP1.1 chunked encoding response, or run to completion and return the base64 encoded file.
    # stream_format: str = "adts" # 'adts' or 'flac' for stream format. Default 'adts'
}

st = time.time()


class UnseekableWrapper:
    def __init__(self, obj):
        self.obj = obj

    def read(self, n):
        return self.obj.read(n)


# Step 4: Send the POST request (note the first request might be a bit slow, but following requests should be fast)
response = requests.post(url, headers=headers, json=data, stream=True, timeout=300)
streamer = StreamReader(UnseekableWrapper(response.raw))
streamer.add_basic_audio_stream(
    11025, buffer_chunk_size=3, sample_rate=44100, num_channels=1
)

# Step 4.1: check the header format of the returned stream response
for i in range(streamer.num_src_streams):
    print(streamer.get_src_stream_info(i))

# Step 5: stream the response back and decode it on-the-fly
audio_samples = []
for chunks in streamer.stream():
    audio_chunk = chunks[0]
    audio_samples.append(
        audio_chunk._elem.squeeze()
    )  # this is now just a (T,) float waveform, however you can set your own output format bove.
    print(
        f"Playing audio chunk of size {audio_chunk._elem.squeeze().shape} at {time.time() - st:.2f}s."
    )
    # If you wish, you can also play each chunk as you receive it, e.g. using IPython:
    # ipd.display(ipd.Audio(audio_chunk._elem.squeeze().numpy(), rate=44100, autoplay=True))

# Step 6: concatenate all the audio chunks and play the full audio (if you didn't play them on the fly above)
final_full_audio = torch.concat(audio_samples, dim=0)  # (T,) float waveform @ 44.1kHz
# ipd.display(ipd.Audio(final_full_audio.numpy(), rate=44100))
```

## Output

```json  theme={"system"}
{
    "reuslt": "base64 encoded audio data",\
}
```
