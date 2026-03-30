# Source: https://firebase.google.com/docs/reference/js/ai.transcription.md.txt

# Transcription interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Transcription of audio. This can be returned from a [LiveGenerativeModel](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel.md#livegenerativemodel_class) if transcription is enabled with the `inputAudioTranscription` or `outputAudioTranscription` properties on the [LiveGenerationConfig](https://firebase.google.com/docs/reference/js/ai.livegenerationconfig.md#livegenerationconfig_interface).

**Signature:**

    export interface Transcription 

## Properties

| Property | Type | Description |
|---|---|---|
| [text](https://firebase.google.com/docs/reference/js/ai.transcription.md#transcriptiontext) | string | ***(Public Preview)*** The text transcription of the audio. |

## Transcription.text

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The text transcription of the audio.

**Signature:**

    text?: string;