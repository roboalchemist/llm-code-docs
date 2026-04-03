# Source: https://firebase.google.com/docs/reference/js/ai.prebuiltvoiceconfig.md.txt

# PrebuiltVoiceConfig interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Configuration for a pre-built voice.

**Signature:**  

    export interface PrebuiltVoiceConfig 

## Properties

|                                                     Property                                                      |  Type  |                                                                                                      Description                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [voiceName](https://firebase.google.com/docs/reference/js/ai.prebuiltvoiceconfig.md#prebuiltvoiceconfigvoicename) | string | ***(Public Preview)*** The voice name to use for speech synthesis.For a full list of names and demos of what each voice sounds like, see [Chirp 3: HD Voices](https://cloud.google.com/text-to-speech/docs/chirp3-hd). |

## PrebuiltVoiceConfig.voiceName

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The voice name to use for speech synthesis.

For a full list of names and demos of what each voice sounds like, see [Chirp 3: HD Voices](https://cloud.google.com/text-to-speech/docs/chirp3-hd).

**Signature:**  

    voiceName?: string;