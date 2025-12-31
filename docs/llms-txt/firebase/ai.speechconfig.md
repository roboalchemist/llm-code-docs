# Source: https://firebase.google.com/docs/reference/js/ai.speechconfig.md.txt

# SpeechConfig interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Configures speech synthesis.

**Signature:**  

    export interface SpeechConfig 

## Properties

|                                                Property                                                 |                                                 Type                                                 |                                 Description                                 |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [voiceConfig](https://firebase.google.com/docs/reference/js/ai.speechconfig.md#speechconfigvoiceconfig) | [VoiceConfig](https://firebase.google.com/docs/reference/js/ai.voiceconfig.md#voiceconfig_interface) | ***(Public Preview)*** Configures the voice to be used in speech synthesis. |

## SpeechConfig.voiceConfig

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Configures the voice to be used in speech synthesis.

**Signature:**  

    voiceConfig?: VoiceConfig;