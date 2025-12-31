# Source: https://firebase.google.com/docs/reference/js/ai.languagemodelcreatecoreoptions.md.txt

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Configures the creation of an on-device language model session.

**Signature:**  

    export interface LanguageModelCreateCoreOptions 

## Properties

|                                                                     Property                                                                      |                                                                  Type                                                                  |      Description       |
|---------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| [expectedInputs](https://firebase.google.com/docs/reference/js/ai.languagemodelcreatecoreoptions.md#languagemodelcreatecoreoptionsexpectedinputs) | [LanguageModelExpected](https://firebase.google.com/docs/reference/js/ai.languagemodelexpected.md#languagemodelexpected_interface)\[\] | ***(Public Preview)*** |
| [temperature](https://firebase.google.com/docs/reference/js/ai.languagemodelcreatecoreoptions.md#languagemodelcreatecoreoptionstemperature)       | number                                                                                                                                 | ***(Public Preview)*** |
| [topK](https://firebase.google.com/docs/reference/js/ai.languagemodelcreatecoreoptions.md#languagemodelcreatecoreoptionstopk)                     | number                                                                                                                                 | ***(Public Preview)*** |

## LanguageModelCreateCoreOptions.expectedInputs

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    expectedInputs?: LanguageModelExpected[];

## LanguageModelCreateCoreOptions.temperature

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    temperature?: number;

## LanguageModelCreateCoreOptions.topK

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    topK?: number;