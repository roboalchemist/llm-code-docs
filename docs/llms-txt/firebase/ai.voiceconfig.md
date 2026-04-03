# Source: https://firebase.google.com/docs/reference/js/ai.voiceconfig.md.txt

# VoiceConfig interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Configuration for the voice to used in speech synthesis.

**Signature:**  

    export interface VoiceConfig 

## Properties

|                                                       Property                                                        |                                                             Type                                                             |                                    Description                                     |
|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [prebuiltVoiceConfig](https://firebase.google.com/docs/reference/js/ai.voiceconfig.md#voiceconfigprebuiltvoiceconfig) | [PrebuiltVoiceConfig](https://firebase.google.com/docs/reference/js/ai.prebuiltvoiceconfig.md#prebuiltvoiceconfig_interface) | ***(Public Preview)*** Configures the voice using a pre-built voice configuration. |

## VoiceConfig.prebuiltVoiceConfig

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Configures the voice using a pre-built voice configuration.

**Signature:**  

    prebuiltVoiceConfig?: PrebuiltVoiceConfig;