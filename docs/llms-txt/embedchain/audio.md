# Source: https://docs.embedchain.ai/components/data-sources/audio.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 🎤 Audio

To use an audio as data source, just add `data_type` as `audio` and pass in the path of the audio (local or hosted).

We use [Deepgram](https://developers.deepgram.com/docs/introduction) to transcribe the audiot to text, and then use the generated text as the data source.

You would require an Deepgram API key which is available [here](https://console.deepgram.com/signup?jump=keys) to use this feature.

### Without customization

```python  theme={null}
import os
from embedchain import App

os.environ["DEEPGRAM_API_KEY"] = "153xxx"

app = App()
app.add("introduction.wav", data_type="audio")
response = app.query("What is my name and how old am I?")
print(response)
# Answer: Your name is Dave and you are 21 years old.
```
