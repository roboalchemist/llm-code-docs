# Source: https://firebase.google.com/docs/reference/js/vertexai.baseparams.md.txt

# BaseParams interface

Base parameters for a number of methods.

**Signature:**  

    export interface BaseParams 

## Properties

|                                                      Property                                                       |                                                           Type                                                            | Description |
|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|-------------|
| [generationConfig](https://firebase.google.com/docs/reference/js/vertexai.baseparams.md#baseparamsgenerationconfig) | [GenerationConfig](https://firebase.google.com/docs/reference/js/vertexai.generationconfig.md#generationconfig_interface) |             |
| [safetySettings](https://firebase.google.com/docs/reference/js/vertexai.baseparams.md#baseparamssafetysettings)     | [SafetySetting](https://firebase.google.com/docs/reference/js/vertexai.safetysetting.md#safetysetting_interface)\[\]      |             |

## BaseParams.generationConfig

**Signature:**  

    generationConfig?: GenerationConfig;

## BaseParams.safetySettings

**Signature:**  

    safetySettings?: SafetySetting[];