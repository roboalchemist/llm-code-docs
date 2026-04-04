# Install dependencies - CHANGE THIS to `apk`
RUN apt-get update && apt-get install -y dumb-init

```

Before Change

```codeBlockLines_e6Vv
RUN apt-get update && apt-get install -y dumb-init

```

After Change

```codeBlockLines_e6Vv
RUN apk update && apk add --no-cache dumb-init

```

`deepgram`, `fireworks ai`, `vision`, `admin ui`, `dependency upgrades`

## New Models [​](https://docs.litellm.ai/release_notes\#new-models "Direct link to New Models")

### **Deepgram Speech to Text** [​](https://docs.litellm.ai/release_notes\#deepgram-speech-to-text "Direct link to deepgram-speech-to-text")

New Speech to Text support for Deepgram models. [**Start Here**](https://docs.litellm.ai/docs/providers/deepgram)

```codeBlockLines_e6Vv
from litellm import transcription
import os