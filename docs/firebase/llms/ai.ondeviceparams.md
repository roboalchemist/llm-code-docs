# Source: https://firebase.google.com/docs/reference/js/ai.ondeviceparams.md.txt

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Encapsulates configuration for on-device inference.

**Signature:**  

    export interface OnDeviceParams 

## Properties

|                                                    Property                                                     |                                                                       Type                                                                        |      Description       |
|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| [createOptions](https://firebase.google.com/docs/reference/js/ai.ondeviceparams.md#ondeviceparamscreateoptions) | [LanguageModelCreateOptions](https://firebase.google.com/docs/reference/js/ai.languagemodelcreateoptions.md#languagemodelcreateoptions_interface) | ***(Public Preview)*** |
| [promptOptions](https://firebase.google.com/docs/reference/js/ai.ondeviceparams.md#ondeviceparamspromptoptions) | [LanguageModelPromptOptions](https://firebase.google.com/docs/reference/js/ai.languagemodelpromptoptions.md#languagemodelpromptoptions_interface) | ***(Public Preview)*** |

## OnDeviceParams.createOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    createOptions?: LanguageModelCreateOptions;

## OnDeviceParams.promptOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    promptOptions?: LanguageModelPromptOptions;